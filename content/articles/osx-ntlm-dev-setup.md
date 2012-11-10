Date: 2012-10-31
Title: Mac OSX NTLM Proxy Setup
Tags: osx, ntlm, proxy
Category: Posts
Author: Ian Forsey
Status: draft

When you are a developer, working behind a corporate proxy can be a right pain. Especially if it requires [NTLM](http://en.wikipedia.org/wiki/NTLM) authentication. If you are lucky, your favourite tools will support NTLM authentication. If you are really unlucky they won't support proxy authentication at all. After some playing, I have a setup that works well for me. Here's what it looks like:

# NTLMAPS

[NTLMAPS](http://ntlmaps.sourceforge.net/) will to do the NTLM authentication against your corporate proxy and expose a new proxy which requires no authentication. Because you are running this proxy 