import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from dense_neural_class import *
import pickle
import os

def load_model(filename):
    # Gets the current directory where the script is being executed
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Constructs the full path of the .pkl file
    filepath = os.path.join(current_dir, filename + '.pkl')
    
    with open(filepath, 'rb') as file:
        model_loaded = pickle.load(file)
    
    return model_loaded


model = load_model('model')

class DATA(BaseModel):
    vec:list

app = FastAPI()

@app.post("/predict")
def get_prediction(data:DATA):
    print(data)
    print(f"Received vector of length: {len(data.vec)}")
    prediction = model.predict(data.vec)[0]
    print(f"Model Prediction: {prediction}")
    return {"prediction": str(prediction)}
    
uvicorn.run(app, host="0.0.0.0", port=8080)