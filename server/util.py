import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None

def get_estimated_price(locations,sqft,bhk,bath):
    try:
      loc_index = __data_columns.index(locations.lower())
    except:
       loc_index=-1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    if __model:
        estimated_price = __model.predict([x])[0]
        return estimated_price
    else:
        print("Model not loaded.")
        return None
def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts......start")
    global __data_columns
    global __locations

    with open("./artifact/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations=__data_columns[3:]
    global __model
    with open("./artifact/Bengaluru_House_Data.pickle",'rb') as f:
        __model=pickle.load(f)
    print("loading saved artifacts....done")
if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st phase jp nagar',1000,3,3))
    print(get_estimated_price('1st phase jp nagar',1000,2,2))
    print(get_estimated_price('ambalipura',1000,2,2))
    print(get_estimated_price('ambedkar nagar',1000,2,2))