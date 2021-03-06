function graph(source,interface,capacity) {
    Plotly.purge(graph2)
    var url = "http://127.0.0.1:8801/api/ifName?"+"ip="+interface+"&"+"host="+source
    var interface_name = $.ajax({type: "GET", url: url, async: false, dataType:'json'}).responseText;
    //console.log(url)
    var rawDataURL = "http://127.0.0.1:8801/api/graph_ifindex?"+"ip="+interface+"&"+"host="+source
    //console.log(rawDataURL)
    //// map the fields 
    var xField = 'time';
    var yField = 'bps';
    /// create selector 
    var selectorOptions = {
        buttons: [{
            step: 'minute',
            stepmode: 'backward',
            count: 30,
            label: '30m'
        }, {
            step: 'hour',
            stepmode: 'backward',
            count: 1,
            label: '1h'
        }, {
            step: 'hour',
            stepmode: 'todate',
            count: 3,
            label: '3h'
        }, {
            step: 'hour',
            stepmode: 'todate',
            count: 6,
            label: '6h'
        }, {
            step: 'all',
        }],
    };
    ////prepare the graph
    Plotly.d3.csv(rawDataURL, function(err, rawData) {
        if(err) throw err;
        var data = prepData(rawData);
        var layout = {
            showlegend: true,
            autoresize: true,
            width: 820,
            height: 360,
            title: 'Router: ' + source + ' Interface: '+ interface_name + ' Speed: ' + capacity +' Mbps',
            xaxis: {
                fixedrange: true,
                rangeselector: selectorOptions,
                rangeslider: {},
                type: 'date',
                title: 'Time',
            },
            yaxis: {
                fixedrange: true,
                autotick: true,
                autorange: true,
                tickformat: ".3s",
                title: 'bps'
            }
        };

        Plotly.newPlot('graph2', data, layout);
    });
    ////prepare the data
    function prepData(rawData) {
        var x = [];
        var y = [];

        rawData.forEach(function(datum, i) {

            x.push(new Date(datum[xField]));
            y.push(datum[yField]);
        });

        return [{
            mode: 'lines',
            connectgaps: 'false',
            fill: 'tonexty',
            line: { width: 1 , shape: 'spline' , color: 'rgb(153, 204, 255)' },
            name: interface_name,
            x: x,
            y: y
        }];

    }
}

