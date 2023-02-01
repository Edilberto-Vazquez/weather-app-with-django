const URL = "http://127.0.0.1:8000/line-chart-data-api/";

const getUrlDate = (date_type) => {
  const positions = new Map([
    ["from", 3],
    ["to", 4],
  ]);

  return window.location.pathname
    .split("/")
    [positions.get(date_type)].split("%")[0];
};

let date_field = "month";
let from_date = getUrlDate("from");
let to_date = getUrlDate("to");
let chart = null;

const generateURL = (station_id, date_field, from_date, to_date) => {
  return `${URL}${station_id}/${date_field}/${from_date}/${to_date}`;
};

const getChartData = (url) => {
  return fetch(url)
    .then((response) => response.json())
    .then((data) => data)
    .catch((error) => {
      console.error(error);
    });
};

const printChart = async (date_field, from_date, to_date) => {
  const ctx = document.getElementById("chart");

  if (chart !== null) {
    chart.destroy();
  }

  const { datasets, labels } = await getChartData(
    generateURL(ctx.attributes.name.value, date_field, from_date, to_date)
  );

  const config = {
    type: "line",
    data: {
      labels: labels,
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

  chart = new Chart(ctx, config);
};

const dateButton = (field) => () => {
  date_field = field;
  printChart(date_field, from_date, to_date);
};

const datePicker = (e) => {
  if (new Date(e.target.value) > new Date(to_date)) {
    alert("From Date cannot be greater than to Date");
    return;
  } else {
    if (new Date(e.target.value) < new Date(from_date)) {
      alert("To Date cannot be less than From Date");
      return;
    }
  }
  switch (e.target.id) {
    case "from-date-picker":
      from_date = e.target.value;
      printChart(date_field, from_date, to_date);
      break;
    case "to-date-picker":
      to_date = e.target.value;
      printChart(date_field, from_date, to_date);
      break;
  }
};

const monthButton = document
  .getElementById("month-button")
  .addEventListener("click", dateButton("month"));
const yearButton = document
  .getElementById("year-button")
  .addEventListener("click", dateButton("year"));

// Get datepickers
const fromDatePicker = document.getElementById("from-date-picker");
const toDatePicker = document.getElementById("to-date-picker");
// Set default values
fromDatePicker.valueAsDate = new Date(from_date);
toDatePicker.valueAsDate = new Date(to_date);
// add onclic event
fromDatePicker.addEventListener("input", datePicker);
toDatePicker.addEventListener("input", datePicker);

printChart(date_field, from_date, to_date);
