Date: 2012-09-09
Title: Plant Watering with Arduino
Tags: arduino, cube, cubism, nodejs, ec2
Category: Posts
Author: Ian Forsey
Status: draft

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
        
        var amount = (moistureExtent - 525) * (moistureHeight / moistureExtent);
        ctx.moveTo(0, amount);
        ctx.lineTo(800, amount);
        ctx.stroke();
    }
</script>

# Automating My Chilli Plant

So yeah... I've plugged my chilli plant into the internet. Every minute it will report how moist it's soil is to a server on the web. Below is a live chart of that data - check it out, you can see right this second exactly how moist the soil for the chilli plant in my living room is.... wow, this is the sort of stuff the Internet was built for. 

The x-axis is time - one pixel per 5 minutes. The y-axis is moisture level in an arbritary unit - the number coming from a reading of one of the arduino's analogue pins which has 10 bits of resolution, so has the theoretical range is 0 - 1023. Saying that if the chart ever reads 0, then my chilli has either been long dead, or I have hi-jacked the arduino for my next project. A normal reading should be somewhere in the range of 500-800.

<div id="moisture-time-series" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("1023 - (sum(moisture(moisture)) / sum(moisture))", "Moisture", "#moisture-time-series", [0, moistureExtent], 3e5, ["#31a354", "#E9967A"]);
    </script>
</div>

Once I got the above mositure logging working, the next logical step was to get the plant to water itself when the moisture level got below a certain threshold. At the moment I am using a threshold of 525 which is the red line on the above chart. The below chart shows when the chilli has decided to water itself. 

<div id="watering-time-series" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("max(moisture(watered))", "Watering Events", "#watering-time-series", [0, 1], 3e5, ["#08519c", "#6baed6"]);
    </script>
</div>
<script type="text/javascript">
    addRules();
    setTimeout(drawWaterLine, 1000);
</script>

# The Build

## Hardware

For the moisture recording part of the project I didn't need to buy any special hardware. As it turns out it is incredibly straightforward to measure the moisture of soil, you simply drive a current through two wires poked into the soil and measure the resistance. The less water, the more resistance.

I found some galvanised picture hooks in a toolkit to use as prongs for the sensor and glued them to a small block of plastic to keep them at a consistent distance.

The diagram below shows the circuit. I tried the three different resistors I had to hand and the highest 10kΩ one seems to work the best.

![moisture sensor circuit](https://lh4.googleusercontent.com/-4ByM_14M6bw/UFeFtuf2CpI/AAAAAAAACj0/5fUmZlYOzqA/s400/moisture-circuit.png)

For actually watering the plant I had to buy a bit more gear. I'd seen people do projects like this with mains powered water pumps, but that felt like overkill. I wanted to do it with a simple valve and the power of gravity and I also wanted the valve to be powered via the arduino without having to use an external power supply. I ended up buying [this one](http://www.ebay.co.uk/itm/Pressure-Solar-Water-Heater-Dedicated-12V-Solenoid-Valve-/170860701640?pt=LH_DefaultDomain_3&hash=item27c81767c8#ht_5001wt_1190) for 4 quid. Two things to look out for if you are doing a similar project:

 * Arduino support power adapters [between 9v and 12v](http://arduino.cc/playground/Learning/WhatAdapter) so get a solenoid valve that operates in this range.
 * Check the operating pressure of the valve. The one I bought had a range of 0.02 ~ 0.8Mpa which seemed to work well for this gravity fed system. 

I had the idea of using a hydration system I already used for hiking to feed the water, but bought a couple of [hose tails](http://www.ebay.co.uk/itm/220970410428#ht_500wt_923) and a [longer piece of hose](http://www.ebay.co.uk/itm/110777707434#ht_2594wt_956) to hook everything up.  

Below is the circuit diagram for driving the solenoid valve. My electronics knowledge is pretty poor, however I managed to cobble this together from various reasearch and it seems to work. The arduino's VIN pin gives you access to the the input voltage when using a mains adapter to power the arduino. I used a 12V 1500mA adapter I had in the flat. The diode in parallel with the solenoid is there as a [snubber dioide](http://en.wikipedia.org/wiki/Flyback_diode).  

![solenoid valve circuit](https://lh3.googleusercontent.com/-cn581J1INpY/UFeSmFHvOjI/AAAAAAAACkE/x8ZQXeEcZq0/s400/solenoid-valve.png)

## Software

This project required very little server-side programming. I used [cube](http://square.github.com/cube/) to store the time-series moisture and watering event data, which uses node.js and mongodb under the hood. As mentioned in their docs, _Cube is designed for internal use only_ so I added a simple proxy using [node-http-proxy](https://github.com/nodejitsu/node-http-proxy) to lock down write access to the cube server - afterall I don't want anyone hacking my chilli plant! Cube exposes a RESTful api which my arduino could happily talk thanks to the [aJson](https://github.com/interactive-matter/aJson) library, so all I had to do was deploy this lot onto a amazon EC2 insance and it was ready to go.

For the frontend visulasation I used the [cubism](http://square.github.com/cubism/) JavaScript library wich seamlessly integrates with cube.

The arduino and cubism code can be found on [this github repo](https://github.com/theon/auto-watering-system). The arduino code has a few dependencies:

 * [aJson](https://github.com/interactive-matter/aJson)
 * [SimpleTimer](http://arduino.cc/playground/Code/SimpleTimer)