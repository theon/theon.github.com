Date: 2012-10-26
Title: Old Android Recycling - GPS Tracking Unit
Tags: android, gps, hack, cyanogenmod, adw.l
Category: Posts
Author: Ian Forsey
Status: draft

I do a fair bit of walking with my girlfriend at the weekends and I like to record the routes using my phone and an app like [My Tracks](http://www.google.com/mobile/mytracks/). Unfortunately, I was finding that my current device (the [Evo 3D](http://en.wikipedia.org/wiki/HTC_Evo_3D)) wouldn't have enough battery to last the distance a lot of the time. It was fine for a run around the park, but a day long hike with GPS on constantly was just too much to ask. It must be all those CPU cores supping up all the juice... Then I had the idea to transform an old [HTC Tattoo](http://en.wikipedia.org/wiki/HTC_Tattoo) I had gathering dust in a drawer into a single purpose GPS unit. 

The first thing I did was order a gigantic battery. This [2600mAh battery](http://www.amazon.co.uk/gp/product/B004W1J0CW/ref=oh_details_o02_s00_i00) is almost 2.5 times larger than the stock 1100mAh battery which allows the Tattoo to last a whole day with GPS constantly on.

The next thing I wanted to so was tweak the device's homescreen. I wanted something simple as all I needed to do with this device was launch My Tracks to record walks, launch Google Drive to transfer exported recordings over WiFi and to have some sort of indication of the battery level. 

![homescreen](https://picasaweb.google.com/111938457571698764905/BlogImages#5802985215325381522) ![Walking round ham](https://lh5.googleusercontent.com/-XbwHTCnmEQI/UIhYT5_lP5I/AAAAAAAACm8/uB64SeimZwE/s320/ScreenShot%2520%25281%2529.png)

I already had [CyanogenMod](http://www.cyanogenmod.com) installed on the Tattoo which comes with the super flexible [ADW Launcher](https://play.google.com/store/apps/details?id=org.adw.launcher&hl=en). In the ADW.L settings I did the following:

 * **Screen Preferences > Hide Status Bar** - The device doesn't have a SIM card in it. I don't need to see the signal strength icon.
 * **Screen Preferences > Hide Icon Labels** - I only need two icons. I know what they do.
 * **UI Settings > Main Dock Style None** - I don't need a dock with the phone and messaging icons.

I also changed more general settings:

 * **Menu > Edit** - Remove all but one home screens
 * Because I'd remove the dock, I added an 'open app drawer' icon to the homescreen, using the following icon: <img src="https://lh5.googleusercontent.com/-iEcJuj82usI/UIhkmT1vRXI/AAAAAAAACnQ/ZsUPANvmjDM/s128/1926603215.jpg" width="20" height="20" />

Finally I added a couple widgets to my homescreen:

 * [Simple Battery Widget](https://play.google.com/store/apps/details?id=at.dsteiner.android.simplebatterywidget&feature=search_result#?t=W251bGwsMSwxLDEsImF0LmRzdGVpbmVyLmFuZHJvaWQuc2ltcGxlYmF0dGVyeXdpZGdldCJd) sits in the middle of the homescreen
 * [Digital Clock Widget](https://play.google.com/store/apps/details?id=com.maize.digitalClock&feature=search_result#?t=W251bGwsMSwxLDEsImNvbS5tYWl6ZS5kaWdpdGFsQ2xvY2siXQ..) as seeing the time is always useful.

And that's it. It feels good taking something that was useless and turning it into something useful.