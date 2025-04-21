import requests
import io
from fastapi import HTTPException
from config import config

async def get_prediction(image_bytes: bytes):
    try:
        print('roboflow кошулду')
        url = config.MONGODB_URL
        files ={
            'file': ('image.jpg', io.BytesIO(image_bytes), 'image/jpg')
        }
        response = requests.post(url, files = files)

        print(response.text)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail='ошибка')

        return {
            'answer': response.json()['inference_id'],
            'result_tame': response.json()['time'],
            'class': response.json()['predictions'][0]['class'],
            'confidence': round(response.json()['predictions'][0]['confidence']*100,1)
                }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

