# Investcraft Sim
***
# Some illustration pictures.
<img src="md files/image.png" alt="drawing" width="250"/>
<img src="md files/image-1.png" alt="drawing" width="250"/>
<img src="md files/image-2.png" alt="drawing" width="250"/>
<img src="md files/image-4.png" alt="drawing" width="250"/>

***
# Description

The web application will primarily be intended for people interested in analyzing the stock market and, in particular, understanding why certain price movements occur at certain points. The application features a simple dashboard that can be easily customized to suit preferences, where news, charts, and financial information are combined on one dashboard available on the same webpage. Furthermore, it is possible to run your own simulation, replaying a portion of the market in the past. During the simulation, news articles will appear, allowing users to quickly and easily understand why certain price movements occurred during that period.

***
# Instructions
Pull the GitHub repository, and then in your terminal:
<br> <mark>pip3 install -r requirements.txt</mark><br>
<mark>flask run --debug</mark> will run the application.
***

# references
- https://github.com/karthik947/TVChartsOwnData for displaying a static chart. I partially adapted the code that actually displays the chart in chart.js.

- https://www.youtube.com/watch?v=d-M-8WHdb5E CodewithJ, how I create the Alpaca Trading API in config.py and how I format the stock string so that the trading widget understands which stock to use. Contributed to configAPI.py, not the same code but showed how to format convertwatchlist correctly in models.py and used one line in dashboard.html.

- https://www.youtube.com/watch?v=EjQ-3iXEPEs Part Time Larry, helped me understand how to get data from the Alpaca API and how to interpret the documentation. Unfortunately, the code he used was outdated because the API now had a v2 version instead of v1, but much of the terminology was the same. Contributed to configAPI.py in terms of code.

- https://github.com/startbootstrap/startbootstrap-sb-admin Bootstrap template.

- https://www.tradingview.com/widget/  for providing the basic widgets in the dashboard. The code in the index.html where the tradingview widgets are located, is derived from here.



Apart from that, no code has been copied from other platforms. I have used some platforms such as w3schools, Stack Overflow, or Reddit to better understand certain concepts, and I have visited some educational websites that explained various examples of what I was trying to achieve. No code has been copied from these sources, and they only served to understand the concepts.

***
# Video Links
here is the Youtube link where i walk through the application (in dutch):<br>
https://youtu.be/6uQHKZMBzYc
<br>
<br>
<br>
For better quality video scan the QR-code. <br>
<img src="md files/qr-code.png" alt="drawing" width="250"/>
***
