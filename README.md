# poller

This is a package to automate the creation of a poll from a Discourse thread. It has a very specific use case: it goes 
through a thread and compiles a list of each poster, and then creates a poll with one entry per poster. 

For example, if a thread has posts from Poster1, Poster2 and Poster3, it will create a poll with the entries:

```
<intro blurb>
[poll <options>]
* Poster1
* Poster2
* Poster3
[/poll]
```

At the moment, the options for the poll, and indeed the template for the output are hardcoded due to the specific nature
of the use-case. 

## Usage

Poller lives in my local repository of useful packages: `~/code/my_packages`;  pip install it as usual into the 
venv where I want to use it. 

```python
from poller import Manager

# thread_id is the ID of the Discourse_thread. It can be found in the thread URL. 
# submission_deadline is used in the rendered template.
m = Manager(thread_id: str, submission_deadline: str)

# Wait a moment while poller fetches and parses the thread
print(m.output) # this is the rendered template containing the text that can be copied and pasted into Discourse
```


