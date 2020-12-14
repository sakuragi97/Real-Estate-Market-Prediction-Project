import json
import pickle
import numpy as np

__columns = None
__locations = None
__model = None


def getLocationNames():
    loadArtifacts()
    return __locations


def loadArtifacts():
    print('Loading artifacts...')
    global __columns
    global __locations
    global __model
    with open('./artifacts/columns.json', 'r') as f:
        __columns = json.load(f)['data_columns']
    __locations = __columns[3:]
    with open('artifacts/Bengaluru_House_Data_Model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('Loading artifacts Done!')


def getEstimatedPrice(location, sqmeter, bath, bhk):
    try:
        loc_index = __columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__columns))
    x[0] = bhk
    x[1] = sqmeter
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    predictResult = round(__model.predict([x])[0], 2)
    if predictResult < 0:
        return "No such data is given"
    return predictResult


if __name__ == '__main__':
    print(getLocationNames())
    print(getEstimatedPrice('1st Phase JP Nagar', 100, 2, 2))
    print(getEstimatedPrice('1st Phase JP Nagar', 100, 2, 3))
    print(getEstimatedPrice('1st Phase JP Nagar', 120, 2, 4))
    print(getEstimatedPrice('Whitefield', 160, 3, 4))
