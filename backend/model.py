import librosa
import pandas as pd
import numpy as np
import pickle
import sys
import os
# from PIL import Image
import pathlib
import csv
from IPython.display import Audio
import pickle as pk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score


# load csv file
load_file = pd.read_csv(r"D:\Ki2-2021\XLTN\pythonProject\data\data.csv")
genre_list = load_file.iloc[:, -1]

encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)

# split train and test dataset
X_train, X_test, y_train, y_test = train_test_split(load_file.iloc[:, :-1], y, test_size=0.2)



# n_estimators = 2000
# max_depth = 13
# learning_rate = 0.1
# xgb = XGBClassifier(
#     n_estimators=n_estimators,
#     learning_rate = learning_rate,
#     max_depth=max_depth,
#     subsample=0.9,
#     colsample_bytree=0.9,
#     missing=-1
#     # random_state=300,
#     # tree_method='gpu_hist'
#     )
#
# lgbm = LGBMClassifier(
#     n_estimators=n_estimators,
#     learning_rate = learning_rate,
#     max_depth=max_depth,
#     subsample=0.9,
#     colsample_bytree=0.9,
#     missing=-1
#     # tree_method='gpu_hist'
#     )
#
# lgbm.fit(X_train, y_train)
# xgb.fit(X_train, y_train)

# save model
# filename = 'model/model_xgb.sav'
# pk.dump(xgb, open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), filename)), 'wb'))
# loaded_model = pickle.load(open(r"C:\Users\asus\Desktop\pythonProject\model\Booster.save_model","rb"))

# evaluate model
# test_lgbm = lgbm.predict(X_test)
# test_xgb = xgb.predict(X_test)

loaded_model = pickle.load(open(r'D:\Ki2-2021\XLTN\pythonProject\model\xgb.pkl', 'rb'))
result = loaded_model.score(X_test, y_test)
model_test = loaded_model.predict(X_test)
print( accuracy_score(model_test,y_test))
# print(model.score(test_sample, y_test))
