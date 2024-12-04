document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el gráfico para humedad
    var graficoHumedad = echarts.init(document.getElementById('grafico-humedad'));
  
    // Obtener los datos desde Django
    fetch('/home/datos-humedad/')
      .then(response => response.json())
      .then(data => {
        // Extraer los datos para ambas series
        const nodosCounter = data.data.counter.map(item => item.nodo);
        const valoresCounter = data.data.counter.map(item => item.cnt);
  
        const nodosCounterHT = data.data.counter_ht.map(item => item.nodo);
        const valoresCounterHT = data.data.counter_ht.map(item => item.cnt_ht);
  
        // Configuración del gráfico
        var opciones = {
          title: {
            text: 'Humedad ambiente y suelo',
            subtext: 'Comparación entre dos fuentes',
            left: 'center'
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: ['Counter', 'CounterHT'],
            top: '15%'
          },
          xAxis: {
            type: 'category',
            data: nodosCounter, // Usar los nodos de Counter como etiquetas del eje X
            name: 'Nodos'
          },
          yAxis: {
            type: 'value',
            name: 'Valores'
          },
          series: [
            {
              name: 'Counter',
              type: 'bar',
              data: valoresCounter,
              color: '#5470C6'
            },
            {
              name: 'CounterHT',
              type: 'bar',
              data: valoresCounterHT,
              color: '#91CC75'
            }
          ]
        };
  
        // Establecer las opciones del gráfico
        graficoHumedad.setOption(opciones);
        const estadoTextoHumedad = document.getElementById('estado-humedad');
        const estadosCounter = valoresCounter.map(valor => {
            if (valor >= 70) {
                return 'Bueno';
            } else if (valor >= 40) {
                return 'Regular';
            } else {
                return 'Malo';
            }
        });

        const estadosCounterHT = valoresCounterHT.map(valor => {
            if (valor >= 70) {
                return 'Bueno';
            } else if (valor >= 40) {
                return 'Regular';
            } else {
                return 'Malo';
            }
        });

        // Mostrar el estado para ambos nodos
        estadoTextoHumedad.innerHTML = nodosCounter.map((nodo, index) => {
            return `<b>${nodo} (Humedad Ambiente)</b>: ${estadosCounter[index]}<br><b>${nodosCounterHT[index]} (Humedad del Suelo)</b>: ${estadosCounterHT[index]}`;
        }).join('<br>');

      })
      .catch(error => {
        console.error('Error al obtener los datos:', error);
      });
  });
  

  document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el gráfico para MQ7 y MQ8
    var graficoGas = echarts.init(document.getElementById('grafico-gas'));
  
    // Obtener los datos desde Django
    fetch('/home/datos-gas/')
      .then(response => response.json())
      .then(data => {
        // Extraer los datos para ambas series
        const nodosMQ7 = data.data.mq7.map(item => item.nodo);
        const valoresMQ7 = data.data.mq7.map(item => item.cnt_mq7);
  
        const nodosMQ8 = data.data.mq8.map(item => item.nodo);
        const valoresMQ8 = data.data.mq8.map(item => item.cnt_mq8);
  
        // Configuración del gráfico
        var opciones = {
          title: {
            text: 'Concentración de Gases MQ7 y MQ8',
            subtext: 'Comparación de sensores',
            left: 'center'
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: ['MQ7', 'MQ8'],
            top: '15%'
          },
          xAxis: {
            type: 'category',
            data: nodosMQ7, // Usar nodos de MQ7 como etiquetas del eje X
            name: 'Nodos'
          },
          yAxis: {
            type: 'value',
            name: 'Concentración'
          },
          series: [
            {
              name: 'MQ7',
              type: 'bar',
              data: valoresMQ7, // Valores de MQ7
              color: '#5470C6'
            },
            {
              name: 'MQ8',
              type: 'bar',
              data: valoresMQ8, // Valores de MQ8
              color: '#91CC75'
            }
          ]
        };
  
        // Establecer las opciones del gráfico
        graficoGas.setOption(opciones);
        const estadoTextoGas = document.getElementById('estado-gas');
        const estadosMQ7 = valoresMQ7.map(valor => {
            if (valor < 500) {
                return 'Bueno';
            } else if (valor < 1000) {
                return 'Regular';
            } else {
                return 'Malo';
            }
        });

        const estadosMQ8 = valoresMQ8.map(valor => {
            if (valor < 400) {
                return 'Bueno';
            } else if (valor < 800) {
                return 'Regular';
            } else {
                return 'Malo';
            }
        });

        // Mostrar el estado para ambos nodos
        estadoTextoGas.innerHTML = nodosMQ7.map((nodo, index) => {
            return `<b>${nodo} (MQ7)</b>: ${estadosMQ7[index]}<br><b>${nodosMQ8[index]} (MQ8)</b>: ${estadosMQ8[index]}`;
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
  
  document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el gráfico para intensidad lumínica
    var graficoLux = echarts.init(document.getElementById('grafico-lux'));

    // Obtener los datos desde Django
    fetch('/home/datos-lux/')
        .then(response => response.json())
        .then(data => {
            // Extraer los datos para el gráfico
            const nodosLUX = data.data.lux.map(item => item.nodo);
            const valoresLUX = data.data.lux.map(item => item.cnt_lux);

            // Configuración del gráfico
            var opciones = {
                title: {
                    text: 'Intensidad Lumínica',
                    subtext: 'Mediciones de intensidad de luz',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['Intensidad'],
                    top: '15%'
                },
                xAxis: {
                    type: 'category',
                    data: nodosLUX, // Usar los nodos como etiquetas del eje X
                    name: 'Nodos'
                },
                yAxis: {
                    type: 'value',
                    name: 'Intensidad'
                },
                series: [
                    {
                        name: 'Intensidad',
                        type: 'bar',
                        data: valoresLUX,
                        color: '#EE6666'
                    }
                ]
            };

            // Establecer las opciones del gráfico
            graficoLux.setOption(opciones);

            const estadoTexto = document.getElementById('estado-lux');
            const estados = valoresLUX.map(valor => {
                if (valor >= 60000) {
                    return 'Bueno';
                } else if (valor >= 30000) {
                    return 'Regular';
                } else {
                    return 'Malo';
                }
            });

            // Mostrar el estado para cada nodo
            estadoTexto.innerHTML = nodosLUX.map((nodo, index) => {
                return `<b>Intensidad lumínica</b>: ${estados[index]}`;
            }).join('<br>');
        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
});


document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el gráfico para pH
    var graficoPH = echarts.init(document.getElementById('grafico-ph'));

    // Obtener los datos desde Django
    fetch('/home/datos-ph/')
        .then(response => response.json())
        .then(data => {
            // Extraer los datos para el gráfico
            const nodosPH = data.data.ph.map(item => item.nodo);
            const valoresPH = data.data.ph.map(item => item.cnt_ph);

            // Configuración del gráfico
            var opciones = {
                title: {
                    text: 'Nivel de pH',
                    subtext: 'Mediciones del nivel de pH',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['pH'],
                    top: '15%'
                },
                xAxis: {
                    type: 'category',
                    data: nodosPH, // Usar los nodos como etiquetas del eje X
                    name: 'Nodos'
                },
                yAxis: {
                    type: 'value',
                    name: 'pH'
                },
                series: [
                    {
                        name: 'pH',
                        type: 'bar',
                        data: valoresPH,
                        color: '#91CC75'
                    }
                ]
            };

            // Establecer las opciones del gráfico
            graficoPH.setOption(opciones);
            const estadoTextoPH = document.getElementById('estado-ph');
            const estadosPH = valoresPH.map(valor => {
                if (valor >= 6.5 && valor <= 7.5) {
                    return 'Bueno';
                } else if (valor >= 5.5 && valor < 6.5 || valor > 7.5 && valor <= 8.5) {
                    return 'Regular';
                } else {
                    return 'Malo';
                }
            });
            
            // Mostrar el estado para cada nodo
            estadoTextoPH.innerHTML = nodosPH.map((nodo, index) => {
                return `<b>${nodo}</b>: ${estadosPH[index]}`;
            }).join('<br>');

        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
});
