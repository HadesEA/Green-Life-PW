// Datos de ejemplo para diferentes gráficos
const chartData = {
  intensidadluminica: {
      type: 'line',
      title: 'Intensidad Lumínica',
      xAxisData: ['1', '2', '3', '4', '5', '6', '7'],
      seriesData: [{ name: 'Lumínica', data: [820, 932, 901, 934, 1290, 1330, 1320] }]
  },
  humedadsuelo: {
      type: 'bar',
      title: 'Humedad del Suelo y Ambiente',
      xAxisData: ['1', '2', '3', '4', '5', '6', '7'],
      seriesData: [
          { name: 'Suelo', data: [5, 10, 15, 20, 25, 30, 35] },
          { name: 'Ambiente', data: [6, 11, 16, 21, 26, 31, 36] }
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
  },
  temperatura: {
      type: 'bar',
      title: 'Temperatura del Suelo y Ambiente',
      xAxisData: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
      seriesData: [
          { name: 'Suelo', data: [16, 17, 15, 16, 16, 15, 16, 17, 16] },
          { name: 'Ambiente', data: [20, 19, 18, 20, 21, 21, 20, 21, 20] }
      ]
  }
};

// Función para obtener la opción del gráfico basada en el tipo
function getChartOption(chartId) {
  const chartConfig = chartData[chartId];
  let option = {
      title: { text: chartConfig.title },
      legend: {
          data: chartConfig.seriesData.map(series => series.name), // Agrega la leyenda con los nombres de las series
          top: '10%' // Puedes ajustar la posición de la leyenda según tus preferencias
      }
  };

  switch (chartConfig.type) {
      case 'line':
          option = {
              ...option,
              xAxis: { type: 'category', data: chartConfig.xAxisData },
              yAxis: { type: 'value' },
              series: chartConfig.seriesData.map(series => ({
                  name: series.name,
                  data: series.data,
                  type: 'line',
                  areaStyle: {}
              }))
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
                  type: 'bar'
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
                  type: 'scatter'
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
