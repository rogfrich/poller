"""
Create a formatted text output that can be easily pasted into a Discourse post to create a poll.
"""
from jinja2 import Environment, FunctionLoader


def template(template):
    return """Please vote for your three favourite photos, using whatever criteria you feel is best. All Dopers are welcome to vote - you don’t need to have submitted a photo. **You cannot vote for your own photo**. You get three votes (and the poll will make you use all of them).

The voting deadline is **9pm UK time on {{voting_deadline}}**.

[poll type=multiple results=always min=3 max=3 chartType=bar]
{% for entrant in entrants -%}
* {{entrant}}
{% endfor -%}
[/poll]"""


class Output:
    """
    Creates formatted text that can be copy-pasted directly into Discourse with no further formatting to create a voting poll.
    """

    def __init__(self, entrants, voting_deadline):
        self.entrants = entrants
        self.voting_deadline = voting_deadline
        self.environment = Environment(loader=FunctionLoader(template))
        self.template = self.environment.get_template("template")

    #
    def render(self):
        return self.template.render(
            entrants=self.entrants, voting_deadline=self.voting_deadline
        )


if __name__ == "__main__":
    output = Output(entrants=["Person1", "Person2"], voting_deadline="1/1/2024")

    print(output.render())
