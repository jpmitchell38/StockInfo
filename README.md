# StockInfo

**Link to the website:** https://stockinfo-dtbq.onrender.com

This project allows users to input a list of stocks and specify the number of days back from which to retrieve data. It fetches this data and presents four insightful graphs: Closing Price vs Time, Closing Price vs Volume, Volume vs Time, and High-Low Range vs Time.

<div style="display: flex; justify-content: space-evenly;">
    <img src="docs/Screenshot 2024-08-05 140436.png" alt="Graph 1" style="width: 33%;"/>
    <img src="docs/Screenshot 2024-08-05 140732.png" alt="Graph 2" style="width: 33%;"/>
</div>
<br>
Picture 1. Main screen with nothing inputted <br>
Picture 2. Main screen after data is inputted (page is scrolled down)

<br><br>
## How Its Made:

Tech used: Python, HTML, CSS

I utilized Python for the backend of this project, enabling connectivity to the Yahoo Finance API to fetch stock data dynamically. With Flask, I managed incoming inputs from the web interface. The HTML structure neatly organizes content for easy styling with CSS. To enhance user experience and provide additional guidance, we have integrated tooltips next to the input boxes. When users hover over these tooltips, a helpful information box will appear. The input boxes include error checking that displays a helpful error message if the entered data is incorrect.†

† = See picture
<div style="display:flex; justify-content: space-evenly;">
    <img src="docs/Screenshot 2024-08-05 141635.png" alt="Graph 3" style="width: 33%;"/>
</div>

<br><br>
## Note

Both the accounts that contributed to the project are mine