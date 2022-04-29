import numpy as np
import pandas as pd

## importing road safety datasets
def get(kind, year):
    """
    import road safety data sets from UK department for transport.
    """
    url = f"https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-{kind}-{year}.csv"
    df = pd.read_csv(url, low_memory=False, index_col=0)
    return df
## importing data guide
def lookup(kind):
    """
    import road safety data guide
    """
    url = "https://data.dft.gov.uk/road-accidents-safety-data/Road-Safety-Open-Dataset-Data-Guide.xlsx"
    df = pd.read_excel(url, index_col=0, usecols=[0, 1, 2, 3]).loc[kind]
    df.set_index("field name", drop=True, inplace=True)
    return df
## creating code/format:label pair values
def load_descriptions(group_data):
    code_label_dict = dict(zip(group_data['code/format'], group_data['label']))
    return ( 
        pd.DataFrame({'code': code_label_dict.keys(), 'format': code_label_dict.values()}).dropna()
    )
## creating code/label pair values for each field name
def lookup_pairs(kind):
    """
    get pair values for each field name
    """
    df = (
    lookup(kind).groupby('field name')
    .apply(load_descriptions)
    .reset_index(level=1, drop=True)
    .reset_index()
    .rename(columns={'field name': 'field_name'})
    .groupby('field_name')
    .apply(lambda group: dict(zip(group['code'], group['format'])))
    .to_frame()
    .rename(columns={0:'descriptions'})
    )
    return df


