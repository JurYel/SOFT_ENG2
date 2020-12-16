// Requires jquery cdn and chartsjs API
<script>
$(document).ready(function(){
        // var jsonData = $.ajax({
        //         url: "fetchMovies.php",
        //         dataType: "json",
        //         async: true
        //     }).responseText;
        //     console.log(jsonData);
        //     jsonData = JSON.parse(jsonData);
        //     jsonData.map(({title,year,ratings,metascore,votes,gross_income}) => ({title,year,ratings,metascore,votes,gross_income}));

        //     var jsonData;

        // $.ajax({
        //     url: "fetchMovies.php",
        //     method: "GET",
        //     dataType: "json",
        //     success: function(data){
        //         jsonData = data;
        //     }
        // });
        
        // jQuery.extend({
        //     getValues : function(url){
        //         var result = [];
        //         $.ajax({
        //             url: url,
        //             type: 'GET',
        //             dataType: 'json',
        //             async: true,
        //             success: function(data){
        //                 result = data;
        //             }
        //         });
        //         return result;
        //     }
        // });

        // var jsonData = $.getValues("fetchMovies.php");
        // var jsonData = null;
        // var jsonData = $.ajax({
        //     url: "fetchMovies.php",
        //     type: 'GET',
        //     dataType: "json"
        // }).done(function(data,textStatus,jqXHR){
        //     console.log("success");
        //     // jsonData = jqXHR.responseText;
        // }).fail(function(){
        //     console.log("error");
        // });
        
        /* Chartjs Working */

        // var jsonData = $.ajax({
        //     url: "fetchMovies.php",
        //     dataType: "json",
        //     async: false
        // }).responseText;

        // // console.log(JSON.parse(jsonData));

        // jsonData = JSON.parse(jsonData);
        // console.log(jsonData[0]["title"]);
        // jsonData.map(({title,year,ratings,metascore,votes,gross_income}) => ({title,year,ratings,metascore,votes,gross_income}));

        // jsonData.map(({votes,gross_income}) => ({votes,gross_income}));

        // var title = new Array();
        // var year = new Array();
        // var ratings = new Array();
        // var metascore = new Array();
        // var votes = new Array();
        // var gross_income = new Array();

        // for(var i = 0, j = jsonData.length; i < j; i++){
        //     // title.push(jsonData[i]["title"]);
        //     // year.push(jsonData[i]["year"]);
        //     // ratings.push(jsonData[i]["ratings"]);
        //     // metascore.push(jsonData[i]["metascore"]);
        //     votes.push(parseInt(jsonData[i]["votes"]));
        //     gross_income.push(parseFloat(jsonData[i]["gross_income"]));
        // }

        // console.log(votes);
        // console.log(typeof(votes[0]));
        // console.log(typeof(gross_income[0]));
        // var lineChartData = {
        // labels: votes.slice(0,15),
        // datasets: [{
        //     label: "Gross Income",
        //     borderColor: window.chartColors.red,
        //     backgroundColor: window.chartColors.red,
        //     fill: false,
        //     data: gross_income.slice(0,15),
        //     yAxisID: "y-axis-1",
        // }]
        // };
        

        /* Chartjs Display Data - Working */
        // window.onload = function(){


        // var ctx = document.getElementById("chart_div").getContext("2d");
        // window.myLine = new Chart(ctx,{
        //     type: 'line',
        //     data: lineChartData,
        //     options: {
        //             responsive: true,
        //             hoverMode: 'index',
        //             stacked: false,
        //             title: {
        //                 display: true,
        //                 text: "Gross Income Over Votes",
        //                 fontSize: 15,
        //                 fontFamily: "'Formular', sans-serif",
        //                 fontStyle: 'bold'
        //             },
        //             scales: {
        //                 yAxes: [{
        //                     type: "linear",
        //                     display: true,
        //                     id: "y-axis-1",

        //                     gridLines: {
        //                         drawChartArea: false,
        //                     },
        //                 }],
        //             }
        //         }
        //     });
        // };

            /* Chartjs End*/


              /* Bug to fix - not working */
        //    google.charts.load('current',{packages: ['corechart','bar']});
        //    google.charts.setOnLoadCallback(drawStacked);

        //    function drawStacked(){
        //         var jsonData = $.ajax({
        //             url: "fetchMovies.php",
        //             dataType: "json",
        //             async: false
        //         }).responseText;
        //         jsonData = JSON.parse(jsonData);
        //         // jsonData.map(({votes,gross_income}) => ({votes,gross_income}));
        //     // var data = google.visualization.arrayToDataTable([
        //     //         ['City', '2010 Population', '2000 Population'],
        //     //         ['New York City, NY', 8175000, 8008000],
        //     //         ['Los Angeles, CA', 3792000, 3694000],
        //     //         ['Chicago, IL', 2695000, 2896000],
        //     //         ['Houston, TX', 2099000, 1953000],
        //     //         ['Philadelphia, PA', 1526000, 1517000]
        //     //         // [
        //     //         //     {label: 'votes', id: 'votes', type: 'number'},
        //     //         //     {label: 'gross_income', id: 'gross_income', type: 'number'}
        //     //         // ],
        //     //         // [votes,gross_income]
        //     //     ]);

        //         // console.log(jsonData["votes"]);
                
        //         console.log(jsonData);
        //         var data = new google.visualization.DataTable(jsonData);
        //         // var data = new google.visualization.DataTable();
        //         // data.addColumn('number','votes');
        //         // data.addColumn('number','gross_income');
        //         // data.addRows([
        //         //     [votes,gross_income]
        //         // ]);
        //         console.log(data);

        //         var options = {
        //             'title': "Top 20 Movies",
        //             'width': 600,
        //             'height': 400,
        //             'bar': {groupWidth: "95%"},
        //             'legend': {position: "none"},
        //         };

               
        //             var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
        //             chart.draw(data,options);
                
        //    }

        // new ScrollBooster({
        //    viewport: document.querySelector('.slick-list'),
        //    content: document.querySelector('.slick-track'),
        //    scrollMode: 'transform',
        //    direction: 'horizontal',
        //    emulateScroll: true,
        // });

    //    $('autoWidth').lightSlider({
    //        autoWidth: true,
    //        loop: true,
    //        onSliderLoad: function(){
    //            $('#autoWidth').removeClass('cs-hidden');
    //        }
    //    });

    

    });
</script>