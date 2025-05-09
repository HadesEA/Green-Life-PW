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
        const recomendacionesHumedad = {
            "Bueno": "El nivel de humedad es óptimo, no es necesaria intervención.",
            "Regular": "El nivel de humedad es moderado, considere ajustar el riego.",
            "Malo": "El nivel de humedad es bajo, se recomienda incrementar el riego."
        };
        const estadosHumedad = valoresCounter.map(valor => {
            if (valor >= 70) {
                return 'Bueno';
            } else if (valor >= 40) {
                return 'Regular';
            } else {
                return 'Malo';
            }
        });
        estadoTextoHumedad.innerHTML = nodosCounter.map((nodo, index) => {
            const estado = estadosHumedad[index];
            return `
                <b>${nodo}</b>: ${estado}<br>
                <i>Recomendación: ${recomendacionesHumedad[estado]}</i>
            `;
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
        // Gases
        const estadoTextoGas = document.getElementById('estado-gas');

        // Recomendaciones específicas para MQ7 y MQ8
        const recomendacionesGas = {
            "Bueno": "La concentración de gases está dentro de un nivel seguro.",
            "Regular": "La concentración de gases es moderada, monitorea para posibles ajustes.",
            "Malo": "La concentración de gases es alta, considera tomar medidas de ventilación o mitigación."
        };

        // Estados para MQ7 y MQ8
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

        // Mostrar el estado y recomendación para cada nodo
        estadoTextoGas.innerHTML = nodosMQ7.map((nodo, index) => {
            const estadoMQ7 = estadosMQ7[index];
            const estadoMQ8 = estadosMQ8[index];
        
            return `
                <b>${nodo}</b>:<br>
                <b>MQ7 (Monóxido de Carbono)</b>: ${estadoMQ7} <i>Recomendación: ${recomendacionesGas[estadoMQ7]}</i><br>
                <b>MQ8 (Hidrógeno)</b>: ${estadoMQ8} <i>Recomendación: ${recomendacionesGas[estadoMQ8]}</i>
            `;
        }).join('<br><br>');


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
        const recomendacionesTemperatura = {
            "Bueno": "La temperatura es adecuada, no se requiere intervención.",
            "Regular": "La temperatura está moderada, considere monitorear frecuentemente.",
            "Malo": "La temperatura es extrema, ajuste las condiciones del ambiente."
        };
        const estadosTemperatura = valoresTemperaturaTC.map(valor => {
            if (valor >= 15 && valor <= 25) {
                return 'Bueno';
            } else if ((valor > 25 && valor <= 35) || (valor >= 10 && valor < 15)) {
                return 'Regular';
            } else {
                return 'Malo';
            }
        });
        estadoTextoTemperatura.innerHTML = nodosTemperaturaTC.map((nodo, index) => {
            const estado = estadosTemperatura[index];
            return `
                <b>${nodo}</b>: ${estado}<br>
                <i>Recomendación: ${recomendacionesTemperatura[estado]}</i>
            `;
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

            const estadoTextoLux = document.getElementById('estado-lux');
            const recomendacionesLux = {
                "Bueno": "La intensidad lumínica es adecuada.",
                "Regular": "La intensidad lumínica es moderada, considere ajustes en iluminación.",
                "Malo": "La intensidad lumínica es insuficiente, realice cambios inmediatos."
            };
            const estadosLux = valoresLUX.map(valor => {
                if (valor >= 60000) {
                    return 'Bueno';
                } else if (valor >= 30000) {
                    return 'Regular';
                } else {
                    return 'Malo';
                }
            });
            estadoTextoLux.innerHTML = nodosLUX.map((nodo, index) => {
                const estado = estadosLux[index];
                return `
                    <b>${nodo}</b>: ${estado}<br>
                    <i>Recomendación: ${recomendacionesLux[estado]}</i>
                `;
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
            const recomendacionesPH = {
                "Bueno": "El nivel de pH es óptimo.",
                "Regular": "El nivel de pH es moderado, considere ajustes pequeños.",
                "Malo": "El nivel de pH es crítico, realice ajustes inmediatos."
            };
            const estadosPH = valoresPH.map(valor => {
                if (valor >= 6.5 && valor <= 7.5) {
                    return 'Bueno';
                } else if ((valor >= 5.5 && valor < 6.5) || (valor > 7.5 && valor <= 8.5)) {
                    return 'Regular';
                } else {
                    return 'Malo';
                }
            });
            estadoTextoPH.innerHTML = nodosPH.map((nodo, index) => {
                const estado = estadosPH[index];
                return `
                    <b>${nodo}</b>: ${estado}<br>
                    <i>Recomendación: ${recomendacionesPH[estado]}</i>
                `;
            }).join('<br>');

        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
});

document.addEventListener("DOMContentLoaded", function () {
  // Crear un arreglo global para recopilar elementos en estado crítico
  let elementosCriticosTotales = [];

  // Función para mostrar notificaciones
  function mostrarNotificacion(elementosCriticos) {
    const notificacionDiv = document.getElementById('notificacion');
    const contenidoDiv = document.getElementById('contenido-notificacion');

    if (elementosCriticos.length > 0) {
        const mensaje = `
            ⚠️ <strong>Alerta:</strong> Los siguientes elementos están en estado crítico:<br>
            <ul>
                ${elementosCriticos.map(el => `<li>${el}</li>`).join('')}
            </ul>
        `;
        contenidoDiv.innerHTML = mensaje;
        notificacionDiv.style.display = 'block';
    } else {
        notificacionDiv.style.display = 'none';
    }

    // Agregar evento para cerrar la notificación
    const botonCerrar = document.getElementById('cerrar-notificacion');
    botonCerrar.addEventListener('click', () => {
        notificacionDiv.style.display = 'none';
    });
}

  // Cargar y procesar los datos para cada gráfico
  const procesarDatosHumedad = () => {
      return fetch('/home/datos-humedad/')
          .then(response => response.json())
          .then(data => {
              const nodosCounter = data.data.counter.map(item => item.nodo || "Nodo Desconocido");
              const valoresCounter = data.data.counter.map(item => item.cnt);

              const estadosHumedad = valoresCounter.map(valor => {
                  if (valor >= 70) return 'Bueno';
                  if (valor >= 40) return 'Regular';
                  return 'Malo';
              });

              const criticosHumedad = nodosCounter.filter((_, index) => estadosHumedad[index] === 'Malo')
                  .map(nodo => `${nodo} (Humedad Ambiente)`);

              elementosCriticosTotales.push(...criticosHumedad);
          });
  };

  const procesarDatosTemperaturaSuelo = () => {
    return fetch('/home/datos-temperatura/')
        .then(response => response.json())
        .then(data => {
            const nodosTemperaturaTC = data.data.tc.map(item => item.nodo || "Nodo Desconocido");
            const valoresTemperaturaTC = data.data.tc.map(item => item.cnt_tc);

            const estadosTemperaturaTC = valoresTemperaturaTC.map(valor => {
                if (valor >= 15 && valor <= 25) return 'Bueno';
                if (valor > 25 && valor <= 35 || valor >= 10 && valor < 15) return 'Regular';
                return 'Malo';
            });

            const criticosTemperaturaTC = nodosTemperaturaTC.filter((_, index) => estadosTemperaturaTC[index] === 'Malo')
                .map(nodo => `${nodo} (Temperatura TC)`);

            elementosCriticosTotales.push(...criticosTemperaturaTC);
        });
};

  const procesarDatosGas = () => {
      return fetch('/home/datos-gas/')
          .then(response => response.json())
          .then(data => {
              const nodosMQ7 = data.data.mq7.map(item => item.nodo || "Nodo Desconocido");
              const valoresMQ7 = data.data.mq7.map(item => item.cnt_mq7);

              const estadosMQ7 = valoresMQ7.map(valor => {
                  if (valor < 500) return 'Bueno';
                  if (valor < 1000) return 'Regular';
                  return 'Malo';
              });

              const criticosGas = nodosMQ7.filter((_, index) => estadosMQ7[index] === 'Malo')
                  .map(nodo => `${nodo} (MQ7)`);

              elementosCriticosTotales.push(...criticosGas);
          });
  };

  const procesarDatosPH = () => {
      return fetch('/home/datos-ph/')
          .then(response => response.json())
          .then(data => {
              const nodosPH = data.data.ph.map(item => item.nodo || "Nodo Desconocido");
              const valoresPH = data.data.ph.map(item => item.cnt_ph);

              const estadosPH = valoresPH.map(valor => {
                  if (valor >= 6.5 && valor <= 7.5) return 'Bueno';
                  if ((valor >= 5.5 && valor < 6.5) || (valor > 7.5 && valor <= 8.5)) return 'Regular';
                  return 'Malo';
              });

              const criticosPH = nodosPH.filter((_, index) => estadosPH[index] === 'Malo')
                  .map(nodo => `${nodo} (pH)`);

              elementosCriticosTotales.push(...criticosPH);
          });
  };

  // Procesar los datos para todos los gráficos y luego mostrar notificaciones
  Promise.all([procesarDatosHumedad(), procesarDatosGas(), procesarDatosPH(), procesarDatosTemperaturaSuelo()])
      .then(() => {
          mostrarNotificacion(elementosCriticosTotales);
      })
      .catch(error => {
          console.error('Error al procesar los datos:', error);
      });
});
