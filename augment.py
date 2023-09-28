

import matplotlib.image as img
import matplotlib.pyplot as plt
import PIL.Image as Image
import pathlib, os, random
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib.pyplot import imread



gen = ImageDataGenerator(rotation_range = 90, width_shift_range=0.1,height_shift_range =0.1, shear_range = 0.15, zoom_range=0.1,channel_shift_range=20.,horizontal_flip = True, vertical_flip = True)


os.mkdir("train_new/")



for image_folder in os.listdir('indian_food/'):
    if '.' not in image_folder:
        folder_image = 'indian_food/'+image_folder
        save_here = 'train_new/'+image_folder
        os.mkdir(save_here)
        for image_path in os.listdir(folder_image):
            image_path_new = folder_image+'/'+image_path

            im = Image.open(image_path_new)
            if 'png' in image_path:
                rgb_im = im.convert('RGB')
                rgb_im.save(save_here+'/'+image_path.replace('png','jpg'))
                image_path = image_path.replace('png','jpg')
            else:
                im.save(save_here+'/'+image_path)
            
        #os.remove(image_path)
        ## Save Image to new path 
       
        
        
            

            
        ## https://stackoverflow.com/questions/47826730/how-to-save-resized-images-using-imagedatagenerator-and-flow-from-directory-in-k    
            image = np.expand_dims(imread(save_here+'/'+image_path), 0)


            for x , val in zip(gen.flow(image,save_to_dir=save_here,save_prefix='aug',save_format='jpg'),range(5)):

                pass
    