Date: 2012-04-24
Title: Documenting the JSON Schema of your Rest APIs 
Tags: rest, api, iodocs, mashery, nodejs 
Category: Posts
Author: Ian Forsey

Recently at work I have been looking at how to document our Restful APIs. After a chat with a couple of developers we had defined the following requirements we wanted from our restful API documentation:
 
 * We needed to be able to document the URIs, HTTP methods, querystring parameters.
 * We wanted to be able to specify a bit of descriptive text associated with each API call.
 * A tool embedded in the docs that allowed the reader to call the live deployed API would be a plus.
 * Being able to define the schema of JSON objects returned by the APIs was a must have.

The last point regarding the JSON schema is important for us because we want to make sure our APIs are consistent by resusing JSON schema as much as possible. For example; if two APIs return say, product information, then both APIs should be using the same field names for the product objects in the returned payloads and the documentation should make this re-use easy to spot for both server-side developers who are building the APIs and the and client-side developers consuming them. 

I wasn't able to find any API documentation tools that supported the ability to define JSON schema, however [iodocs](https://github.com/mashery/iodocs) did everything else we wanted and had a shiney look and feel. So this evening I forked iodocs and after a couple hours implementing some dirty hacks, I have something that works. 

In the iodocs JSON file used to write your API documentation, I added a couple extra fields. The first is at the endpoint level and allows you to specify a list of object schemas you want to re-use across several of your APIs. It is a list of JSON objects in [JSON Schema](http://en.wikipedia.org/wiki/JSON#Schema) format. The second field is at the method level and allows you to define the schema of returned payload from individual API calls. It is also defined in [JSON Schema](http://en.wikipedia.org/wiki/JSON#Schema) format and allows you to reference the global schema when required.

The output looks pretty similar to the actual returned payloads, except with types instead of values. Types are clickable and will take you to the global schema section. 

Here is [the fork](https://github.com/theon/iodocs), an [example api documentation JSON file](https://github.com/theon/iodocs/blob/master/public/data/zoo.json) and a screenshot of the output:

![iodocs with JSON schema](https://lh6.googleusercontent.com/-w7n5eVl4rrc/T5cZiGLimeI/AAAAAAAACb0/euv371Xsy-w/s687/iodocs-json-schema.png)