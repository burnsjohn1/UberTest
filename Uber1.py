#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
open pandas as pd
import streamlit as st


# In[ ]:


st.title("Uber Pickups in New York")


# In[ ]:DATE_COLUMN="date/time"
DATA_URL = ( ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
data=pd.read_csv(DATA_URL),nrows=nrows)
lowercase=lamda x:str(x).lower()
data.rename(lowercase,axis="columns",inplace=True)
data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
Return data

data_load_state=st.text("Loading Data......")
data=load_data(10000)
data_load_state.text("Loading Data.....done! using cache data")



if st.checkbox("Show Raw Data"):
	st.subheader("Raw Data")
	st.write(data)
	
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# plot all data on a map with a slider
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
 
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)



DeltaGenerator()


# In[ ]:





# In[ ]:


data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data
data_load_state=st.text("Loading Data...")
data=load_data(10000)
data_load_state.text("Loading Data...Done!")

