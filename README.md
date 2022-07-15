# SOFT_ENG2
WEB SCRAPING AND DATA VISUALIZATION

A Web based scraping system that analyses and visualizes data from indicated sources.


# ABOUT THE PROJECT
The project is built under Django Web Framework using Anaconda (Python Distribution) so django and other python dependencies are required to run the project. 
All python dependencies are listed in the requirements.txt file

If you are having a hard time installing the python dependencies from the requirements.txt file,
this site may help; 
    https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t

# USER INTERFACE

Home Page
![Home Page](https://github.com/JurYel/SOFT_ENG2/blob/master/homepage.PNG)

Movies Data Page
![Movies](https://github.com/JurYel/SOFT_ENG2/blob/master/movies.PNG)

Movies Data Scraped Data Sample
![Scraped](https://github.com/JurYel/SOFT_ENG2/blob/master/scraped_data.PNG)

Movies Data Visualization
![Viz](https://github.com/JurYel/SOFT_ENG2/blob/master/visualization.PNG)

Data Analysis
![Analysis](https://github.com/JurYel/SOFT_ENG2/blob/master/analyses.PNG)

# ABOUT THE SCRAPERS

Scrapy framework is used for scraping data from indicated sources.
The database used is MySQL relational database.
As for the depencies for MySQL, mysqlclient is used for this.
In case you are having a rough time downloading mysqlclient or find errors in doing so.
I recommend you download the wheel version of mysqlclient from this site;

https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

Download the mysqlclient that matches your python version.
To locally install the dependency;
  - Open CMD in the directory of mysqlclient
  - Then install your wheel file with 'pip install mysqlclient‑1.3.13‑cp36‑cp36m‑win_amd64.whl'
  - It should be good to go

# Ecommerce Data Scraper

The Shopee Data Scraper utilizes Splash for loading dynamic sites. 
Splash requires Docker to be installed;
  - Install docker from https://docs.docker.com/get-docker/
  - Then install Splash from https://splash.readthedocs.io/en/stable/install.html
  - Run Splash afterwards in order to start the shopee crawler.
  
 

