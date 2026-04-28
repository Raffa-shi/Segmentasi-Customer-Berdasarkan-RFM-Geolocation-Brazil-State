import pandas as pd

def load_data():
    rfm = pd.read_csv('data/rfm.csv')
    segment = pd.read_csv('data/segment_analysis.csv')
    geo = pd.read_csv('data/geo.csv')
    
    return rfm, segment, geo