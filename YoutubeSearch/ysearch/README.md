# Youtube Search sample application

## Setup

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env -p python3.6
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000` and search in search box it will show you suggestions from youtube and on submitting will show video details.


