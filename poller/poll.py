import copy
import requests


class Poll:
    """
    This class represents a topic in Discourse dedicated to a particular competition. When initialised,
    it will use the supplied topic ID to get data about the topic and its constituent posts, and will
    derive the list of posters ("entrants") in the topic.
    """

    def __init__(self, topic_id):
        self.target_url = f"https://boards.straightdope.com/t/{topic_id}.json"
        self.errors = []

        response = self._get_thread()
        if not self.errors:
            raw_data = response.json()
            post_stream = raw_data["post_stream"]

            self._posts = post_stream["posts"]
            self._post_refs = post_stream["stream"]
            self.all_posts = copy.deepcopy(self._posts)

            #  The initial API call returns the first 20 posts, and references to the rest which we need to get.
            self._unfetched_posts = self._post_refs[20:]
            for post_ref in self._unfetched_posts:
                response = self._get_single_post(post_ref)
                if not self.errors:
                    raw_data = response.json()
                    self.all_posts.append(raw_data)

            self.all_entrants = [post["username"] for post in self.all_posts]

    def _get_thread(self):
        """
        Get all posts in a thread, using the Discourse API.
        """
        try:
            response = requests.get(self.target_url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as timeout_error:
            self.errors.append(timeout_error)
        except requests.exceptions.HTTPError as http_error:
            self.errors.append(http_error)
        except Exception as uncaught_exception:
            self.errors.append(uncaught_exception)

    def _get_single_post(self, post_ref):
        """
        Get single post using the Discourse API:
        https://boards.straightdope.com/posts/<post_ref>.json
        We need this because the API call to get the thread only returns the first 20 posts, and just pointers
        ("post refs") to any other posts after the first 20 - so we have to get those separately one at a time
        """
        target_url = f"https://boards.straightdope.com/posts/{post_ref}.json"
        try:
            response = requests.get(target_url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as timeout_error:
            self.errors.append(timeout_error)
        except requests.exceptions.HTTPError as http_error:
            self.errors.append(http_error)
        except Exception as uncaught_exception:
            self.errors.append(uncaught_exception)

    def __str__(self):
        return f"Poll object with {len(self.all_entrants)} entries"

    def __repr__(self):
        return f"Poll object with {len(self.all_entrants)} entries"


if __name__ == '__main__':
    poll = Poll('984627')
    print(poll)
