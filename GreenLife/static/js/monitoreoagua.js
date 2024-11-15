const getOptionChart = async () => {
    try {
        const response=await fetch("http://localhost:8000/home/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex);        
    }    
};

const initChart=async () => {
  const myChart=echarts.init(document.getElementById("nivelpha"));
  let option = {
    title:{
      text: 'Nivel pH'
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['1', '2', '3', '4', '5', '6', '7']
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
        areaStyle: {}
      }
    ]
  };

window.addEventListener('resize', myChart.resize);


    // myChart.setOption(await getOptionChart());
    myChart.setOption(option);

    window.addEventListener('resize', () => {
      myChart.resize();
  });
};

const iniChart=async () => {
  const myChart=echarts.init(document.getElementById("temperaturaa"));
  let option = {
    title:{
      text: 'Temperatura'
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['1', '2', '3', '4', '5', '6', '7']
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
        areaStyle: {}
      }
    ]
  };

window.addEventListener('resize', myChart.resize);


    // myChart.setOption(await getOptionChart());
    myChart.setOption(option);

    window.addEventListener('resize', () => {
      myChart.resize();
  });
};

const inisChart=async () => {
  const myChart=echarts.init(document.getElementById("conductividad"));
  let option = {
    title:{
      text: 'Conductividad Eléctrica'
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['1', '2', '3', '4', '5', '6', '7']
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
        areaStyle: {}
      }
    ]
  };

window.addEventListener('resize', myChart.resize);


    // myChart.setOption(await getOptionChart());
    myChart.setOption(option);

    window.addEventListener('resize', () => {
      myChart.resize();
  });
};

const inidChart=async () => {
  const myChart=echarts.init(document.getElementById("nivelagua"));
  let option = {
    title:{
      text: 'Nivel del agua'
    },
    xAxis: {
      type: '',
      boundaryGap: false,
      data: []
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'pie',
        areaStyle: {}
      }
    ]
  };

window.addEventListener('resize', myChart.resize);


    // myChart.setOption(await getOptionChart());
    myChart.setOption(option);

    window.addEventListener('resize', () => {
      myChart.resize();
  });
};



window.addEventListener("load",async () => {
    await iniChart();    
    await inisChart();    
    await inidChart();    
    await initChart();    
});