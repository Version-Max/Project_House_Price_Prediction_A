import json
import pickle
import numpy as np

# Variable:
df_columns = None
locations = None
model = None


# Price Predict funtion:
def Price_Predict(locationOut, SqFt, Bath, Bed):
    locationsIn = locationOut.lower()
    location_index = df_columns.index(locationsIn)
    SqFt = float(SqFt)
    Bath = int(Bath)
    Bed = int(Bed)
    print('\n\n [2]Price predict called from utilities')
    print(SqFt)
    print(Bath)
    print(Bed)
    print(location_index)
    size = len(df_columns)
    x = np.zeros(size)
    x[0] = Bath
    x[1] = Bed
    x[2] = SqFt
    x[location_index] = 1

    price = model.predict([x])[0]  # 2d array converted to 1D
    print('Price is: ')
    price = price.round(2)
    price = float(price)
    print(price)
    return price


# Dummy function: START ---
def ask(Belt, Bad):
    Belt = int(Belt)
    Bad = int(Bad)
    print(Belt)
    print(Bad)
    print(" <- Bed number.")
    total = Belt + Bad
    return total
# Dummy END ---


''' Dummy function: START --- [Works for Sure]
def ask(Belt, Bad):
    Belt = int(Belt)
    Bad = int(Bad)
    print(Belt)
    print(Bad)
    print(" <- Bed number.")
    total = Belt + Bad
    return total
# Dummy END --- '''

def location_names():
    return locations


def load__model_and_column_names():
    global locations
    global df_columns
    global model
    # Get column names
    with open('Column_Names.json', 'r') as L:
        df_columns = json.load(L)['Columns']  # ['Columns'] is the key name in the Column_Names.json file
        locations = df_columns[3:]

    # Get model
    with open('Price_prediction_banglore_homes_in_USD', 'rb') as L:
        model = pickle.load(L)
        print('Model loaded')


if __name__ == 'utilities':
    load__model_and_column_names()
    print('\n\n[1] Location names are \n\n:', location_names())
    print('\n\n[2] The price is: ', Price_Predict('1st Phase JP Nagar', 1000, 2, 2))
