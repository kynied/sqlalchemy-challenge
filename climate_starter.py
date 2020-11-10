#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


import datetime as dt


# In[ ]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[ ]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[ ]:


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)


# In[ ]:


# We can view all of the classes that automap found
Base.classes.keys()


# In[ ]:


# Save references to each table
measurement_table = Base.classes.measurement
station_table = Base.classes.station


# In[ ]:


# Create our session (link) from Python to the DB
session = Session(engine)


# In[ ]:


# Design a query to retrieve the last 12 months of precipitation data and plot the results
# Calculate the date 1 year ago from the last data point in the database
date = dt.datetime.strptime(session.query(func.max(measurement_table.date))[0][0],'%Y-%m-%d')
date_prior = date - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
precip_scores = session.query(measurement_table.prcp, measurement_table.date).filter(measurement_table.date > date_prior)

# Save the query results as a Pandas DataFrame and set the index to the date column
precip_df = pd.DataFrame(precip_scores)
precip_df = precip_df.rename(columns = {"date" : "Date", "prcp" : "Precipitation"})
precip_df = precip_df.set_index("Date")

# Sort the dataframe by date
precip_df = precip_df.sort_values(by="Date")

# Use Pandas Plotting with Matplotlib to plot the data
precip_df.plot(rot = 90, figsize = (10, 5))
plt.ylabel("Inches of Precipitation per Day")


# In[ ]:


# Use Pandas to calcualte the summary statistics for the precipitation data
precip_df.describe()


# In[ ]:


# Design a query to show how many stations are available in this dataset?
stations = session.query(station_table.station).count()
print(stations)


# In[ ]:


# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.
active_stations = session.query(station_table.station, station_table.name, func.count(measurement_table.station)).    filter(measurement_table.station == station_table.station).    group_by(measurement_table.station).    order_by(func.count(measurement_table.station).desc()).all()
active_stations


# In[ ]:


# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature of the most active station?
most_active_station = active_stations[0][0]
most_active_station_data = session.query(func.min(measurement_table.tobs),func.max(measurement_table.tobs),func.avg(measurement_table.tobs)).    filter(measurement_table.station == most_active_station).all()
most_active_station_data


# In[ ]:


# Choose the station with the highest number of temperature observations.
most_observations = session.query(measurement_table.date, measurement_table.tobs).    filter(measurement_table.station == station_table.station).filter(measurement_table.date > date_prior).all()

most_observations_df = pd.DataFrame(most_observations)

# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
most_observations_df["tobs"].plot(kind ='hist', bins = 12)
# Pulls first ID directly from tuple
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.legend()

