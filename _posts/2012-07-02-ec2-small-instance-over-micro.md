---
layout: post
date: 2012-07-02
title: You May Want to Drop that EC2 Micro Instance
tags: [amazon-ec2]
category: Posts
author: Ian Forsey
permalink: /you-may-want-to-drop-that-ec2-micro-instance.html
---

A few months ago I wrote a [blog post](http://theon.github.com/amazon-ec2-gotchas.html) about gotchas when deploying applications to Amazon EC2. Despite not developing anything for EC2 at the moment, I learnt a new one today. It all started when I received a bunch of emails from Cloudkick (the monitoring system I mentioned in my previous post) stating that the API I had deployed there about a year ago was timing out. So I SSHed in to see what the deal was.

The first thing I noticed was that the terminal was a bit sluggish, so I ran `top` and on the first line saw this:

    :::console
    load average: 44.17, 35.29, 31.24
    
Ok... that's looking a little on the high side...  This was a pretty lightweight web app that had been running fine on a micro instance for about a year with a fairly low load average. Why the drastic increase in CPU usage?

At first I thought it might be caused by a traffic spike, so I checked the request logs, but they weren't looking too busy.
Next I figured it may be something dodgy in my code and that bouncing the server might help. So I stopped the app server and noticed that load average went back to near zero. I brought the server back up and load average sky rocketed again. I checked the traffic logs and realised no traffic was getting logged now and the reason was because the app server hadn't even booted up yet. It was starting painfully slowly and wasn't even ready to accept requests yet.

I ran `top` again and noticed on the third line down that CPU usage was actually only around 2%. `st` was at over 97%.

    :::console
    Cpu(s):  1.8%us,  0.5%sy,  0.0%ni, 0.0%id,  0.0%wa,  0.0%hi,  0.0%si,  97.7%st

I had no idea what `st` was, so broke out some googlefu and found a whole bunch of [useful blog posts](http://gregsramblings.com/2011/02/07/amazon-ec2-micro-instance-cpu-steal/). The `st` stands for 'steal time' and indicates the amount of CPU throttling EC2 is doing. 

To be fair to Amazon, they do document a lot of this [here](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/concepts_micro_instances.html) stating that micro instances can burst up to two EC2 compute units, but should have a usual background level that is much smaller. What they don't mention however is how the CPU throttling can kick in so suddenly and drastically after a year and instantly cripple your system. 

Our "fix" for the meantime is to upgrade to one of the small instances. These come it at over four times the price (8.5 cents per hour compared to the 2 cents per hour on the micro instances), and only have a max of one EC2 compute unit, however they seem much safer as the max CPU steal is much lower (maxing out at something like 60%) giving you a more consistent CPU performance. If you want a more reliable EC2 environment you may want to do the same.