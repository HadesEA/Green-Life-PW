
// const getOptionChart = async () => {
//     try {
//         const response=await fetch("http://localhost:8000/home/get_chart/");
//         return await response.json();
//     } catch (ex) {
//         alert(ex);        
//     }    
// };

// const initChart=async () => {
//   const myChart=echarts.init(document.getElementById("humedadsuelo"));
//   let option = {
//     title:{
//       text: 'Humedad'
//     },
//     xAxis: {
//       type: 'category',
//       boundaryGap: false,
//       data: ['1', '2', '3', '4', '5', '6', '7']
//     },
//     yAxis: {
//       type: 'value'
//     },
//     series: [
//       {
//         data: [820, 932, 901, 934, 1290, 1330, 1320],
//         type: 'line',
//         areaStyle: {}
//       }
//     ]
//   };

// window.addEventListener('resize', myChart.resize);


//     // myChart.setOption(await getOptionChart());
//     myChart.setOption(option);

//     window.addEventListener('resize', () => {
//       myChart.resize();
//   });
// };



// window.addEventListener("load",async () => {
//     await initChart();    
// });


// const initChart = async (elementId, titleText) => {
//     const myChart = echarts.init(document.getElementById(elementId));
//     let option = {
//       title: {
//         text: titleText
//       },
//       xAxis: {
//         type: 'category',
//         boundaryGap: false,
//         data: ['1', '2', '3', '4', '5', '6', '7']
//       },
//       yAxis: {
//         type: 'value'
//       },
//       series: [
//         {
//           data: [820, 932, 901, 934, 1290, 1330, 1320],
//           type: 'line',
//           areaStyle: {}
//         }
//       ]
//     };
  
//     myChart.setOption(option);
//     window.addEventListener('resize', () => myChart.resize());
//   };
  
//   window.addEventListener("load", () => {
//     initChart("intensidadluminica", "Intensidad lumínica");
//     initChart("humedadsuelo", "Humedad");
//   });
  


// Datos de ejemplo para diferentes gráficos
const chartData = {
    intensidadluminica: {
      type: 'line',
      title: 'Intensidad Lumínica',
      xAxisData: ['1', '2', '3', '4', '5', '6', '7'],
      seriesData: [820, 932, 901, 934, 1290, 1330, 1320]
    },
    humedadsuelo: {
      type: 'bar',
      title: 'Humedad del Suelo',
      xAxisData: ['1', '2', '3', '4', '5', '6', '7'],
      seriesData: [
        { name: 'Suelo', data: [5, 10, 15, 20, 25, 30, 35] },
        { name: 'Ambiente', data:[6, 11, 16, 21, 26, 31, 36] }
    ]
    },
    concentraciongases: {
      type: 'scatter',
      title: 'Concentración de gases',
      xAxisData: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
      seriesData: [
        { name: 'Temperatura', data: [5, 20, 36, 10, 10, 20, 25] },
        { name: 'Humedad', data: [15, 25, 30, 20, 35, 40, 30] }
      ]
    }
  };
  
  
  // Función para obtener la opción del gráfico basada en el tipo
  function getChartOption(chartId) {
    const chartConfig = chartData[chartId];
    let option = { title: { text: chartConfig.title } };
    
    switch (chartConfig.type) {
        case 'line':
            option = {
              ...option,
              xAxis: { type: 'category', data: chartConfig.xAxisData },
              yAxis: { type: 'value' },
              series: Array.isArray(chartConfig.seriesData[0])
                ? chartConfig.seriesData.map(series => ({
                    name: series.name,
                    data: series.data,
                    type: 'line',
                    areaStyle: {}
                  }))
                : [{ data: chartConfig.seriesData, type: 'line', areaStyle: {} }]
            };
            break;
      
        case 'bar':
            option = {
                ...option,
                xAxis: { type: 'category', data: chartConfig.xAxisData },
                yAxis: { type: 'value' },
                series: chartConfig.seriesData.map(series => ({
                  name: series.name,
                  data: series.data,
                  type: 'bar',
                  areaStyle: {}
                }))
            };
            break;
        
        case 'scatter':
            option = {
              ...option,
              xAxis: { type: 'category', data: chartConfig.xAxisData },
                yAxis: { type: 'value' },
                series: chartConfig.seriesData.map(series => ({
                  name: series.name,
                  data: series.data,
                  type: 'scatter',
                  areaStyle: {}
                }))
            };
            break;
    }
  
    return option;
  }
  
  
  // Inicialización de gráficos según sus IDs
  function initCharts() {
    Object.keys(chartData).forEach(chartId => {
      const chartDom = document.getElementById(chartId);
      if (chartDom) {
        const myChart = echarts.init(chartDom);
        const option = getChartOption(chartId);
        myChart.setOption(option);
        window.addEventListener('resize', myChart.resize);
      }
    });
  }
  
  // Llama a la función al cargar la página
  window.addEventListener('load', initCharts);
  