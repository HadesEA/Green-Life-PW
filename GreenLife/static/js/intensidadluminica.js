
const getOptionChart = async () => {
    try {
        const response=await fetch("http://localhost:8000/home/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex);        
    }    
};

const initChart=async () => {
  const myChart=echarts.init(document.getElementById("intensidadluminica"));
  let option = {
    title:{
      text: 'Intensidad lumínica'
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



window.addEventListener("load",async () => {
    await initChart();    
});