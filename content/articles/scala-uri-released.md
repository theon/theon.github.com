Date: 2012-11-19
Title: scala-uri 0.1 Released
Tags: scala-uri, scala, url, uri, dsl
Category: Posts
Author: Ian Forsey

The other day I was looking for a Java or Scala library to help me parse a URL (with query string) and then build a new URL by changing the host and some of the parameters. I read a [couple](http://stackoverflow.com/questions/6521419/how-do-i-parse-a-x-www-url-encoded-string-into-a-mapstring-string-using-lift) of [posts](http://stackoverflow.com/questions/2809877/how-to-convert-map-to-url-query-string) on stackoverflow, but nothing seemed to fit the bill perfectly. I didn't want to pull in a whole web framework just to do this one simple task, and I was a bit disappointed I couldn't find a nice small Scala DSL for building URL query strings.

So I spent this weekend putting together a Scala library to fit that niche. The full details are on this [github page](https://github.com/theon/scala-uri), but here is a quick example of how you build a URL with it:

    :::scala
    val uri = "http://theon.github.com" ? ("param1" -> "1") & ("param2" -> "2")

Version 0.1 is now available in the Sonatype OSS Maven repository and should get synced to Maven Central soon. Check the [github page](https://github.com/theon/scala-uri) for more details.