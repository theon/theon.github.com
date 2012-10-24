Date: 2012-04-10
Title: Powering your Blog with Pelican and Git
Tags: pelicangit, pelican, git, github, amazon ec2, cloud9 ide 
Category: Posts
Author: Ian Forsey

When I decided to start writing this blog, I played around with blogger, wordpress and tumblr, but didn't really get along with any of them - they all seemed a bit too heavyweight for what I wanted. I didn't need much - just the ability to specify some HTML/CSS for the styling and then a quick and easy way to write and publish posts.

I stumbled across [calepin](http://calepin.co/) which seemed more along the right lines. Unfortunately it had no support for theming (HTML/CSS etc), however the system behind calepin, known as [pelican](http://pelican.notmyidea.org/), was freely available to use standalone and did give you full control over the styling of your blog. So that's what I'm using today for this blog.

Here is a diagram showing the pelican set up behind this blog:

<div class="central-section">
    <img src="http://lh4.googleusercontent.com/-KPeKZ92FhaE/T4IeoedMY_I/AAAAAAAACXE/fSpxiJ_iCwE/s876/PelicanGit.png" />
</div>

I write my posts in markdown and push them to a github repo. A git service hook then causes a pelican instance running in Amazon EC2 to convert this markdown to HTML and push it to a [github pages](http://pages.github.com/) repo for hosting. It's worth noting that github pages and Cloud9 IDE are completely free at the time of writing. EC2 have a year long free tier before charging.  

The wrapper around pelican that responds to the git service hook and manages the git repos is a python script I've unimaginatively called [pelicangit](https://github.com/theon/pelicangit) - feel free to fork it, play with it and/or provide feedback/criticism. 

So far, this set up has been nice to work with. I really like the simplicity of writing a blog post as a markdown file with a few headers and then pushing it to a git repo to publish it. Plus, the best thing about pushing pelican into the cloud is that I can write my blog posts from my Chromebook, which can't run pelican locally :)