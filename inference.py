import tensorflow as tf
from tensorflow import keras
import numpy as np
#from keras.preprocessing import image

from model import model_def

import pandas as pd


import json

from tensorflow.keras.utils import load_img, img_to_array


def infer(img):


    indian_food_final = pd.read_csv('indian_food_final.csv')


    img_width, img_height = 224, 224
    img = load_img(img, target_size = (img_width, img_height))
    img = img_to_array(img)
    img = np.expand_dims(img, axis = 0)/255.
    

    model = model_def()

    
    model.load_weights("training_1/cp.ckpt")

    predicted_vector = model.predict(img,use_multiprocessing=True)

    

    ## Convert the vector to list

    predicted_vector_list = predicted_vector.tolist()



    predicted_vector_list = sum(predicted_vector_list,[])

    ### Getting top 5 indices

    def sort_index(lst, rev=True):
        index = range(len(lst))
        s = sorted(index, reverse=rev, key=lambda i: lst[i])
        return s


    top_three = sort_index(predicted_vector_list)[:5]

    print(top_three)
    with open('class_mappings.json') as json_file:
        data = json.load(json_file)

    data = {y: x for x, y in data.items()}



    #### the top five predictions

    list_of_predictions = []

    list_of_prep_times  = []

    list_of_regions = []

    list_of_ingredients= []

    for index in top_three:

        list_of_predictions.append(data[index])

        prep_time = indian_food_final[indian_food_final['name']==data[index]]['prep_time'].iloc[0]


        list_of_prep_times.append(prep_time)

        region = indian_food_final[indian_food_final['name']==data[index]]['region'].iloc[0]

        list_of_regions.append(region)

        ingredients = indian_food_final[indian_food_final['name']==data[index]]['ingredients'].iloc[0]

        list_of_ingredients.append(ingredients)



    ##### return predictions, prep times, list of regions and ingredients



    top_three_values_prediction = sorted(predicted_vector_list,reverse=True)[:5]



    return(list_of_predictions,list_of_prep_times,list_of_regions,list_of_ingredients,top_three_values_prediction)















