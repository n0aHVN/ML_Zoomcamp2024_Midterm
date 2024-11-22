import pandas as pd
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("banana.csv")

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



df_train_full, df_test = train_test_split(df, test_size=0.2) #Random state is seed
y_train_full = df_train_full.quality_score
def train(df, y):
    cat = df.to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    dv.fit(cat)

    X = dv.transform(cat)

    model = LinearRegression()
    model.fit(X, y)

    return dv, model

dv,model = train(df_train_full[str_cols+num_cols], y_train_full)
f_name = 'model.bin'

with open(f_name, "wb") as f_out:
	pickle.dump((dv,model), f_out)
