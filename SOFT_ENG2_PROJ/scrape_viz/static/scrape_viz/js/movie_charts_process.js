$(document).ready(function(){
    var endpoint = "/visualization/movies/data/"
    var jsonData = $.ajax({
        url: endpoint,
        dataType: "json",
        async: false
    }).responseText;
    
    jsonData = JSON.parse(jsonData);
    

    function getValues(obj,key){
        var objects = [];
        for(var i in obj){
            if(!obj.hasOwnProperty(i)) continue;
            if(typeof(obj[i]) == 'object'){
                objects = objects.concat(getValues(obj[i],key));
            }
            else if (i == key){
                objects.push(obj[i]);
            }
        }
        return objects;
    }
    
   
    google.charts.load('current',{packages: ['scatter']});
    google.charts.setOnLoadCallback(drawChart);
    
    function drawChart(){
        var chart_div = document.getElementById('chart_div');
    
        var myTicks = new Array();
        var data = new google.visualization.DataTable();
        
        
        
        data.addColumn('number','Votes');
        data.addColumn('number', 'Gross Income');
        
    
        var votes_data = getValues(jsonData,'votes');
        var gross_income_data = getValues(jsonData,'gross_income');
        var movie_title = getValues(jsonData, 'title');
    
        var formatter = new google.visualization.NumberFormat({
            fractionDigits: 2
        });
    
        for(var i=0;i<gross_income_data.length;i++){
            income = Math.log(parseFloat($.trim(gross_income_data[i])));
            votes = Math.log(parseInt($.trim(votes_data[i])));
            data.addRow([votes,income]);
        }
    
        var materialOptions = {
            chart: {
                title: 'Correlation of Gross Income and Votes'
            },
            width: 800,
            height: 500,
            series: {
                0: {axis: 'gross income'}
                
            },
            axes: {
                y: {
                    'gross income': {label: 'Gross Income'}
                },
            }
        };
    
        var options = {
            title: "Correlation of Gross Income and Votes",
            width: 800,
            height: 500,
            hAxis: {title: 'Votes', format: 'short'},
            vAxis: {title: 'Gross Income', format: 'short'},
            legend: {position: 'top'},
            crosshair:{
                color: '#000',
                trigger: 'selection'
            },
            series: {
                0: {axis: 'gross income'}
            },
            axes: {
                y: {
                    'gross income': {label: 'Gross Income'}
                }
            }
        };

        var materialChart = new google.charts.Scatter(chart_div);
        materialChart.draw(data, google.charts.Scatter.convertOptions(materialOptions));
    }
    
    new ScrollBooster({
        viewport: document.querySelector('.slick-list'),
        content: document.querySelector('.slick-track'),
        scrollMode: 'transform',
        direction: 'horizontal',
        emulateScroll: true,
     });
});

