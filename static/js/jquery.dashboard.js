/* jQuery Plot
 *
 * Various type of Chart
/*====================================================================*/
$(function () {
   var data = [
       {
           label : 'Visits',
           color : '#266999',
           data: [['Jan', Math.floor((Math.random()*50)+1)], ['Feb', Math.floor((Math.random()*50)+1)],['Mac', Math.floor((Math.random()*50)+1)], ['Apr', Math.floor((Math.random()*50)+1)], ['Mei', Math.floor((Math.random()*50)+1)]]
       },
	   {
           label : 'Hit',
           color : '#B74231',
           data: [['Jan', Math.floor((Math.random()*50)+1)], ['Feb', Math.floor((Math.random()*50)+1)],['Mac', Math.floor((Math.random()*50)+1)], ['Apr', Math.floor((Math.random()*50)+1)], ['Mei', Math.floor((Math.random()*50)+1)]]
       }
   ]
   
   $.plot($("#chart1"), data, {
       series: {
           lines: {
               show: true,
               fill: .7
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
           label : 'Visits',
           color : '#801E7A',
           data: [['Jan', Math.floor((Math.random()*50)+1)], ['Feb', Math.floor((Math.random()*50)+1)],['Mac', Math.floor((Math.random()*50)+1)], ['Apr', Math.floor((Math.random()*50)+1)], ['Mei', Math.floor((Math.random()*50)+1)]]
       	},
	   	{
           label : 'Hit',
           color : '#B74231',
           data: [['Jan', Math.floor((Math.random()*50)+1)], ['Feb', Math.floor((Math.random()*50)+1)],['Mac', Math.floor((Math.random()*50)+1)], ['Apr', Math.floor((Math.random()*50)+1)], ['Mei', Math.floor((Math.random()*50)+1)]]
       	}
   	]
   
   	$.plot($("#chart2"), data, {
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
    var sin = [], cos = [];
    for (var i = 0; i < 14; i += 0.5) {
        sin.push([i, Math.sin(i)]);
        cos.push([i, Math.cos(i)]);
    }

	var plot = $.plot($("#chart3"),
	[ 
	   { 
			data: sin, 
			color : '#A1345E',
			label: "sin(x)"
		}, 
		{ 
		data: cos,
		color : '#B74231',
		label: "cos(x)" 
		} 
	], 
	{
	   series: {
		   lines: { show: true },
		   points: { show: true }
	   },
	   grid: { hoverable: true, clickable: true, borderWidth: 0, },
	   yaxis: { min: -1.2, max: 1.2 },
	   tooltip: true,
       	tooltipOpts: {
           	content: "%x : %y"
       	}
	});
});

$(function () {
   	var data = [
       	{
           	label : 'Sales',
           	color : '#B74231',
           	data: [[1990, 18.9], [1991, 18.7], [1992, 18.4], [1993, 19.3], [1994, 19.5], [1995, 19.3], [1996, 19.4], [1997, 20.2], [1998, 19.8], [1999, 19.9], [2000, 20.4], [2001, 20.1], [2002, 20.0], [2003, 19.8], [2004, 20.4]]
       	},
       	{
           	label : 'Users',
           	color : '#266999',
           	data: [[1990, 11.9], [1991, 14.7],[1992, 13.4], [1993, 12.2], [1994, 10.6], [1995, 10.2], [1996, 10.1], [1997, 9.7], [1998, 9.5], [1999, 9.7], [2000, 9.9], [2001, 9.9], [2002, 9.9], [2003, 10.3], [2004, 10.5]]
       	}
   	]
   
   	$.plot($("#chart4"), data, {
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

/* Twitter Bootstrap Tooltip
 *
 * Link Tooltips
/*====================================================================*/
$(function() {
	$('[rel="tooltip"]').tooltip({
		placement : 'top'
	});
	$('#table-todo').selectRow({
		classname : 'line'
	});
});

/* Datatable
 *
 * dashboard datatable sample
/*====================================================================*/
$(function () {
	$('#table1').dataTable({
		"bProcessing": true,
		"sAjaxSource": "js/jquery.datatable.arrays.txt"
	});
});
$(function () {
	$("#spark1").sparkline([5,6,7,9,9,5,3,2,2,4,6,7], {
		type: 'line',
		type: 'line',
		width: '100',
		height: '30',
		lineWidth: 3,
		spotRadius: 3,
		lineColor: '#bf0000',
		fillColor: '#ffaaaa',
		spotColor: '#7f007f',
		minSpotColor: '#ffaaff',
		maxSpotColor: '#ff00ff',
		highlightSpotColor: '#0000ff',
		highlightLineColor: '#7f003f',
		drawNormalOnTop: true
   });
   $("#spark2").sparkline([5,6,7,-5,1,-3,-2,4,5,2,7,3,1], {
		type: 'bar',
		height: '30',
		barWidth: 7,
		barSpacing: 1,
		negBarColor: '#ff5656'
   });
});