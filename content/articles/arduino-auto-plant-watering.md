Date: 2012-09-21
Title: Plant Watering with Arduino
Tags: arduino, hack, cube, cubism, nodejs, amazon ec2
Category: Posts
Author: Ian Forsey

# Automating My Chilli Plant

<div class="central-section">
    <a href="https://lh4.googleusercontent.com/-JgB0BCSNOdA/UF2OyAhWPRI/AAAAAAAACmA/Xo0KV3yP7Ow/s1280/DSC_0038.JPG">
        <img src="https://lh4.googleusercontent.com/-JgB0BCSNOdA/UF2OyAhWPRI/AAAAAAAACmA/Xo0KV3yP7Ow/s800/DSC_0038.JPG" />
    </a>
</div>

So... I've plugged my chilli plant into the internet. Every minute it will report how moist its soil is to a server on the web. Below is a live chart of that data - check it out - you can see exactly how moist my chilli plant is right this second. Wow, this is the sort of stuff the Internet was built for... probably.

The x-axis is time - one pixel per 5 minutes. The y-axis is moisture level in an arbitrary unit - the number is actually a reading of one of the arduino's analogue pins which has 10 bits of resolution, so it has the theoretical range of `0` - `1023`. Saying that if the chart ever reads `0`, then my chilli has either been long dead, or I have hi-jacked the arduino for my next project. A normal reading should be somewhere in the range of `400` - `800`.

_*Update 2012-11-05:* The Arduino Plant Watering system has been shut down for now. It did it's job, I got some tasty chillis and now I need the arduino for the next project. Here's a couple images of what the charts to give you an idea what the did looks like. They were lovely interactive HTML5 canvas elements originally - trust me ;) Check out this [git repo](https://github.com/theon/auto-watering-system) for the code_

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
<div id="old-moisture-time-series" class="time-series">
    <script type="text/javascript">
        //renderTimeSeries("1023 - (sum(moisture(moisture)) / sum(moisture))", "Moisture", "#moisture-time-series", [0, moistureExtent], 3e5, ["#31a354", "#E9967A"]);
    </script>
</div>
<div id="moisture-time-series" class="time-series">
    <img src="data:image/png;base64,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+PnzlMjfp//88ePtx6mHmDyvwN+L738ECBDICPz45T//IIBk5MwhQIDA5gK//Mfvfv7ub7/4Frp5Hzg+AQIEogJ+BSsqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlEBASQqZjwBAgQIECBAgAABAmkBASRNZyIBAgQIECBAgAABAlGB/wOITz4U+eNrrQAAAABJRU5ErkJggg==" />
</div>
This data is really useful. I have a tendency to over-water plants and this chart would tell me when the soil was dry enough to warrant a watering. Sometimes the soil would look really dry on the surface, but the chart would indicate a lot of moisture beneath the surface. But seeing as the the arduino now already knows how moist the soil is, the next step was to get the plant to water itself and take my over-watering habits out of the equation all together. So that's what I did. Once the moisture hits a certain threshold, the arduino waters the chilli. At the moment I am using a threshold of <s>`525`</s> <s>`425`</s> `450` which is the red line on the above chart. The below chart indicates events when the chilli has decided to water itself. 

<div id="old-watering-time-series" class="time-series">
    <script type="text/javascript">
        //renderTimeSeries("max(moisture(watered))", "Watering Events", "#watering-time-series", [0, 1], 3e5, ["#08519c", "#6baed6"]);
    </script>
</div>
<div id="moisture-time-series" class="time-series">
    <img src="data:image/png;base64,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FDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk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AQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAg6Q5XSLe7PoisNRGgECJwXM5ZOxa5pARMABEmH3qEXnGyBAgECXgLnclYdqCCwLOECW0y3uzaIrDkdpBAicFDCXT8auaQIRAQdIhN2jFp1vgAABAl0C5nJXHqohsCzgAFlOt7g3i644HKURIHBSwFw+GbumCUQEHCARdo9adL4BAgQIdAmYy115qIbAsoADZDnd4t4suuJwlEaAwEkBc/lk7JomEBFwgETYPWrR+QYIECDQJWAud+WhGgLLAr93S2G04XscpAAAAABJRU5ErkJggg==" />
</div>

<script type="text/javascript">
    //addRules();
    //setTimeout(drawWaterLine, 1000);
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