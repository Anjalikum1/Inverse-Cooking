import pandas as pd

import json

indian_food_info = pd.read_csv('indian_food_details/indian_food.csv')


indian_food_info['name'] = indian_food_info['name'].str.lower()

indian_food_info['name'] = indian_food_info['name'].str.replace(' ','_')


with open('class_mappings.json') as json_file:
        data = json.load(json_file)

data = {y: x for x, y in data.items()}


indian_food_info.loc[len(indian_food_info.index)] =  ['dal_makhani','lentil daal, water, tomato puree,salt, capsicum, garam masala,turmeric,oil,cumin seeds,onion','vegetarian',100,60,'spicy','main','Punjab','North']


    
    
for i in data.values():
    if i in indian_food_info['name'].tolist():
        pass
    else:
        
        print(i , 'is not present in indian_food_info')
        # dal_makhani is not present in indian_food_info
        
        
indian_food_final = indian_food_info[['name','prep_time','state','region','ingredients']]

indian_food_final.loc[indian_food_final['prep_time']  == -1, 'prep_time'] = 15


# print(indian_food_final[indian_food_final['name']=='dal_makhani']['prep_time'].iloc[0])

indian_food_final.to_csv('indian_food_final.csv',index = False)







#print(indian_food_info.head())