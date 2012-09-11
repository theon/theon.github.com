Date: 2012-09-09
Title: Plant Watering with Arduino
Tags: arduino, cube, cubism, nodejs
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
        
        var amount = (moistureExtent - 250) * (moistureHeight / moistureExtent);
        ctx.moveTo(0, amount);
        ctx.lineTo(800, amount);
        ctx.stroke();
    }
</script>

# Automating My Chilli Plant

Blah blah blah

<div id="moisture-time-series" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("1023 - (sum(moisture(moisture)) / sum(moisture))", "Moisture Level", "#moisture-time-series", [0, moistureExtent], 3e5, ["#31a354", "#E9967A"]);
    </script>
</div>

<div id="time-series2" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("1023 - max(moisture(moisture))", "Moisture Max", "#time-series2", [0, 1023], 3e5, ["#08519c", "#6baed6"]);
    </script>
</div>

<script type="text/javascript">
    addRules();
    setTimeout(drawWaterLine, 1000);
</script>