"""
Create a formatted text output that can be easily pasted into a Discourse post to create a poll.
"""
from jinja2 import Environment, FileSystemLoader


class Output:
    """
    Creates formatted text that can be copy-pasted directly into Discourse with no further formatting to create a voting poll.
    """

    def __init__(self, entrants, voting_deadline):
        self.entrants = entrants
        self.voting_deadline = voting_deadline
        self.environment = Environment(loader=FileSystemLoader("./poller/template/"))
        self.template = self.environment.get_template("template.txt")

    def render(self):
        return self.template.render(
            entrants=self.entrants, voting_deadline=self.voting_deadline
        )


if __name__ == "__main__":
    output = Output(entrants=["Person1", "Person2"], voting_deadline="1/1/2024")

    print(output.render())
