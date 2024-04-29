import os, re
import weaviate as wv
import base64



def clear_animals():
    """
    used if we want to clear the animals collection
    useful if we want to clear and repopulate with diff pictures
    """
    WEAVIATE_URL = os.getenv('WEAVIATE_URL')
    if not WEAVIATE_URL:
        WEAVIATE_URL = 'http://localhost:8080'

    client = wv.Client(WEAVIATE_URL)

    with client.batch as batch:
        batch.delete_objects(
            class_name = "animal",
            where = {
                "operator" : "NotEqual",
                "path" : ["animal"],
                "valueString": "x"
            },
            output = "verbose",
        )

def import_data():
    WEAVIATE_URL = os.getenv('WEAVIATE_URL')
    if not WEAVIATE_URL:
        WEAVIATE_URL = 'http://localhost:8080'

    client = wv.Client(WEAVIATE_URL)

    with client.batch as batch:
        # Iterate over all images
        image_path = "./Images/"
        for file_path in os.listdir(image_path):
            with open("./Images/" + file_path, "rb") as file:
                b64_encoding = base64.b64encode(file.read()).decode('utf-8')

            # remove image file extension and swap - for " " to get the animal name
            animal = re.sub(".(jpg|jpeg|png)", "", file_path).split("-")[0]
            animal = animal.replace("_", " ")
            # The properties from our schema
            data_properties = {
                "animal": animal,
                "image": b64_encoding,
                "filepath": file_path,
            }

            batch.add_data_object(data_properties, "Animal")
    print("Images imported successfully.")

