/* jQuery Plot
 *
 * Various type of Chart
/*====================================================================*/
$(function () {
   var data = [{
       label : 'Population',
       color : '#B74231',
       shadowSize : 0,
       data : [["Jan", 450],["Feb", 550],["Mar", 320],["Apr", 700],["May", 200],["Jun", 330],["Jul", 900],["Aug", 140],["Sep", 300],["Nov", 500],["Dec", 300]]
   }]
   
   $.plot($("#chart1"), data, {
       series: {
           bars: {
               show: true,
               barWidth: 0.3,
               align: "center" ,
               fill: .8
           }
       },
       grid: {
           borderWidth: 0, 
           hoverable: true 
       },
       tooltip: true,
       tooltipOpts: {
           content: "%x : %y"
       },
       xaxis: {
           mode: "categories",
           tickLength: 0
       }
   });
});

$(function () {
   var data = [
       {
           label : 'United State',
           color : '#B74231',
           data: [[1990, 18.9], [1991, 18.7], [1992, 18.4], [1993, 19.3], [1994, 19.5], [1995, 19.3], [1996, 19.4], [1997, 20.2], [1998, 19.8], [1999, 19.9], [2000, 20.4], [2001, 20.1], [2002, 20.0], [2003, 19.8], [2004, 20.4]]
       },
       {
           label : 'Belgium',
           color : '#266999',
           data: [[1990, 11.9], [1991, 14.7],[1992, 13.4], [1993, 12.2], [1994, 10.6], [1995, 10.2], [1996, 10.1], [1997, 9.7], [1998, 9.5], [1999, 9.7], [2000, 9.9], [2001, 9.9], [2002, 9.9], [2003, 10.3], [2004, 10.5]]
       }
   ]
   
   $.plot($("#chart2"), data, {
       series: {
           lines: {
               show: true,
               fill: .5
           },
           points: { show: true }
       },
       grid: {
           borderWidth: 0, 
           hoverable: true 
       },
       tooltip: true,
       tooltipOpts: {
           content: "%x : %y"
       },
       xaxis: {
           mode: "categories",
           tickLength: 0
       }
   });
});

$(function () {
   var data = [
       {
           label : 'United State',
           color : '#368B60',
           data: [[1990, 18.9], [1991, 18.7], [1992, 18.4], [1993, 19.3], [1994, 19.5], [1995, 19.3], [1996, 19.4], [1997, 20.2], [1998, 19.8], [1999, 19.9], [2000, 20.4], [2001, 20.1], [2002, 20.0], [2003, 19.8], [2004, 20.4]]
       }
   ]
   
   $.plot($("#chart3"), data, {
       series: {
           lines: { show: true, },
           points: { show: true }
       },
       grid: {
           borderWidth: 0, 
           hoverable: true 
       },
       tooltip: true,
       tooltipOpts: {
           content: "%x : %y"
       },
       xaxis: {
           mode: "categories",
           tickLength: 0
       }
   });
});

$(function () {
   var data = [
       {
           label : 'United State',
           color : '#801E7A',
           data: [[1990, Math.floor((Math.random()*20)+1)], [1991, Math.floor((Math.random()*20)+1)], [1992, Math.floor((Math.random()*20)+1)], [1993, Math.floor((Math.random()*20)+1)], [1994, Math.floor((Math.random()*20)+1)], [1995, Math.floor((Math.random()*20)+1)], [1996, Math.floor((Math.random()*20)+1)], [1997, Math.floor((Math.random()*20)+1)], [1998, Math.floor((Math.random()*20)+1)], [1999, Math.floor((Math.random()*20)+1)], [2000, Math.floor((Math.random()*20)+1)], [2001, Math.floor((Math.random()*20)+1)], [2002, Math.floor((Math.random()*20)+1)], [2003, Math.floor((Math.random()*20)+1)], [2004, Math.floor((Math.random()*20)+1)]]
       },
       {
           label : 'Belgium',
           color : '#266999',
           data: [[1990, Math.floor((Math.random()*20)+1)], [1991, Math.floor((Math.random()*20)+1)], [1992, Math.floor((Math.random()*20)+1)], [1993, Math.floor((Math.random()*20)+1)], [1994, Math.floor((Math.random()*20)+1)], [1995, Math.floor((Math.random()*20)+1)], [1996, Math.floor((Math.random()*20)+1)], [1997, Math.floor((Math.random()*20)+1)], [1998, Math.floor((Math.random()*20)+1)], [1999, Math.floor((Math.random()*20)+1)], [2000, Math.floor((Math.random()*20)+1)], [2001, Math.floor((Math.random()*20)+1)], [2002, Math.floor((Math.random()*20)+1)], [2003, Math.floor((Math.random()*20)+1)], [2004, Math.floor((Math.random()*20)+1)]]
       }
   ]
   
   $.plot($("#chart4"), data, {
       series: {
           lines: { show: true, },
           points: { show: true }
       },
       grid: {
           borderWidth: 0, 
           hoverable: true 
       },
       tooltip: true,
       tooltipOpts: {
           content: "%x : %y"
       },
       xaxis: {
           mode: "categories",
           tickLength: 0
       }
   });
});

$(function () {
   var data = [];
   var series = Math.floor(Math.random()*10)+1;
   for( var i = 0; i<series; i++) {
       data[i] = { label: "Series"+(i+1), data: Math.floor(Math.random()*100)+1 }
   }

   $.plot($("#chart5"), data, {
       series: {
           pie: { show: true }
       }
   });
});

$(function () {
   var data = [];
   var series = Math.floor(Math.random()*10)+1;
   for( var i = 0; i<series; i++) {
       data[i] = { label: "Series"+(i+1), data: Math.floor(Math.random()*100)+1 }
   }

   $.plot($("#chart6"), data, {
       series: {
           pie: { 
               innerRadius: 0.5,
               show: true
           }
       },
       grid: {
           hoverable: true,
           clickable: true
       }
   });
});

$(function () {
   var data = [], totalPoints = 100;
   function getRandomData() {
       if (data.length > 0)
           data = data.slice(1);

       // do a random walk
       while (data.length < totalPoints) {
           var prev = data.length > 0 ? data[data.length - 1] : 50;
           var y = prev + Math.random() * 10 - 5;
           if (y < 0)
               y = 0;
           if (y > 100)
               y = 100;
           data.push(y);
       }
       var res = [];
       for (var i = 0; i < data.length; ++i)
           res.push([i, data[i]])
       return res;
   }
   var updateInterval = 600;
   var options = {
       series: { 
           lines: {
               show: true,
               fill: .5
           },
           shadowSize: 0 
       },
       yaxis: { min: 0, max: 100 },
       xaxis: { show: false },
       grid: {
           borderWidth: 0, 
           hoverable: true 
       }
   };
   var plot = $.plot($("#chart7"), [ getRandomData() ], options);

   function update() {
       plot.setData([ getRandomData() ]);
       plot.draw();
       
       setTimeout(update, updateInterval);
   }	
   update();
});