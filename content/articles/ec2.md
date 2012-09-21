Date: 2012-04-01
Title: Amazon EC2 Gotchas
Tags: amazon ec2, cloudkick
Category: Posts
Author: Ian Forsey

Amazon EC2 is pretty awesome. In under a minute you can fire up a server in the cloud and SSH in. The SSH access combined with the fact you can run your choice of OS, makes it much more flexible than other cloud platforms as a service, such as Heroku, Google App Engine and Cloud Foundry. The down side is that there is a lot more configuration to do, so it is probably going to take a little longer to deploy your app, than it would with Heroku.

I've used EC2 to deploy some small public facing projects and have compiled this list of lessons I've learnt along the way.

*Disclaimer:* The projects I have deployed to EC2 have been small (single instance) proof of concepts and demos, and this post is aimed at people in a similar situation. I haven't used EC2 in anger for production quality software, so am only covering some basics here.

# Enable Termination Protection

These points aren't in any particular order, but if there is one thing to take away from the post, this is it: Turn on Termination Protection for your EC2 instances!

So once you have your EC2 instance up and running, there are two states you can change it to:

*  Stopped
*  Terminated

Stopping an instance is kind of like the equivalent of shutting down a physical machine; you can get your instance back up and running later. Terminating an instance is kind of like the equivalent of picking up a physical machine and throwing it out the window; you're not going to be able to get it back up and running later.

Unfortunately it is really easy to terminate an instance - right click on it and select 'Terminate'. That's it. No dialog asking you to confirm. No undo button. That instance is dead. This happened to me when I was looking to terminate a certain instance, but didn't realise that I also had another instance selected that was being used in production. When I clicked terminate, they both got killed - and believe me that's not fun!

If you do accidentally terminate a instance, then don't panic. Despite the instance getting killed, the hard drive attached to it remains available so you can launch a new instance to replace it:

*  Click the ![Launch Instance](https://images-na.ssl-images-amazon.com/images/G/01/webservices/console/ec2/icon_launchinstances.png) Launch Instance Button and go through the wizard choosing the same settings as per your terminated instance (same keypair for SSH access etc). You can use any AMI to launch from, it doesn't matter, because we will be deleting this instances Hard Drive, OS, etc.
*  Immediately Stop the new instance
*  Click on the Volumes from the left hand menu. You should see a new Hard Drive attached to the instance we just launched, as well as the hard drive from the instance we accidentally terminated (it will be unattached).
*  Unattach the Volume from the new instance (you can also delete it as we no longer need it), and attach the other Volume. It will ask for the device name, which may vary depending on your set up. For a default Amazon Linux instance it is /dev/sda1.
*  Start the instance and all should be good! If you were using an elastic IP, you will need to reattach it and if you are monitoring with Cloudkick (see below) you may need to update your setting in the Cloudkick dashboard.

If you make enabling Termination Protection the first thing you do, then hopefully you will never need follow those instructions. Why it isn't enabled by default I don't know!

# Release Unused Elastic IPs

Elastic IPs allow you to assign a static IP to your instances and they are free. That is they are free, but only provided you are using them. As soon as your Elastic IPs are not assigned to any instances, they will start coming up in your monthly bill. This is a measure from Amazon to stop people hording IPs, since they are in such short supply at the moment.

So if you un-assign one of your Elastic IPs and no longer plan to use it, then release it back into the pool. However, note that this means you will no longer be able to get that specific IP back.

# Monitor with CloudKick

[Cloudkick](https://www.cloudkick.com/) is an awesome way to monitor the health of your EC2 instances and applications deployed to them. It is also free, so check it out!

At the time of writing Cloudkick is transitioning to Rackspace Cloud Monitoring with Cloudkick disappearing in a year or two, so watch out for that.

# Name your instances

In fact name everything you can; Instances, Volumes, Snapshots, AMIs. Naming instances and the such is optional, but if you don't then it becomes some what more difficult picking the right Volume from a drop down list that contains vol-bc5e8dd4, vol-aca11cd and vol-a7fe7de.

To name things:

*  Click the Tags tab
*  Click the ![Add/Edit Tags](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/ec2/tags_icon.png) Add/Edit Tags button
*  There should already be a key prepopulated with 'Name'. Just fill in the value. 
