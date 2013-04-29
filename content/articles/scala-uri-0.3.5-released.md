Date: 2013-04-29
Title: scala-uri 0.3.5 Released
Tags: scala-uri, scala, url, uri, dsl
Category: Posts
Author: Ian Forsey


[Last time](http://theon.github.io/scala-uri-02-released.html) I blogged about [`scala-uri`](https://github.com/theon/scala-uri) was in January when `0.2` was released. Since then a whole bunch of changes have been made and `scala-uri` is now at version `0.3.5`. Here's the highlights of the changes that have been happening:

  * The Parser has been completely reimplemented in [`parboiled`](https://github.com/sirthias/parboiled/wiki). Why did I do this? Mainly because the core scala Parser Combinators have a couple of issues highlighted in [SI-4929](https://issues.scala-lang.org/browse/SI-4929). a) They are not thread-safe, so I was having to instatiate a new instance for each parse and b) There is a memory leak that requires a hacky workaround. The implementation with parboiled solved both of these problems and also fixed some bugs in the process, such as [failing to parse query string params with empty values](https://github.com/theon/scala-uri/issues/15)
  * Support for [protocol relative urls](https://github.com/theon/scala-uri#protocol-relative-urls) has been added
  * Code coverage repoting on [coveralls](https://coveralls.io/r/theon/scala-uri). To acheive this I spawned a new project [`xsbt-coveralls-plugin`](https://github.com/theon/xsbt-coveralls-plugin). Thanks to the lack of boilerplate code in scala, the test coverage is way higher than any Java project I've worked on (currently 97%)
  * Several other bug fixes. Thanks to everyone who raised bugs.

# What's next?

The next thing I would like to work on in `scala-uri` is a `PercentDecoder`. `scala-uri` currently percent encodes reserved characters when rendering URLs however doesn't decode percent encoded characters when parsing URLs. As [raised](https://github.com/theon/scala-uri/issues/12) by `hgiddens` this makes the parser and `toString` a bit wonky. Expect this soon!

My other main goal is to tackle parsing performance. I've set up a [github repo](https://github.com/theon/scala-uri-benchmarks) with some micro benchamrks of `scala-uri`. Large hostnames, paths and query string params fair pretty poorly in the benchmarks and despite most people working with small URLs, I think it is still worth looking to improve this so I'm going to break out VisualVM and see if there are some quick wins.