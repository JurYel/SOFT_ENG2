$(document).ready(function(){
    new ScrollBooster({
        viewport: document.querySelector('.slick-list'),
        content: document.querySelector('.slick-track'),
        scrollMode: 'transform',
        direction: 'horizontal',
        emulateScroll: true,
     });

     window.onload = function(e){
        //  toggle();
     }

     function toggle(){
        var blur = document.getElementById('blur');
        blur.classList.toggle('active');

        var buffer = document.getElementById('buffer');
        buffer.classList.toggle('active');
    }

    window.chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(75, 192, 192)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)'
    }

    var lazada_endpoint = "/visualization/ecommerce/lazada/data/"
    var shopee_endpoint = "/visualization/ecommerce/shopee/data/"

    var lazadaData = $.ajax({
        url: lazada_endpoint,
        dataType: "json",
        async: false
    }).responseText;

    lazadaData = JSON.parse(lazadaData);

    var shopeeData = $.ajax({
        url: shopee_endpoint,
        dataType: "json",
        async: false
    }).responseText;

    shopeeData = JSON.parse(shopeeData);

    // console.log(shopeeData);
    // console.log(lazadaData);

    var prod_id = new Array();
    var lazadaPrices = new Array();
    var shopeePrices = new Array();

    for(var i = 0, j = lazadaData.length; i < j; i++){
        prod_id.push(lazadaData[i]["id"]);
        lazadaPrices.push(Math.log(parseFloat(lazadaData[i]["price"])));
        shopeePrices.push(Math.log(parseFloat(shopeeData[i]["price"])));
    }

    console.log(prod_id);
    console.log(lazadaPrices);
    console.log(shopeePrices);

    var lineChartData = {
        labels: prod_id,
        datasets: [{
            label: "Lazada",
            borderColor: window.chartColors.green,
            backgroundColor: window.chartColors.green,
            fill: false,
            data: lazadaPrices,
            yAxisID: "y-axis-1"
        },{
            label: "Shopee",
            borderColor: window.chartColors.orange,
            backgroundColor: window.chartColors.orange,
            fill: false,
            data: shopeePrices,
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
                    text: 'Lazada vs Shopee',
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
                        scaleLabel: {
                            display: true,
                            labelString: 'Lazada Prices'
                        }
                    }, {
                        type: "linear",
                        display: true,
                        position: "right",
                        id: "y-axis-2",
                        scaleLabel: {
                            display: true,
                            labelString: 'Shopee Prices'
                        },

                        gridLines: {
                            drawChartArea: false,
                        },
                    }],
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'Products'
                        }
                    }]
                },
                layout: {
                    padding: {
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