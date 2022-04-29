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
    df = (
        pd.read_excel(url, index_col=0, usecols=[0, 1, 2, 3])
        .loc[kind.title()]
        .dropna()
        .reset_index(drop=True)
    )
    return df

