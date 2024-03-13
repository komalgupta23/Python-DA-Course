import pandas as pd
import numpy as np
import plotly.express as px 
import streamlit as st 
import os

# 1. Load the data

def load_data():
    df = pd.read_excel('Canada.xlsx', sheet_name = 1, skiprows = 20, skipfooter = 2)
    
    #col to drop
    cols_to_drop = ['AREA', 'REG', 'DEV', 'Type', 'Coverage']
    df = df.drop(columns = cols_to_drop, inplace = True)
    # rename columns
    df = df.rename(columns = {
        'Odname' : 'Country',
        'AreaName' : 'Continent',
        'RegName' : 'Region',
        'DevName' : 'Status'
    })
    
    # add a total coulmn
    years = list(range(1980, 2014))
    df['total'] = df[years].sum(axis = 1)
    df.set_index('Country', inplace = True)
    return df
