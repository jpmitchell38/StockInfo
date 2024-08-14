# StockInfo

**Link to the website:** https://stockinfo-dtbq.onrender.com

This project has multiple pages you could visit. The Graphing page allows users to input a list of stocks and specify the number of days back from which to retrieve data. It fetches this data and presents four insightful graphs: Closing Price vs Time, Closing Price vs Volume, Volume vs Time, and High-Low Range vs Time. The Analysis page allows users to input a stock ticker to retrieve and visualize stock analysis data. Once a ticker is submitted, the page fetches data from approximately 50 analysts who have evaluated the stock. This information is then represented on a line graph, showcasing the average rating consensus. The ratings are categorized into five distinct levels: Strong Sell, Sell, Hold, Buy, and Strong Buy. The Metrics page allows users to enter a stock ticker to view various financial metrics. The page displays key indicators such as the current price, P/E ratio, PEG ratio, dividend yield, profit margin, and short interest, providing a comprehensive overview of the stock’s financial health. The Generate Report page enables users to input a list of stocks for evaluation. Based on specific metrics, it assesses each stock and categorizes it as Strong Buy, Buy, Maybe, or No Buy. The results are compiled into a downloadable CSV file, accessible via a button that appears once the report is generated.

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
    <img src="docs/Screenshot 2024-08-14 121529.png" alt="Graph 1" style="width: 48%; margin-bottom: 10px;" />
    <img src="docs/Screenshot 2024-08-14 121549.png" alt="Graph 2" style="width: 48%; margin-bottom: 10px;" />
    <img src="docs/Screenshot 2024-08-14 121611.png" alt="Graph 3" style="width: 48%; margin-bottom: 10px;" />
    <img src="docs/Screenshot 2024-08-14 121629.png" alt="Graph 4" style="width: 48%; margin-bottom: 10px;" />
</div>

<br>
Picture 1. Graphing page with aapl, rcl, and mcd entered <br>
Picture 2. Analysis page with tsla entered <br>
Picture 3. Metrics page with goog entered <br>
Picture 4. Generate Reports page after input was entered

<br><br>
## How Its Made:

Tech used: Python, HTML, CSS

The project utilizes Python for the backend, integrating the Yahoo Finance API and Finnhub API to fetch stock data. While Yahoo Finance provides dynamic data, Finnhub may offer data with varying update frequencies depending on the endpoint and subscription level. Flask manages incoming inputs from the web interface, routing them to the appropriate handlers based on user interactions with different pages. The HTML structure is organized for efficient styling with CSS, and tooltips have been integrated next to input boxes to enhance user experience and provide additional guidance.

<br><br>
## Note

Both the accounts that contributed to the project are mine