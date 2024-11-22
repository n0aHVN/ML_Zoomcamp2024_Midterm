import pandas as pd
import numpy as np
import requests

url = 'http://localhost:9696/predict'

df = pd.read_csv('banana.csv')
del df['sample_id']
str_cols = df.select_dtypes(include=['object', 'string']).columns.to_list()
num_cols = df.select_dtypes(exclude=['object','string']).columns.to_list()
if str_cols.__contains__('quality_category'):
    str_cols.remove('quality_category')
    print('Remove quality_category')
if str_cols.__contains__('harvest_date'):
    str_cols.remove('harvest_date')
    print('Remove harvest_date')

if num_cols.__contains__('quality_score'):
    num_cols.remove('quality_score')
    print('Remove quality_score')


def predict_single_test(df: pd.DataFrame, 
                        str_cols: list,
                        num_cols:list):
    print("This is predict single banana")
    df = df[str_cols+num_cols]
    random_index = np.random.randint(0,1000)
    row = df.iloc[random_index].to_dict()
    response = requests.post(url, json=row)
    result = response.json()
    print(row)
    print(result)
    print('\n')

def predict_multiple_test(df: pd.DataFrame,
                        str_cols: list,
                        num_cols:list):
    print("This is predict multiple bananas")
    df = df[str_cols+num_cols]
    random_indexes = np.random.randint(0,1000,size=5)
    rows = df.iloc[random_indexes].to_dict(orient='records')
    response = requests.post(url, json=rows)
    results = response.json()
    
    for row, result in zip(rows, results):
        print(row)
        print(result)
        print('\n')

def main():
    predict_single_test(df, str_cols,num_cols)
    predict_multiple_test(df,str_cols,num_cols)
if __name__ == "__main__":
    main()