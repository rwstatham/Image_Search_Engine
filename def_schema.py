import os
import weaviate as wv
import base64
import shutil
from PIL import Image
from io import BytesIO
from Init_weaviate_client import *


def init_schema():
    WEAVIATE_URL = os.getenv('WEAVIATE_URL')
    if not WEAVIATE_URL:
        WEAVIATE_URL = 'http://localhost:8080'

    client = wv.Client(WEAVIATE_URL)


    animal_schema = {
        "classes": [
            {
                "class": "Animal",
                "description": "Images of different animals",
                "moduleConfig": {
                    "img2vec-neural": {
                        "imageFields": [
                            "image"
                        ]
                    }
                },
                "vectorIndexType": "hnsw", 
                "vectorizer": "img2vec-neural", # the img2vec-neural module
                "properties": [
                    {
                        "name": "animal", #what animal is depicted in the image
                        "dataType": ["string"],
                        "description": "name of dog breed",
                    },
                    {
                        "name": "image",
                        "dataType": ["blob"],
                        "description": "image",
                    },
                    {
                        "name": "filepath",
                        "dataType":["string"],
                        "description": "filepath of the images",
                    }
                ]
            }
        ]
    }

    # adding the animal image schema 
    client.schema.create(animal_schema)

    print("The schema has been defined.")

def query_image(q_image_path, q_animal_name, n_results):
    WEAVIATE_URL = os.getenv('WEAVIATE_URL')
    if not WEAVIATE_URL:
        WEAVIATE_URL = 'http://localhost:8080'

    client = wv.Client(WEAVIATE_URL)

    #read and decode query image
    with open(q_image_path, "rb") as file:
        b64_encoding = base64.b64encode(file.read()).decode('utf-8')


        response = (
            client.query
            .get("Animal", ['image', 'animal'])
            .with_near_image({'image' :b64_encoding}, encode = False)
            .with_limit(n_results)
            .do()
        )

    result_dir = "./Results"

    # check to see if results folder already exists, if it does, then delete it

    output_name = "Results"
    if os.path.exists(output_name):
        shutil.rmtree(output_name)
    
    os.mkdir(output_name)


    for i in range(n_results):
        result_b64 = response['data']['Get']["Animal"][i]
        result_b64 = result_b64['image'] #get image with that b64 representation
        result_path = f'{result_dir}/result{i}.jpg'
        result_data = base64.b64decode(result_b64)
        result_img = Image.open(BytesIO(result_data))
        result_img.save(result_path, 'JPEG')

        print("Image saved at ", result_path)


        




