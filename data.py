import pandas as pd

def load_data():
    df = pd.read_csv(r'C:\Users\Lenovo\project\UCL_Finals2.csv')
    return df

df = load_data()
