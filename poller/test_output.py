from .output import Output
import os


def test_output():
    # output = Output(entrants=["Person1, Person2"], voting_deadline="1/1/2023")
    with open("log.txt", "w") as fout:
        fout.write(f"{os.getcwd()}")

    with open("/poller/template.txt"):
        pass

    with open("/Users/bob/template.txt"):
        pass
