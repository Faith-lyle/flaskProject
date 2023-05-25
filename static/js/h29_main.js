let ec_left1 = echarts.init(document.getElementById('l1'),'dark',{
    renderer: 'canvas',
    useDirtyRect: false});
let option = {
    title:{text:'H29 不良柏拉图',
    left:'43%'},
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    legend: {
        data: ['不良数量', '累计占比'],
        left:'60%',
        top:'5%'
    },
    xAxis: [
        {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisPointer: {
                type: 'shadow'
            },
            nameTextStyle:{
                fontSize:7
            },
            axisLabel:{
                interval:0
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '不良数量',
            min: 0,
            max: 100,
            interval: 10,
            axisLabel: {
                formatter: '{value}'
            }
        },
        {
            type: 'value',
            min: 0,
            max: 100,
            interval: 10,
            axisLabel: {
                formatter: '{value} %'
            }
        }
    ],
    series: [
        {
            name: '不良数量',
            type: 'bar',
            tooltip: {
                valueFormatter: function (value) {
                    return value;
                }
            },
            label:{
              show:true,
              position:'inside'
            },
            data: [
                2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
            ]
        },
        {
            name: '累计占比',
            type: 'line',
            yAxisIndex: 1,
            tooltip: {
                valueFormatter: function (value) {
                    return value + ' %';
                }
            },
            label:{
              show:true,
              position:'outside',
                formatter:'{c}%'
            },
            data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
        }
    ]
};

$.ajax({
    url: "/get_data1",
            timeout: 10000, //超时时间设置为10秒；
            success: function(data) {
                let xAxis_data = [];
                var fail_num_data = [];
                let fail_rate_data = [];
                for (let i = 0; i < data['fail_datas'].length; i++) {
                    fail_num_data.push(data['fail_datas'][i][3]);
                    fail_rate_data.push(data['fail_datas'][i][5]);
                    xAxis_data.push(data['fail_datas'][i][2]);
                }
                option['series'][0]['data'] = fail_num_data;
                option['series'][1]['data'] = fail_rate_data;
                option["xAxis"][0]['data'] = xAxis_data;
                option["yAxis"][0]["max"] = Math.max(...fail_num_data)+10;
                option["yAxis"][0]["interval"] = Math.ceil((Math.max(...fail_num_data)+10)/9);

                ec_left1.setOption(option);
                window.addEventListener('resize',ec_left1.resize)
                let frame1 = $('#iframe1');
                frame1.contents().find('body').html(data['html']);

                frame1.contents().find('td:contains("On going")').css("color","yellow");
                frame1.contents().find('td:contains("close")').css("color","lime")
            },
            error: function(xhr, type, errorThrown) {
            }
    });

// ec_left1.setOption(option);
// window.addEventListener('resize',ec_left1.resize)