import streamlit as st

# HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trend Visualization</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #chart-container {
            width: 80%;
            margin: auto;
        }
        canvas {
            display: block;
            width: 100%;
            height: 400px;
        }
    </style>
</head>
<body>
    <div id="chart-container">
        <canvas id="myLineChart"></canvas>
    </div>
    <script>
        // Trend data passed from Flask
        const trendDates = {trend_dates};
        const trendValues = {trend_values};

        // Check if data is valid
        if (trendDates.length === 0 || trendValues.length === 0) {
            console.error('No data available to display the chart.');
        } else if (trendDates.length !== trendValues.length) {
            console.error('Mismatch between dates and values length.');
        } else {
            const data = {
                labels: trendDates,
                datasets: [{
                    label: 'Trend Data',
                    data: trendValues,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 1,
                    fill: true
                }]
            };

            const config = {
                type: 'line',
                data: data,
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(tooltipItem) {
                                    return tooltipItem.dataset.label + ': ' + tooltipItem.raw;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Value'
                            }
                        }
                    }
                }
            };

            const ctx = document.getElementById('myLineChart').getContext('2d');
            new Chart(ctx, config);
        }
    </script>
</body>
</html>
"""

# Render the HTML in Streamlit
st.components.v1.html(html_code, height=600)