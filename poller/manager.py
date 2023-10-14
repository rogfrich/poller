from .poll import Poll
from .output import Output


class Manager:
    def __init__(self, topic_id, voting_deadline):
        self.topic_id = topic_id
        self.poll: Poll = Poll(topic_id)
        self.entrants = self.poll.all_entrants
        self.output = Output(self.entrants, voting_deadline)

