Date: 2012-09-09
Title: Automated Plant Watering with Arduino
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
    function renderTimeSeries(expression, title, container, extent) {
        var context = cubism.context()
                            .serverDelay(0)
                            .clientDelay(0)
                            .step(3e5) //5 minute
                            .size(800);
        
        var horizon = context.horizon();
        horizon.height(300);
        horizon.title(title);
        horizon.extent(extent);
        
        var cube = context.cube("http://54.247.99.12:1081");
        var metric = cube.metric(expression);
        var metrics = [
            metric
        ];
        
        d3.select(container).selectAll(".horizon")
            .data(metrics)
        .enter().append("div")
            .attr("class", "horizon")
            .call(horizon);
        
        d3.select(container).selectAll(".axis")
            .data(["top", "bottom"])
          .enter().append("div")
            .attr("class", function(d) { return d + " axis"; })
            .each(function(d) { d3.select(this).call(context.axis().ticks(12).orient(d)); });
        
        d3.select(container).append("div")
            .attr("class", "rule")
            .call(context.rule());
        
        context.on("focus", function(i) {
          d3.selectAll(".value").style("right", i == null ? null : context.size() - i + "px");
          d3.selectAll(".value").text(parseInt(metric.valueAt(parseInt(i))));
        });
    }
</script>

# Moisture

Blah blah blah

<div id="time-series1" class="time-series">
    <script type="text/javascript">
        renderTimeSeries("1023 - (sum(moisture(moisture)) / sum(moisture))", "Moisture Level", "#time-series1", [0, 1023]);
    </script>
</div>