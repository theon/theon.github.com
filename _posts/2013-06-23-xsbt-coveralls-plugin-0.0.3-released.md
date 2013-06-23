---
layout: post
date: 2013-06-23
title: xsbt-coveralls-plugin 0.0.3 Released
tags: [xsbt-coveralls-plugin, scala, sbt, code-coverage]
category: Posts
author: Ian Forsey
---

I've spent this weekend working on [xsbt-coveralls-plugin](https://github.com/theon/xsbt-coveralls-plugin) and have now released version `0.0.3`.

The updates are:

* Multi project build support! ([Issue #8](https://github.com/theon/xsbt-coveralls-plugin/issues/8))
* Bug Fix: unicode characters in source files now decoded/encoded correctly ([Issue #7](https://github.com/theon/xsbt-coveralls-plugin/issues/7), [Issue #8](https://github.com/theon/xsbt-coveralls-plugin/issues/8))
* New ways to [specify your repo token](https://github.com/theon/xsbt-coveralls-plugin#specifying-your-repo-token) ([Issue #4](https://github.com/theon/xsbt-coveralls-plugin/issues/4), [Issue #5](https://github.com/theon/xsbt-coveralls-plugin/issues/5))
* Support for [different source file encodings](https://github.com/theon/xsbt-coveralls-plugin#custom-source-file-encoding) ([Issue #6](https://github.com/theon/xsbt-coveralls-plugin/issues/6))

In the process of making these changes, I've learnt that [`TaskKey`s](http://www.scala-sbt.org/release/docs/Extending/Plugins.html#example-plugin), rather than [`Command`s](http://www.scala-sbt.org/release/docs/Extending/Plugins.html#example-command-plugin)) are usually the best way to go for SBT plugins. I found this out as a result of wanting to allow users to configure the plugin via `Setting`s in their project's `build.sbt` file. I had no idea how to acheive this, so turned to stackoverflow for help with [this question](http://stackoverflow.com/q/17038663/936869). The [answer](http://stackoverflow.com/a/17100585/936869) from [James](http://stackoverflow.com/users/406984/james) prompted me to read up on SBT `TaskKey`s (there is good documentation [here](http://www.scala-sbt.org/0.12.3/docs/Getting-Started/Basic-Def.html#task-keys) and [here](http://www.scala-sbt.org/0.12.3/docs/Getting-Started/Custom-Settings.html)). The final confirmation I needed that I should be using a `TaskKey` rather than a `Command` was [this post](https://groups.google.com/d/msg/simple-build-tool/vgxkDSgOnlc/8OPkYlikmmAJ) on the SBT mailing list, which was coincidentally posted by Heiko, who ran an Akka course I attended earlier this year.

As a result, in `0.0.3` xsbt-coveralls-plugin has been rewritten to use `TaskKey`s rather than a `Command`.

Thanks for all the feedback and bug reports - keep them coming!

### What's next for xsbt-coveralls-plugin?

 * SBT `0.13.0` support on a branch
 * Ironically, the project's own code coverage has dropped a bit, so look to get that back up.