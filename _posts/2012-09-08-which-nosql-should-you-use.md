---
layout: base
date: 2012-09-08
title: Which NoSQL Database Should You Use?
tags: [nosql]
category: Posts
author: Ian Forsey
published: false
---

When you are looking at your options with regards to NoSQL solutions, there is a lot out there. I've put together this list of questions you may want to ask yourself to help you narrow down the right datastore for you. This article is going to reference some popular NoSQL databases:

 * [MongoDB](http://www.mongodb.org) ([Document Store](http://en.wikipedia.org/wiki/Document-oriented_database))
 * [Neo4J](http://www.neo4j.org) ([Graph Database](http://en.wikipedia.org/wiki/Graph_database))
 * [HBase](http://hbase.apache.org/) and [Cassandra](http://cassandra.apache.org) ([Big Data](http://en.wikipedia.org/wiki/Big_data), [Column Family](http://en.wikipedia.org/wiki/Column_family))
 * [Redis](http://redis.io) ([Key-Value Store](http://en.wikipedia.org/wiki/Key/value_store#Key.E2.80.93value_store))
 
I'll also talk a bit about Relational SQL databases, because sometimes NoSQL isn't the answer.

In part one of this three part series we will ask ourselves:

 * How structured is your data?
 * Do you need to join your data? How important are relationships?

In part two we will consider:

 * How will you query your data?
 * Do you need transactions?

Finally, in part three we will look into:

 * How do you need to scale?
 * How important is durability and consistency?

# How structured is your data? 

One question you should be asking yourself is: *What does my data structure look like?*

Unlike relational SQL databases, many NoSQL datastores do not require you to define a schema up front. These are often referred to as schema-less data stores. Schema-less data stores work well when you either find that you are storing entities with many optional fields or that you are even storing a bunch of entities that each have a completely different shape (i.e. completely different fields altogether). MongoDB, Neo4J, HBase and Cassandra all support this by allowing you to store different fields on a per entity basis.

You may even be looking to store data that have very little, or even no structure. For example you may be building a small analytics system to keep count of the number of views you get per page on your website. A key-value store such as Redis will likely work best for this example, maybe with page url as the key and a count as the value.

Despite most key-value stores only allowing you to store simple values such as integers, strings etc, Redis is a key-value store that allows you to store more complex data in the form of [hashes](http://redis.io/commands#hash). This is similar to the schema-less datastores described above, however be aware that Redis is at it's heart a key-value store so you cannot run complex queries against the fields in hashes. See [here](http://redis.io/commands#hash) for a list of commands you can run against hashes in redis.

Alternatively, if your data is highly structured and can be easily split into different types of entity which all have the same fields the majority of the time, then you data will fit well into tables and a relational SQL database is definetly worth considering.

# Do you need to join your data? How important are relationships?

If you have worked with SQL before, you will probably know about the `JOIN` keyword. It allows you to join together entites of different types which in SQL terms, reside in different tables.

NoSQL databases diverge with regards to JOIN-like functionality. Many NoSQL databases such [MongoDB](http://docs.mongodb.org/manual/applications/database-references/), Redis and [HBase](http://hbase.apache.org/book/joins.html) do not support JOINs in their query language. You can often work around this by either manually running multiple queries and joining the data together yourself or alternatively by denormalising your data so you no longer need to `JOIN`, but this all involves extra work and is something to keep in mind if you need JOIN-like functionality.

In contrast, graph databases like Neo4J are on the other end of the JOIN spectrum and are specifically designed to work well in situations where in SQL you would need to make many JOINs to traverse many relationships. [In the words](http://www.youtube.com/watch?v=2ElGO1P8v0c) of Neo4J's founder Emil Eifrem: *"when the value is within the connections between things, then a graph database rocks"*.

# How will you query your data?

The type of queries you will need to run will have a big impact on which datastores you can use. 

## Traversing the graph

Graph databases (such as Neo4J) work well for a very specific class of query which I have heard described as *finding the needle in the haystack*. These are the sort of queries you often see on Amazon product pages such as *'People who bought this also bought...'* and *'People who viewed this product ultimately end up buying...'*. These are queries that are run on a large dataset and require traversing relationships to return a much smaller subset of the orignal data. Neo4J's [Cypher Query Language](http://docs.neo4j.org/chunked/stable/cypher-query-lang.html) makes these sort of queries easy to write by using ASCII characters to almost draw out the `(nodes)` and `-[:relationships]->`. I can't express how much I love this query language. Here is an example of how you could write the query *'People who bought this product also bought'*:

    START prod=node(12345)
    MATCH (prod)<-[:bought]-(customer)-[:bought]->(alsoBoughtProd)
    RETURN alsoBoughtProd

The `START` clause identifies the node you wish to start with, in this case a product with id `12345`. The `MATCH` clause determines how we wish to traverse the graph. In this case we defines we wish to travserse two relationships; one `bought` relationship shown by the right to left arrow to `prod` and another `bought` relationship shown by the left to right arrow to another product called `alsoBoughtProd`. In the `RETURN` clause we define which nodes and relationships we wish to get back from the query; in this case just the `alsoBoughtProd` product nodes.

You could write this in SQL with joins, but graph databases are designed to efficiently run these type of queries and in my opinion the queries read really well in Cypher.

## A simple SET/GET by id

If you simply need to retrieve and store data against a given indentifier and don't need to do any querying more complex that that, then a Key-Value store is likely the best option for you. Redis is a little different from many key-value stores as has more than just the SET and GET commands ([a lot more](http://redis.io/commands)), which makes it suitable for slightly more use cases, such as [atomically incrementing values](http://redis.io/commands/incr) or as a simple [pub/sub broker](http://redis.io/commands#pubsub). Still at it's core, Redis still works best for those 'set by id, get by id' use cases. 

## Map Reduce

Map Reduce is one of the main features of the Big Data Column Family data stores HBase and Cassandra. Map Reduce allows you to process large datasets by arranging the data into groups (Map) and then reducing these groups down to small results (reduce). 

Conceptually this is somewhat similar to the SQL `GROUP BY` statement. In a `GROUP BY` statement you will usually arrange your rows of data into groups based on the given value of a column, however in Map Reduce you group you data by emitting any number of Key-Value pairs for each row of data. All the values with the same key are considered in the same group. In SQL you usually then reduce the grouped rows into a single value using aggregate functions such as `MIN`, `MAX` and `AVG`. In Map Reduce you will tend to run your own function that reduces all the emitted values for a given key in whatever way you require.

Unlike SQL GROUP BY, Map Reduce is not designed for real time queries, and instead works best for processing large datasets during batch operations. Data Analytics use cases are a prime example of where Map Reduce works well. Say you many rows of data, each detailing a user's interation with a given page, including a column with the time the user spent on the page. Finding aggregated stats such as the average time users spend on each page, or the average time each user spends on a page would be a good use case for Map Reduce. If you have a use case similar to this, checkout Hbase and Cassandra.

## MongoDB querying

Out of the different NoSQL datastores mentioned in this article, I'd say MongoDB has the most flexible query language. It's query language is built into a full blown programming language - Javascript. This gives you incredible flexibility, but also means you have to be careful to prevent are application logic bleeding into your database queries, which similarly has been a risk with SQL stored procedures for a long time. Still, if your problem requires more querying power than the simple GET/SET queries of a key value store, then MongoDB is certainly a candidate worth investigating.

# Do you need transactions?

Neo4J all about transactions
Redis

Mongodb psuedo transactions


# How do you need to scale?

<a name="scaling-for-data-size" />

## Scaling for data size

It is always worth asking the question *How big is my dataset going to get?* Megabytes? Gigabytes? Terabytes? Bigger? Most use cases will be for datasets that are small enough to fit on a single machine.

Some datastores such as Redis keep the entire dataset in memory and are therefore limit how much data you can store by how much memory you can fit in a single machine. If you want to use Redis with a larger dataset, you could look into [sharding](http://en.wikipedia.org/wiki/Shard_%28database_architecture%29) your data across several Redis servers, but until [Redis Cluster](http://redis.io/topics/cluster-spec) becomes available, there is nothing that will manage this out of the box for you. There are however many other Key-Value stores that are distibuted and can handle larger datasets that are too large for a single machine, such as [Voldemort](http://www.project-voldemort.com/).

Neo4J also doesn't currently support sharding out of the box and that is because [sharding graphs is hard](http://jim.webber.name/2011/02/on-sharding-graph-databases/). Jim Webber, Chief Scientist at Neo Technology has posted about [cache sharding](http://jim.webber.name/2011/02/scaling-neo4j-with-cache-sharding-and-neo4j-ha/) which is a pattern applied on top of Neo4J's [High Availability](http://docs.neo4j.org/chunked/stable/ha.html) feature, however unlike traditional sharding, cache sharding still requires the entire dataset to reside on each box which may be a problematic if you have a really large dataset.

MongoDB works well for smaller datasets, but can also scale out for larger datasets via it's [sharding support](http://docs.mongodb.org/manual/core/sharded-clusters/).

If your believe your dataset could grow into the Big Data realm (billions of rows) then that is where HBase and Cassandra come into their own. HBase and Cassandra were designed to be used for huge datasets; in fact the hbase documentation [makes a point](http://hbase.apache.org/book/architecture.html#arch.overview.when) of ensuring it's readers check they have enough data before looking to use it, as there is likely better options for use cases with smaller datasets.  

## Scaling for read and write performance

All the NoSQL databases we talk about in this article have the ability to horizontally scaling out reads to multiple machines when you need to increase read performance:

 * Redis has [master-slave](http://redis.io/topics/replication) replication
 * MongoDB has [replica sets](http://docs.mongodb.org/manual/core/replication/)
 * Neo4J has [High Availability](http://docs.neo4j.org/chunked/stable/ha.html)
 * Hbase and Cassandra are distributed by design, so horizontally scale for reads and writes

As mentioned [earlier](#scaling-for-data-size) in this article, MongoDB has support for sharding to scale out write performance, whereas Redis and Neo4J don't out of the box. That said, Redis and Neo4J are both incredibly fast at writing, since Redis in in-memory and Neo4J uses memory mapped files, so there is a good chance you won't need to scale for write speed - the only way to tell is to benchmark your use case. If you do need to do need to scale up write speed with Neo4J, then vertical scaling to fast [SSD](http://docs.neo4j.org/chunked/snapshot/capabilities-capacity.html#capabilities-write-speed) hard disks is an option - Neo4J really likes SSDs!

Read
Master Slave - Redis
Master Slave - MongoDB

Another way t

# How important is durability and consistency?

<a name="mongo-write-concern" />
Mongo Write Concern
Cassandra tunable consistency