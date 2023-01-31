const URL = "http://127.0.0.1:8000/analysis/line-chart-data-api/";

const getChartData = (station_id) => {
  return fetch(URL + station_id)
    .then((response) => response.json())
    .then((data) => data)
    .catch((error) => {
      console.error(error);
    });
};

const printChart = async () => {
  const ctx = document.getElementById("chart");

  const { datasets } = await getChartData(ctx.attributes.name.value);

  console.log(datasets);

  const config = {
    type: "line",
    data: {
      //   labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: datasets,
    },
    options: {
      plugins: {
        zoom: {
          zoom: {
            wheel: {
              enabled: true,
            },
            pinch: {
              enabled: true,
            },
            mode: "xy",
          },
        },
      },
    },
  };

  new Chart(ctx, config);
};

printChart();
