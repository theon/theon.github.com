Date: 2012-04-17
Title: pelicangit 0.1 released 
Tags: pelican, git, github, pelicangit
Category: Posts
Author: Ian Forsey

In my [previous post](http://theon.github.com/powering-your-blog-with-pelican-and-git.html) I talked about my motivation for creating [pelicangit](https://github.com/theon/pelicangit). I've spent this last week polishing it up a bit and have now made v0.1 available on PyPI. If you already have pelican and pip installed on your machine, installing pelicangit is now as easy as running `sudo pip install pelicangit`.

For more details on configuring pelicangit, check out the documentation on the [github page](https://github.com/theon/pelicangit) or the [PyPI page](http://pypi.python.org/pypi?:action=display&name=pelicangit&version=0.1)

PS. This is probably the first time I've publicly distributed a command line tool and I was really impressed at how [easy it is with python](http://docs.python.org/distutils/index.html). Essentially you write a simple setup.py configuration file detailing things like which python scripts you want to be console commands (copied to /usr/local/bin), then run a single command which asks for your PyPi credentials and that's it: Your distribution is built, uploaded to PyPi and made available to the world. I wish getting Java Libaries into the public maven repository was that easy! 

This will likely make Python my go-to language if I want to make any other command line tools in the future.