from .output import Output
import os


def test_output():
    expected = """Please vote for your three favourite photos, using whatever criteria you feel is best. All Dopers are welcome to vote - you don’t need to have submitted a photo. **You cannot vote for your own photo**. You get three votes (and the poll will make you use all of them).

The voting deadline is **9pm UK time on 1/1/2024**.

[poll type=multiple results=always min=3 max=3 chartType=bar]
* Person1
* Person2
[/poll]"""

    output = Output(entrants=["Person1", "Person2"], voting_deadline="1/1/2024")
    assert output.render() == expected
