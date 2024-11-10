
const getOptionChart = async () => {
    try {
        const response=await fetch("http://localhost:8000/home/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex);        
    }    
};


const initChart=async () => {
    const myChart=echarts.init(document.getElementById("chart"));
    const options = await getOptionChart()
    console.log("Chart options:", options);
    myChart.setOption(options);
    myChart.resize();
};



window.addEventListener("load",async () => {
    await initChart();    
});