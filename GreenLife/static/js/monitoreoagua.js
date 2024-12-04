document.addEventListener("DOMContentLoaded", function () {
  // Inicializar el gráfico para conductividad eléctrica (TDS)
  var graficoTDS = echarts.init(document.getElementById('grafico-tds'));

  // Obtener los datos desde Django
  fetch('/home/datos-tds/')
      .then(response => response.json())
      .then(data => {
          // Extraer los datos para el gráfico
          const nodosTDS = data.data.tds.map(item => item.nodo);
          const valoresTDS = data.data.tds.map(item => item.cnt_tds);

          // Configuración del gráfico
          var opciones = {
              title: {
                  text: 'Conductividad Eléctrica',
                  subtext: 'Mediciones de TDS',
                  left: 'center'
              },
              tooltip: {
                  trigger: 'axis'
              },
              legend: {
                  data: ['TDS'],
                  top: '15%'
              },
              xAxis: {
                  type: 'category',
                  data: nodosTDS, // Usar los nodos como etiquetas del eje X
                  name: 'Nodos'
              },
              yAxis: {
                  type: 'value',
                  name: 'TDS'
              },
              series: [
                  {
                      name: 'TDS',
                      type: 'bar',
                      data: valoresTDS,
                      color: '#5470C6'
                  }
              ]
          };

          // Establecer las opciones del gráfico
          graficoTDS.setOption(opciones);

          const estadoTextoTDS = document.getElementById('estado-tds');
          const estadosTDS = valoresTDS.map(valor => {
              if (valor >= 500 && valor <= 1500) {
                  return 'Bueno';
              } else if ((valor >= 300 && valor < 500) || (valor > 1500 && valor <= 2000)) {
                  return 'Regular';
              } else {
                  return 'Malo';
              }
          });

          // Mostrar el estado para cada nodo
          estadoTextoTDS.innerHTML = nodosTDS.map((nodo, index) => {
              return `<b>${nodo}</b>: ${estadosTDS[index]}`;
          }).join('<br>');

      })
      .catch(error => {
          console.error('Error al obtener los datos:', error);
      });
});

document.addEventListener("DOMContentLoaded", function () {
  // Inicializar el gráfico para agua
  var graficoAgua = echarts.init(document.getElementById('grafico-agua'));

  // Obtener los datos desde Django
  fetch('/home/datos-agua/')
      .then(response => response.json())
      .then(data => {
          // Extraer los datos para el gráfico
          const nodosLluvia = data.data.lluvia.map(item => item.nodo);
          const valoresLluvia = data.data.lluvia.map(item => item.cnt_lluvia);

          // Configuración del gráfico
          var opciones = {
              title: {
                  text: 'Cantidad de Lluvia',
                  subtext: 'Mediciones de agua (Lluvia)',
                  left: 'center'
              },
              tooltip: {
                  trigger: 'axis'
              },
              legend: {
                  data: ['Lluvia'],
                  top: '15%'
              },
              xAxis: {
                  type: 'category',
                  data: nodosLluvia, // Usar los nodos como etiquetas del eje X
                  name: 'Nodos'
              },
              yAxis: {
                  type: 'value',
                  name: 'Cantidad de Lluvia'
              },
              series: [
                  {
                      name: 'Lluvia',
                      type: 'bar',
                      data: valoresLluvia,
                      color: '#73C0DE'
                  }
              ]
          };

          // Establecer las opciones del gráfico
          graficoAgua.setOption(opciones);
          const estadoTextoAgua = document.getElementById('estado-agua');
          const estadosAgua = valoresLluvia.map(valor => {
              if (valor == 0) {
                  return 'No está lloviendo';
              } else if (valor != 0) {
                  return 'Está lloviendo';
              }
          });

          // Mostrar el estado para cada nodo
          estadoTextoAgua.innerHTML = nodosLluvia.map((nodo, index) => {
              return `<b>${nodo}</b>: ${estadosAgua[index]}`;
          }).join('<br>');

      })
      .catch(error => {
          console.error('Error al obtener los datos:', error);
      });
});

document.addEventListener("DOMContentLoaded", function () {
  // Inicializar el gráfico para nivel del agua
  var graficoDistancia = echarts.init(document.getElementById('grafico-distancia'));

  // Obtener los datos desde Django
  fetch('/home/datos-distancia/')
      .then(response => response.json())
      .then(data => {
          // Extraer los datos para el gráfico
          const nodosDistancia = data.data.distancia.map(item => item.nodo);
          const valoresDistancia = data.data.distancia.map(item => item.cnt_distancia);

          // Configuración del gráfico
          var opciones = {
              title: {
                  text: 'Nivel del Agua',
                  subtext: 'Mediciones de distancia del agua',
                  left: 'center'
              },
              tooltip: {
                  trigger: 'axis'
              },
              legend: {
                  data: ['Nivel de Agua'],
                  top: '15%'
              },
              xAxis: {
                  type: 'category',
                  data: nodosDistancia, // Usar los nodos como etiquetas del eje X
                  name: 'Nodos'
              },
              yAxis: {
                  type: 'value',
                  name: 'Distancia'
              },
              series: [
                  {
                      name: 'Nivel de Agua',
                      type: 'bar',
                      data: valoresDistancia,
                      color: '#37A2DA'
                  }
              ]
          };

          // Establecer las opciones del gráfico
          graficoDistancia.setOption(opciones);
          const estadoTextoDistancia = document.getElementById('estado-distancia');
          const estadosDistancia = valoresDistancia.map(valor => {
              if (valor <= 10) {
                  return 'Bueno';
              } else if (valor <= 20) {
                  return 'Regular';
              } else {
                  return 'Malo';
              }
          }); 
          // Mostrar el estado para cada nodo
          estadoTextoDistancia.innerHTML = nodosDistancia.map((nodo, index) => {
              return `<b>${nodo}</b>: ${estadosDistancia[index]}`;
          }).join('<br>');

      })
      .catch(error => {
          console.error('Error al obtener los datos:', error);
      });
});

document.addEventListener("DOMContentLoaded", function () {
  // Inicializar el gráfico para temperatura
  var graficoTemperatura = echarts.init(document.getElementById('grafico-temperatura'));

  // Obtener los datos desde Django
  fetch('/home/datos-temperatura/')
    .then(response => response.json())
    .then(data => {
      // Extraer los datos para las tres series
      const nodosTemperaturaTC = data.data.tc.map(item => item.nodo);
      const valoresTemperaturaTC = data.data.tc.map(item => item.cnt_tc);

      const nodosTemperaturaTF = data.data.tf.map(item => item.nodo);
      const valoresTemperaturaTF = data.data.tf.map(item => item.cnt_tf);

      const nodosTemperaturaTS = data.data.ts.map(item => item.nodo);
      const valoresTemperaturaTS = data.data.ts.map(item => item.cnt_ts);


      // Configuración del gráfico
      var opciones = {
          title: {
            text: 'Temperatura - TC, TF y TS',
            subtext: 'Comparación de mediciones de temperatura',
            left: 'center',
            textStyle: {
              fontSize: 18 // Ajusta el tamaño del texto principal
            },
            subtextStyle: {
              fontSize: 12 // Ajusta el tamaño del subtítulo
            }
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: ['TC', 'TF', 'TS'],
            top: '15%' // Ajusta la posición de la leyenda para que no se sobreponga con el título
          },
          xAxis: {
            type: 'category',
            data: nodosTemperaturaTC,
            name: 'Nodos'
          },
          yAxis: {
            type: 'value',
            name: 'Temperatura'
          },
          series: [
            {
              name: 'TC',
              type: 'bar',
              data: valoresTemperaturaTC,
              color: '#5470C6'
            },
            {
              name: 'TF',
              type: 'bar',
              data: valoresTemperaturaTF,
              color: '#91CC75'
            },
            {
              name: 'TS',
              type: 'bar',
              data: valoresTemperaturaTS,
              color: '#EE6666'
            }
          ]
        };
        

      // Establecer las opciones del gráfico
      graficoTemperatura.setOption(opciones);

      const estadoTextoTemperatura = document.getElementById('estado-temperatura');
      const estadosTC = valoresTemperaturaTC.map(valor => {
          if (valor >= 15 && valor <= 25) {
              return 'Bueno';
          } else if (valor > 25 && valor <= 35 || valor >= 10 && valor < 15) {
              return 'Regular';
          } else {
              return 'Malo';
          }
      });

      const estadosTF = valoresTemperaturaTF.map(valor => {
          if (valor >= 10 && valor <= 30) {
              return 'Bueno';
          } else if (valor > 30 && valor <= 40 || valor >= 5 && valor < 10) {
              return 'Regular';
          } else {
              return 'Malo';
          }
      });

      const estadosTS = valoresTemperaturaTS.map(valor => {
          if (valor >= 5 && valor <= 20) {
              return 'Bueno';
          } else if (valor > 20 && valor <= 30 || valor >= 0 && valor < 5) {
              return 'Regular';
          } else {
              return 'Malo';
          }
      });

      // Mostrar el estado para cada nodo
      estadoTextoTemperatura.innerHTML = nodosTemperaturaTC.map((nodo, index) => {
          return `<b>Temperatura °C (TC)</b>: ${estadosTC[index]}<br><b>Temperatura °F (TF)</b>: ${estadosTF[index]}<br><b>Temperatura Suelo (TS)</b>: ${estadosTS[index]}`;
      }).join('<br>');

    })
    .catch(error => {
      console.error('Error al obtener los datos:', error);
    });
});