# Data Engineering Project

## Overview

The goal of this project was to create a database of graded Pokemon cards from eBay using Python web scraping and the PokeAPI. I cleaned the collected data in MySQL and used Postman to test the API connection. My future plan is to automate and schedule the Python script for continuous data collection.

This data will allow me to investigate the question: "Which Pokemon cards from different eras and grading companies consistently sell for the highest prices on eBay?"  By analyzing factors like listing price, grading company, and card edition, I hope to identify trends that can help determine the rarest and most sought-after Pokemon cards.


### Data Visualization

<img width="908" alt="image" src="https://github.com/Karan-Manhas/PokemonCardMarketDynamics/assets/94873627/60571207-adb1-4092-bfb4-8adf2231880c">


### Data Architecture

![Example architecture image](example-architecture.png)

![deproject](https://github.com/Karan-Manhas/PokemonCardMarketDynamics/assets/94873627/6a0ee01c-4d77-4f87-ae6b-7e0202d623ef)

- The current architecture can easily be modified to be autoamted using Cloud Schedulers in order to prevent the manual exporting. This method was chosen in order to obtain the fastest result.


## Lessons Learned

To further enhance this project, in the future I will use Apache Airflow to set schedules and run the python script itself.
## Contact

Please feel free to contact me if you have any questions at: karanmanhas711@gmail.com 
