import librosa
import pandas as pd #processing csv files
import numpy as np
import pickle
import os
# from PIL import Image
import pathlib
import csv
import pickle as pk
from sklearn.svm import SVC
from lightgbm import LGBMClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

import os
import joblib

n_estimators = 1000
max_depth = 10
learning_rate = 0.1

class AudioModel:
    def __init__(self, model_path='D:\Ki2-2021\XLTN\pythonProject\model\lgbm.pkl'):
        if os.path.exists(model_path):
            with open(model_path, 'rb') as file:
                self.model = pickle.load(file)
                self.model = joblib.load(model_path)
        else:
            self.model = self.__train_model()
            joblib.dump(self.model, model_path, compress=0)

    def __train_model(self):
        loadFile = pd.read_csv("/content/drive/MyDrive/Ki2-2020-2021/XLTN/speech/data/train_data.csv")
        genre_list = loadFile.iloc[:, -1]
        X = loadFile.iloc[:, :-1]
        encoder = LabelEncoder()
        y = encoder.fit_transform(genre_list)
        lgbm = LGBMClassifier(
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            max_depth=max_depth,
            subsample=0.9,
            colsample_bytree=0.9,
            missing=-999,
            tree_method='gpu_hist'
        )
        lgbm.fit(X, y)
        return lgbm

    # def feature_audio_file(self, file_path):
    #     header = 'poly_features chroma_cens chroma_cqt chroma_stft tempogram spectral_centroid spectral_bandwidth spectral_rolloff spectral_contrast spectral_flatness zero_crossing_rate rmse'
    #     for i in range(1, 31):
    #         header += f' mfcc{i}'
    #     header = header.split(" ");
    #
    #     y, sr = librosa.load(file_path, sr=22050)
    #
    #     mfcc = librosa.feature.mfcc(y, n_mfcc=30)
    #     poly_features = librosa.feature.poly_features(y)
    #     chroma_cens = librosa.feature.chroma_cens(y)
    #     chroma_cqt = librosa.feature.chroma_cqt(y)
    #     chroma_stft = librosa.feature.chroma_stft(y)
    #     tempogram = librosa.feature.tempogram(y)
    #
    #     spectral_centroid = librosa.feature.spectral_centroid(y)
    #     spectral_bandwitdh = librosa.feature.spectral_bandwidth(y)
    #     spectral_rolloff = librosa.feature.spectral_rolloff(y)
    #     spectral_contrast = librosa.feature.spectral_contrast(y)
    #     spectral_flatness = librosa.feature.spectral_flatness(y)
    #     zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    #
    #     rmse = librosa.feature.rms(y)
    #
    #     tmp = ""
    #
    #     tmp = f'{np.mean(poly_features)} {np.mean(chroma_cens)} {np.mean(chroma_cqt)} {np.mean(chroma_stft)} {np.mean(tempogram)} {np.mean(spectral_centroid)} {np.mean(spectral_bandwitdh)} {np.mean(spectral_rolloff)} {np.mean(spectral_contrast)} {np.mean(spectral_flatness)} {np.mean(zero_crossing_rate)} {np.mean(rmse)}'
    #
    #     for i in mfcc:
    #         tmp += f' {np.mean(i)}'
    #
    #     arr = tmp.split(" ");
    #     arr = [float(x) for x in arr]
    #     arr = np.array([arr])
    #     header = np.array(header)
    #     testFile = pd.DataFrame(arr, columns=header)
    #     return testFile

    def predict_au(self, file):
        # file_predict = self.feature_audio_file(file)
        result = self.model.predict(file)
        genresArr = ['classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
        return genresArr[result[0]]

