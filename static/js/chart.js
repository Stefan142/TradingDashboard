// Retrieving the value of an element with the id 'my_variable' S.O. to Discchord on reddit for providing a loop around using AJAX calls.
var test = document.querySelector('#my_variable').value;

// Function to fetch and process historical market data from the CSV file
const getData = async () => {
  // Fetches the CSV file containing historical market data
  const res = await fetch('/static/data/Histmarketdata.csv');
  const resp = await res.text();
  
  // Split the CSV data into rows and exclude the header and the last empty row, since csv files always contain empty last row.
  const rows = resp.split('\n').filter((row, index) => index > 0 && row.trim() !== '');

  // Maps each CSV row to an object with timestamp and market data
  const cdata = rows.map((row) => {
    const [timestamp, open, high, low, close] = row.split(',');
    return {
      time: new Date(`${timestamp}`).getTime() / 1000,
      open: open * 1,
      high: high * 1,
      low: low * 1,
      close: close * 1,
    };
  });

  // Returns the processed market data
  return cdata;
};

// Function to display a financial chart using market data
const displayChart = async () => {
  // Properties for the financial chart
  const chartProperties = {
    width: 700,
    height: 400,
    timeScale: {
      timeVisible: true,
      secondsVisible: true,
    },
  };

  // Retrieves the DOM element with the id 'tvchart'
  const domElement = document.getElementById('tvchart');
  // Creates a financial chart with specified properties
  const chart = LightweightCharts.createChart(domElement, chartProperties);
  // Adds a candlestick series to the chart
  const candleseries = chart.addCandlestickSeries();
  // Retrieves historical market data
  const klinedata = await getData();

  // Function to update the chart with a given number of rows
  const updateChart = (rowsToShow) => {
    const partialData = klinedata.slice(0, rowsToShow);
    candleseries.setData(partialData);
  };

  // Initial display with no rows
  candleseries.setData([]);

  let currentIndex = 0;
  const totalRows = klinedata.length;

  // Update the chart every 'test' seconds
  const intervalId = setInterval(() => {
    if (currentIndex < totalRows) {
      const rowsToShow = currentIndex + 1;
      // Updates the chart with the specified number of rows
      updateChart(rowsToShow);
      currentIndex += 1;
    } else {
      // Stop the interval when all rows are displayed
      clearInterval(intervalId);
    }
  }, test * 1000);
};


displayChart();