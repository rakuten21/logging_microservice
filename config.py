import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')

    # api key from random.org
    API_KEY = os.getenv('API_KEY', 'f941797d-302d-4f1e-a7c8-403018a27ac3')
