$(document).ready(function(){
    new ScrollBooster({
        viewport: document.querySelector('.slick-list'),
        content: document.querySelector('.slick-track'),
        scrollMode: 'transform',
        direction: 'horizontal',
        emulateScroll: true,
     });

     window.chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(75, 192, 192)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)'
      };

    var endpoint = "/visualization/weather/data/"
     var jsonData = $.ajax({
        url: endpoint,
        dataType: "json",
        async:false
     }).responseText;
     
     jsonData = JSON.parse(jsonData);

     var day_period = new Array();
     var night_temp = new Array();
     var day_temp = new Array();

     for(var i = 0, j = jsonData.length; i < j; i++){
        day_period.push(jsonData[i]["day_period"]);
        night_temp.push((parseFloat(jsonData[i]["night_temp"])));
        day_temp.push((parseFloat(jsonData[i]["day_temp"])));
     }

     var lineChartData = {
         labels: day_period,
         datasets: [{
             label: "Day",
             borderColor:  window.chartColors.red,
             backgroundColor:  window.chartColors.red,
             fill: false,
             data: day_temp,
             yAxisID: "y-axis-1",
         },{
            label: "Night",
            borderColor: window.chartColors.blue,
            backgroundColor: window.chartColors.blue,
            fill: false,
            data: night_temp,
            yAxisID: "y-axis-2"
         }]
     };

     window.onload = function(){
         var ctx = document.getElementById("chart_div").getContext("2d");
         window.myLine = new Chart(ctx, {
             type: 'line',
             data: lineChartData,
             options: {
                 responsive: true,
                 hoverMode: 'index',
                 stacked: false,
                 title: {
                     display: true,
                     text: '15-Day Weather Forecast',
                     fontSize: 15,
                     fontFamily: "'Formular', sans-serif",
                     fontStyle: 'bold'
                 },
                 scales: {
                     yAxes: [{
                         type: "linear",
                         display: true,
                         position: "left",
                         id: "y-axis-1",
                         scaleLabel:{
                             display: true,
                             labelString: 'Day Temperature'
                         }
                     },{
                         type: "linear",
                         display: true,
                         position: "right",
                         id: "y-axis-2",
                         scaleLabel: {
                             display: true,
                             labelString: 'Night Temperature'
                         },

                         gridLines: {
                             drawChartArea: false,
                         },
                     }],
                     xAxes: [{
                         scaleLabel: {
                             display: true,
                             labelString: 'Period'
                         }
                     }]
                 },
                 layout: {
                     padding:{
                         left: 30,
                         top: 0,
                         right: 30,
                         bottom: 0,
                     }
                 }
             }
         });
     }
});