---
layout: post
date: 2012-04-28
title: Remote Controlled Thermostat with Arduino
tags: [arduino, hack, scala, spring, jetty]
category: Posts
author: Ian Forsey
---

I was out on a walk on a cold day and thought it would be great to be able to remotely turn on the heating in time for when I got back home, which led to this; my first Arduino project. The remote control is achieved over the Internet and the form is web based, so could equally be controlled via any mobile phone with a web browser.

<div class="youtubevid">
    <iframe width="853" height="480" src="http://www.youtube.com/embed/Bxp3UJ3anjc" frameborder="0" allowfullscreen></iframe>
</div>

The project took an evening to build. I went out to some charity shops in the morning to try and find some Lego for the construction, but didn't manage to find any, so hacked it up with some picture wire I already had. A Jetty webserver sits between the Arduino and the laptop with a Scala/Spring webapp deployed. This webapp stores the target temperature posted from the laptop and serves it up to the Arduino, which polls the web server every few seconds.