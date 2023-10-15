from .discourse_thread import DiscourseThread
from .output import Output


class Manager:
    def __init__(self, topic_id, voting_deadline):
        self.topic_id = topic_id
        self.voting_deadline = voting_deadline
        self.entrants = self._get_entrants()
        self.output = self._get_rendered_output()

    def _get_entrants(self):
        poll = DiscourseThread(self.topic_id)
        return poll.all_entrants

    def _get_rendered_output(self):
        output = Output(self.entrants, self.voting_deadline)
        return output.render()
