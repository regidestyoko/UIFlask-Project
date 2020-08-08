# Google Play Store Analytics
<img src="https://raw.githubusercontent.com/fafilia/capstone-UIFlask/master/full_capstone.png">

## Introduction
This project is a collaboration with the algorithm team. The goal of this project is to build a simple web application (dashboard) using the Flask framework. This project will focus on the appearance of the Flask user interface.

## Data Summary
The data used in this project is scraping data from the Google Playstore App. Google Playstore App data consists of several variables with the following details:

- `App`: Application name
- `Category`: Application category
- `Rating`: The overall rating given by the application user (when scraped)
- `Reviews`: Number of reviews provided by application users (when scraped)
- `Size`: Application size (when scraped)
- `Installs`: Number of users who installed / downloaded the application (When scraped)
- `Type`: Application type (paid / free)
- `Price`: Application price (when scraped)
- `Content Rating`: The age group of this app is targeted - Children / Mature 21+ / Adult
- `Genres`: Application genre.
- `Last Updated`: The date when the application was last updated on the Play Store (when scraped)
- `Current Ver`: Current version of the app available on Play Store (when scraped)
- `Android Ver`: Minimum Android version required (when scraped)

## Dependencies
- Flask
- Matplotlib
- Pandas
- Numpy

All of these modules can be installed by:
```
pip install -r requirements.txt
```

### 1. Preprocessed Data and Exploratory Data Analysis
At this preprocessing stage, you are asked to complete the preprocessing data such as removing duplicate data, changing data types and modifying data values.

### 2. Data Wrangling
- At this stage, grouping and aggregating data. Data wrangling is used to prepare the right data according to the analysis requested. As an illustration, in the `stats` object, there is a variable` rev_tablel` where the data is processed by grouping and aggregation so as to create a data table as below:

    <img src="https://raw.githubusercontent.com/fafilia/capstone-UIFlask/master/table_rev.PNG" width=400>

### 3. Data Visualization
- Create or duplicate a plot bar depicting the top 5 Categories on the Google Playstore
- Create or duplicate a scatter plot that describes the distribution of the application based on reviews, ratings, and the number of installed applications.
- Create or duplicate plot histograms to view application size distribution


### 4. Build Flask App
Demonstrate how to render these plots in a Flask application and display them in an html templates / page. Noteworthy is the `app.py` section:
```
render_templates(__________)
```
in `templates / index.html` need to call the source plot.png where to save the plot image.
```
<img src="________________________" height="450" width=500>
```
