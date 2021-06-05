from fastapi import FastAPI, APIRouter, UploadFile, File,  Request
from audio_model import AudioModel
from pydantic import BaseModel
import librosa
import pandas as pd #processing csv files
import numpy as np
from typing import List
from fastapi.staticfiles import StaticFiles

import shutil
router = APIRouter(prefix="/audio")

model = AudioModel()



app = FastAPI()


class Response(BaseModel):
    class_name: str
    # arr: List[float]

async def feature_audio_file(file_path):
        header = 'poly_features chroma_cens chroma_cqt chroma_stft tempogram spectral_centroid spectral_bandwidth spectral_rolloff spectral_contrast spectral_flatness zero_crossing_rate rmse'
        for i in range(1, 31):
            header += f' mfcc{i}'
        header = header.split(" ");

        y, sr = librosa.load(file_path, sr=22050)

        mfcc = librosa.feature.mfcc(y, n_mfcc=30)
        poly_features = librosa.feature.poly_features(y)
        chroma_cens = librosa.feature.chroma_cens(y)
        chroma_cqt = librosa.feature.chroma_cqt(y)
        chroma_stft = librosa.feature.chroma_stft(y)
        tempogram = librosa.feature.tempogram(y)

        spectral_centroid = librosa.feature.spectral_centroid(y)
        spectral_bandwitdh = librosa.feature.spectral_bandwidth(y)
        spectral_rolloff = librosa.feature.spectral_rolloff(y)
        spectral_contrast = librosa.feature.spectral_contrast(y)
        spectral_flatness = librosa.feature.spectral_flatness(y)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)

        rmse = librosa.feature.rms(y)

        tmp = ""

        tmp = f'{np.mean(poly_features)} {np.mean(chroma_cens)} {np.mean(chroma_cqt)} {np.mean(chroma_stft)} {np.mean(tempogram)} {np.mean(spectral_centroid)} {np.mean(spectral_bandwitdh)} {np.mean(spectral_rolloff)} {np.mean(spectral_contrast)} {np.mean(spectral_flatness)} {np.mean(zero_crossing_rate)} {np.mean(rmse)}'

        for i in mfcc:
            tmp += f' {np.mean(i)}'

        arr = tmp.split(" ");
        arr = [float(x) for x in arr]
        arr = np.array([arr])
        return arr


@router.post("/", response_model=Response)
async def audio(request: Request, file_audio: UploadFile = File(...)):
    print(file_audio)
    with open(f'{file_audio.filename}','wb') as buffer:
        shutil.copyfileobj(file_audio.file,buffer)
    file_name = file_audio.filename
    file_feature = await feature_audio_file(file_name)

    class_name = model.predict_au(file_feature)
    # class_name = 'pop'
    return {"class_name": class_name}