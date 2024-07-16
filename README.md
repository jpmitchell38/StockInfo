# StockInfo

This project allows users to input a list of stocks and specify the number of days back from which to retrieve data. It fetches this data and presents four insightful graphs: Closing Price vs Time, Closing Price vs Volume, Volume vs Time, and High-Low Range vs Time.

Both the accounts that you see contributed to the projects are both mine

<div style="display: flex; justify-content: space-between;">
    <img src="docs/Screenshot 2024-07-15 142147.png" alt="Graph 1" style="width: 45%;"/>
    <img src="docs/Screenshot 2024-07-15 144409.png" alt="Graph 2" style="width: 45%;"/>
</div>

## How Its Made:

Tech used: Python, HTML, CSS

I utilized Python for the backend of this project, enabling connectivity to the Yahoo Finance API to fetch stock data dynamically. With Flask, I managed incoming inputs from the web interface. The HTML structure neatly organizes content for easy styling with CSS.

## How to Run

```git clone https://github.com/jpmitchell38/StockInfo.git```
<button class="copy-button" onclick="copyCommand('git clone https://github.com/jpmitchell38/StockInfo.git')">Copy</button>

```cd StockInfo/```
<button class="copy-button" onclick="copyCommand('cd StockInfo/')">Copy</button>

```pip install -r requirements.txt```
<button class="copy-button" onclick="copyCommand('pip install -r requirements.txt')">Copy</button>

```python StockMain.py```
<button class="copy-button" onclick="copyCommand('python StockMain.py')">Copy</button>

You can copy the URL provided, which starts with "http://"

<script>
  function copyCommand(command) {
    // Create a temporary textarea element
    var textarea = document.createElement('textarea');
    textarea.value = command;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px'; // Move the textarea off the screen
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Copied to clipboard: ' + command);
  }
</script>


