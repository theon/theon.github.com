Date: 2012-09-08
Title: Which NoSQL Database Should You Use?
Tags: nosql
Category: Posts
Author: Ian Forsey
Status: draft

When you are looking at your options with regards to NoSQL solutions, there is a lot out there. I've put together this list of questions you may want to ask yourself to help you narrow down the right database for you. This article is going to talk about some of the most popular NoSQL databases:

 * MongoDB (Document Store)
 * Neo4J (Graph DB)
 * Hbase and Cassandra (Column Family)
 * Redis (Key-Value Store)
 * I'll also talk about MySQL, because sometimes NoSQL isn't the answer.

# How structured is your data? 

The first question you should be asking yourself is: What does my data structure look like?

Most NoSQL databases work well when find that you are storing a collection of entities with many optional fields or even storing a collection of entities that each have completely different fields.

# Do you need join data? How important are relationships?

If you have worked with SQL before, you will probably know about `JOIN`s

# How much do you need to scale?

## How big is your dataset going to get? Gigabytes? Hundreds of Gigabytes? Terrabytes?

## What is your query profile?

 