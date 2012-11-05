Date: 2012-09-21
Title: Plant Watering with Arduino
Tags: arduino, hack, cube, cubism, nodejs, amazon ec2
Category: Posts
Author: Ian Forsey

<script type="text/javascript" src="http://theon.github.com/theme/posts/arduino-plant-watering/d3.v2.js"></script>
<script type="text/javascript" src="http://theon.github.com/theme/posts/arduino-plant-watering/cubism.v1.js"></script>
<style>
    @import url(http://theon.github.com/theme/posts/arduino-plant-watering/style.css);
</style>
<script type="text/javascript">
    var contexts = [];
    var moistureHeight = 300;
    var moistureExtent = 1023;


    function renderTimeSeries(expression, title, container, extent, step, colours) {
        var context = cubism.context()
                            .serverDelay(0)
                            .clientDelay(0)
                            .step(step) //3e5 5 minute
                            .size(800);
        
//            1e4 - 10-second
//            6e4 - 1-minute
//            3e5 - 5-minute
//            36e5 - 1-hour
//            864e5 - 1-day

        contexts.push(context);
        
        var horizon = context.horizon();
        horizon.height(moistureHeight);
        horizon.title(title);
        horizon.extent(extent);
        horizon.colors(colours);
        
        var cube = context.cube("http://54.247.99.12");
        var metric = cube.metric(expression);
        var metrics = [
            metric
        ];
        
        d3.select(container).selectAll(".axis")
            .data(["top", "bottom"])
          .enter().append("div")
            .attr("class", function(d) { return d + " axis"; })
            .each(function(d) { d3.select(this).call(context.axis().ticks(12).orient(d)); });
          
        d3.select(container).selectAll(".horizon")
            .data(metrics)
        .enter().insert("div", ".bottom")
            .attr("class", "horizon")
            .call(horizon);
          
        context.on("focus", function(i) {
          d3.selectAll(container + " .value").style("right", i == null ? null : context.size() - i + "px");
          
          var val = parseInt(metric.valueAt(parseInt(i)));
          if(!isNaN(val)) {
            d3.selectAll(container + " .value").text(val);
          }
        });
    }
    
    function addRules() {
        for(var i=0; i<contexts.length; i++) {
            d3.selectAll(".time-series").append("div")
                .attr("class", "rule")
                .call(contexts[i].rule());
        }
    }
    
    function drawWaterLine() {
        var canvas = document.getElementById("moisture-time-series").getElementsByTagName("canvas")[0];
        var ctx = canvas.getContext("2d");
        
        ctx.strokeStyle = "#F66";
        ctx.lineWidth = 1;
        
        var amount = (moistureExtent - 450) * (moistureHeight / moistureExtent);
        ctx.moveTo(0, amount);
        ctx.lineTo(1000, amount);
        ctx.stroke();
    }
</script>

# Automating My Chilli Plant

<div class="central-section">
    <a href="https://lh4.googleusercontent.com/-JgB0BCSNOdA/UF2OyAhWPRI/AAAAAAAACmA/Xo0KV3yP7Ow/s1280/DSC_0038.JPG">
        <img src="https://lh4.googleusercontent.com/-JgB0BCSNOdA/UF2OyAhWPRI/AAAAAAAACmA/Xo0KV3yP7Ow/s800/DSC_0038.JPG" />
    </a>
</div>

So... I've plugged my chilli plant into the internet. Every minute it will report how moist its soil is to a server on the web. Below is a live chart of that data - check it out - you can see exactly how moist my chilli plant is right this second. Wow, this is the sort of stuff the Internet was built for... probably.

The x-axis is time - one pixel per 5 minutes. The y-axis is moisture level in an arbitrary unit - the number is actually a reading of one of the arduino's analogue pins which has 10 bits of resolution, so it has the theoretical range of `0` - `1023`. Saying that if the chart ever reads `0`, then my chilli has either been long dead, or I have hi-jacked the arduino for my next project. A normal reading should be somewhere in the range of `400` - `800`.

_*Update 2012-11-05:* The Arduino Plant Watering system has been shut down for now. It did it's job, I got some tasty chillis and now I need the arduino for the next project. Here's a couple images of what the charts did looks like. They were lovely HTML canvas elements originally :)_

<!--
<div id="moisture-time-series" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("1023 - (sum(moisture(moisture)) / sum(moisture))", "Moisture", "#moisture-time-series", [0, moistureExtent], 3e5, ["#31a354", "#E9967A"]);
    </script>
</div>
-->
<div id="moisture-time-series" class="time-series">
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAyAAAAEsCAYAAAA7Ldc6AAAcFklEQVR4Xu3dzbLkOLUG0FMdzGAOEbwhA5hDBEMegXdkzM+IqCJOQ9JZ2Zlp+7O0LcvrToi47S3JS9tyfnXyVH358H8ECBAgQIAAAQIECBAoEvhSNI9pCBAgQIAAAQIECBAg8CGAaAICBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIECAAAECBAgQICCA6AECBAgQIECAAAECBMoEBJAyahMRIDCjwN/++sdvv/7dX5ylM26ueyJAgACBLgJeml1YDUqAwFUEBJCr7LT7JECAAIFWAgJIK0njECBwSQEB5JLb7qYJECBAYIeAALIDTykBAgQEED1AgAABAgS2CQgg27xcTYAAge8EPgPI5//D74FoDAIECBAgsE5AAFnn5CoCBAg8FRBANAYBAgQIENgmIIBs83I1AQIE/AREDxAgQIAAgR0CAsgOPKUECBC4/QTkU8LXsPQDAQIECBBYFhBAlo1cQYAAgZcCAojmIECAAAEC2wQEkG1eriZAgMB3AvcB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QIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBASQAE0JAQIECBAgQIAAAQKZgACSuakiQIAAAQIECBAgQCAQEEACNCUECBAgQIAAAQIECGQCAkjmpooAAQIECBAgQIAAgUBAAAnQlBAgQIAAAQIECBAgkAkIIJmbKgIECBAgQIAAAQIEAgEBJEBTQoAAAQIECBAgQIBAJiCAZG6qCBAgQIAAAQIECBAIBD4DyH8ArjJHlsLVTA8AAAAASUVORK5CYII=" />
</div>
This data is really useful. I have a tendency to over-water plants and this chart would tell me when the soil was dry enough to warrant a watering. Sometimes the soil would look really dry on the surface, but the chart would indicate a lot of moisture beneath the surface. But seeing as the the arduino now already knows how moist the soil is, the next step was to get the plant to water itself and take my over-watering habits out of the equation all together. So that's what I did. Once the moisture hits a certain threshold, the arduino waters the chilli. At the moment I am using a threshold of <s>`525`</s> <s>`425`</s> `450` which is the red line on the above chart. The below chart indicates events when the chilli has decided to water itself. 

<!--
<div id="watering-time-series" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("max(moisture(watered))", "Watering Events", "#watering-time-series", [0, 1], 3e5, ["#08519c", "#6baed6"]);
    </script>
</div>
-->
<div id="moisture-time-series" class="time-series">
    <img src="data:image/png;base64,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" />
</div>

<script type="text/javascript">
    addRules();
    setTimeout(drawWaterLine, 1000);
</script>

# The Build

So what's the hardware and software behind the charts look like?

## Hardware

For the moisture recording part of the project I didn't need to buy any special hardware. As it turns out it is incredibly straightforward, you simply drive a current through two wires poked into the soil and measure the resistance. The less water, the more resistance.

I found some galvanised picture hooks in a toolkit to use as prongs for the sensor. I just had to solder some wire to them and glue them to a small block of plastic to keep them at a consistent distance.

<div class="central-section">
    <a href="https://lh4.googleusercontent.com/-jfG1R8Uwtik/UFrDontTRuI/AAAAAAAAClk/Mr5DHIPc7bc/s1280/DSC_0030.JPG">
        <img src="https://lh4.googleusercontent.com/-jfG1R8Uwtik/UFrDontTRuI/AAAAAAAAClk/Mr5DHIPc7bc/s800/DSC_0030.JPG" />
    </a>
</div>

The diagram below shows the circuit. I tried the three different resistors I had to hand and the highest one (10kΩ) seems to work the best.

<div class="central-section">
    <img src="https://lh4.googleusercontent.com/-4ByM_14M6bw/UFeFtuf2CpI/AAAAAAAACj0/5fUmZlYOzqA/s400/moisture-circuit.png" />
</div>

For actually watering the plant I had to buy a bit more gear. I'd seen people do projects like this with mains powered water pumps, but that felt a little overkill to me. I wanted to do it with a simple valve and the power of gravity. I also wanted the valve to be powered via the arduino without having to use an external power supply. I ended up buying [this one](http://www.ebay.co.uk/itm/Pressure-Solar-Water-Heater-Dedicated-12V-Solenoid-Valve-/170860701640?pt=LH_DefaultDomain_3&hash=item27c81767c8#ht_5001wt_1190) for 4 quid. Two things to look out for if you are doing a similar project:

 * Arduinos support power adapters [between 9v and 12v](http://arduino.cc/playground/Learning/WhatAdapter), so get a solenoid valve that operates in this range.
 * Check the operating pressure of the valve. The one I bought had a range of 0.02 ~ 0.8Mpa which seemed to work fine for this gravity fed system. 

<div class="central-section">
    <a href="https://lh4.googleusercontent.com/-OhWgEsgV8Tc/UF2QLy03ggI/AAAAAAAACmk/IfLZiZKo0z0/s1280/DSC_0050.JPG">
        <img src="https://lh4.googleusercontent.com/-OhWgEsgV8Tc/UF2QLy03ggI/AAAAAAAACmk/IfLZiZKo0z0/s800/DSC_0050.JPG" />
    </a>
</div>

I had the idea of using a hiking hydration system I already had to feed the water, but bought a couple of [hose tails](http://www.ebay.co.uk/itm/220970410428#ht_500wt_923) and a [longer piece of hose](http://www.ebay.co.uk/itm/110777707434#ht_2594wt_956) to hook everything up.  

<div class="central-section">
    <a href="https://lh4.googleusercontent.com/-aj5cam38x20/UFrCzxruUrI/AAAAAAAACkU/9d3uFWUyIjc/s1280/DSC_0015.JPG">
        <img src="https://lh4.googleusercontent.com/-aj5cam38x20/UFrCzxruUrI/AAAAAAAACkU/9d3uFWUyIjc/s800/DSC_0015.JPG" />
    </a>
</div>

Below is the circuit diagram for driving the solenoid valve. My electronics knowledge is poor, however I managed to cobble this together from various research and it seems to work. The arduino's VIN pin gives you access to the the input voltage when using a mains adapter to power the arduino. I used a 12V 1500mA adapter I had in the flat. The diode in parallel with the solenoid is there as a [snubber diode](http://en.wikipedia.org/wiki/Flyback_diode).  

<div class="central-section">
    <img src="https://lh3.googleusercontent.com/-cn581J1INpY/UFeSmFHvOjI/AAAAAAAACkE/x8ZQXeEcZq0/s400/solenoid-valve.png" />
</div>

## Software

This project required very little server-side programming. I used [cube](http://square.github.com/cube/) to store the time-series moisture and watering event data, which uses node.js and mongodb under the hood. As mentioned in their docs, _Cube is designed for internal use only_ so I added a simple proxy using [node-http-proxy](https://github.com/nodejitsu/node-http-proxy) to lock down write access to the cube server - after all, I don't want anyone hacking my chilli plant! Cube exposes a RESTful API which my arduino could happily talk thanks to the [aJson](https://github.com/interactive-matter/aJson) library. All I had to do was deploy this lot onto a Amazon EC2 instance and the server-side work was done.

For the frontend visualisation I used the [cubism](http://square.github.com/cubism/) JavaScript library which seamlessly integrates with cube. The arduino and cubism code can be found in [this github repo](https://github.com/theon/auto-watering-system) - comments/questions/criticism of the code welcome.