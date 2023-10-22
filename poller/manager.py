"""
The main interface for other code to call poller.
"""
from .discourse_thread import DiscourseThread
from .output import Output


class Manager:
    """
    An instance of the Manager class is the interface for other code to work with poller. The class orchestrates the
    retrieval and parsing of the thread and the production of the rendered output, and abstracts the logic away from
    the calling code.
    """

    def __init__(self, topic_id, voting_deadline):
        self.topic_id = topic_id
        self.voting_deadline = voting_deadline
        self.entrants = self._get_entrants()
        self.output = self._get_rendered_output()

    def _get_entrants(self):
        """
        Create a list of posters in a thread.
        """
        poll = DiscourseThread(self.topic_id)
        return poll.all_entrants

    def _get_rendered_output(self):
        """
        Render the output, merging the list of posters with a template to produce text that can be pasted into a Discourse
        thread to display a poll.
        """
        output = Output(self.entrants, self.voting_deadline)
        return output.render()
