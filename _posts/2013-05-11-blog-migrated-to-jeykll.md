---
layout: post
date: 2013-05-11
title: Blog migrated from pelican to jeykll
tags: [jeykll, pelican, pelicangit, github, amazon-ec2]
category: Posts
author: Ian Forsey
---

Today I migrated this blog from [pelican](http://pelican.notmyidea.org) over to [jeykll](http://jekyllrb.com/).

Why I hear you ask? Well, when I started this blog I [wrote about the features](/powering-your-blog-with-pelican-and-git.html) I wanted from a blog platform and decided that a static site generator was what I was after and why I ultimately chose pelican. One of the downsides to using a static site generator like pelican is having to run the generator every time you add or update a post. This is what drove me to create [pelicangit](/powering-your-blog-with-pelican-and-git.html) which would automatically run pelican on the server-side whenever a post is pushed into the git repo it is watching. More recently my colleague [stig](http://superloopy.io/) introduced me to jeykll which does the same. I've had to use an ec2 instance to keep pelicangit running and the main bonus of migrating to jeykll is that this is no longer required; jeykll is already tightly integrated into github pages. You simply push you markdown posts to a github repo and they are auto-magically converted to a static HTML site.

The migration was a mostly manual process as there are no pelican [importers](http://jekyllrb.com/docs/migrations/), but it went pretty smoothly; luckily the syntax of the two templating systems used by pelcian and jeykll ([jinja](http://jinja.pocoo.org/) and [liquid](http://wiki.shopify.com/Liquid)) are almost identical!

I'm really happy with the result - especially the [related_pages](http://jekyllrb.com/docs/variables/) variable which pelican is missing. The only feature I was missing from pelican was the ability for jeykll to generate a page with a list of posts for each tag. For the meantime I have made a quick (and very dirty) [bash script](https://github.com/theon/theon.github.com/blob/master/gen-tag-pages.sh) to workaround this. I need to run this script every now and again when I need to add new tag pages, which is a bit of a pain, but not the end of the world.

If you see any errors or broken links, then give me a shout or send me a pull request.