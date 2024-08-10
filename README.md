# StockInfo

**Link to the website:** https://stockinfo-dtbq.onrender.com

This project has multiple pages you could visit. The Graphing page allows users to input a list of stocks and specify the number of days back from which to retrieve data. It fetches this data and presents four insightful graphs: Closing Price vs Time, Closing Price vs Volume, Volume vs Time, and High-Low Range vs Time. The Analysis page allows users to input a stock ticker to retrieve and visualize stock analysis data. Once a ticker is submitted, the page fetches data from approximately 50 analysts who have evaluated the stock. This information is then represented on a line graph, showcasing the average rating consensus. The ratings are categorized into five distinct levels: Strong Sell, Sell, Hold, Buy, and Strong Buy.

<div style="display: flex; justify-content: space-evenly;">
    <img src="docs/Screenshot 2024-08-09 195715.png" alt="Graph 1" style="width: 40%;"/>
    <img src="docs/Screenshot 2024-08-09 195756.png" alt="Graph 2" style="width: 40%;"/>
</div>
<br>
Picture 1. Graphing page with aapl, rcl, and mcd entered <br>
Picture 2. Analysis page

<br><br>
## How Its Made:

Tech used: Python, HTML, CSS

The project utilizes Python for the backend, integrating the Yahoo Finance API and Finnhub API to fetch stock data. While Yahoo Finance provides dynamic data, Finnhub may offer data with varying update frequencies depending on the endpoint and subscription level. Flask manages incoming inputs from the web interface, routing them to the appropriate handlers based on user interactions with different pages. The HTML structure is organized for efficient styling with CSS, and tooltips have been integrated next to input boxes to enhance user experience and provide additional guidance.

<br><br>
## Note

Both the accounts that contributed to the project are mine