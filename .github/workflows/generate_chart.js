/**
 * generate_chart.js
 * -----------------
 * Reads data/repo_history.json, plots “count vs. timestamp” with Chart.js,
 * and writes stats/usage/totat.svg.
 */

const fs = require('fs-extra');
const { ChartJSNodeCanvas } = require('chartjs-node-canvas');

// Dimensions for the SVG
const width = 600;
const height = 300;
const chartJSNodeCanvas = new ChartJSNodeCanvas({
  width,
  height,
  chartCallback: (ChartJS) => {
    // No additional plugins needed for a simple line chart
  },
});

(async () => {
  // 1) Load history
  const historyFile = 'data/repo_history.json';
  if (!fs.existsSync(historyFile)) {
    console.error('❌ data/repo_history.json not found!');
    process.exit(1);
  }
  const history = fs.readJsonSync(historyFile);
  // Sort by timestamp just to be safe
  history.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));

  const labels = history.map((entry) => entry.timestamp);
  const data = history.map((entry) => entry.count);

  // 2) Chart configuration
  const configuration = {
    type: 'line',
    data: {
      labels,
      datasets: [
        {
          label: 'Unique Repos Using JF_URL',
          data,
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1,
          pointRadius: 3,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: 'time',
          time: {
            parser: 'YYYY-MM-DDTHH:mm:ssZ',
            unit: 'day',
            tooltipFormat: 'YYYY-MM-DD',
          },
          title: {
            display: true,
            text: 'Date',
          },
        },
        y: {
          title: {
            display: true,
            text: 'Unique Repo Count',
          },
          beginAtZero: true,
        },
      },
      plugins: {
        legend: { display: false },
        title: {
          display: true,
          text: '“JF_URL” Usage Over Time',
        },
      },
    },
  };

  // 3) Render as SVG
  const svgBuffer = await chartJSNodeCanvas.renderToBuffer(configuration, 'image/svg+xml');
  fs.ensureDirSync('stats/usage');
  fs.writeFileSync('stats/usage/totat.svg', svgBuffer);
  console.log('✅ Chart generated at stats/usage/totat.svg');
})();
