from model import model_def

import json

from keras.preprocessing.image import ImageDataGenerator

import tensorflow as tf

from tensorflow import keras


model = model_def()

# for layer in base_model.layers:
#     layer.trainable = False



datagen = ImageDataGenerator(rescale = 1/255., validation_split = 0.1)
batch_size = 128
img_height = 224
img_width = 224


train_data = datagen.flow_from_directory('train_new/', class_mode='sparse', target_size=(img_height, img_width), batch_size=batch_size, shuffle = True, seed=42,subset='training')
val_data = datagen.flow_from_directory('train_new/',class_mode='sparse', target_size=(img_height, img_width), batch_size=batch_size, 
                                       shuffle=True, seed=42,subset='validation')


class_mappings = train_data.class_indices


with open("class_mappings.json", "w") as fp:
    json.dump(class_mappings , fp) 


model.load_weights("training_1/cp.ckpt")





# print(val_data.class_indices)

# print(val_data.class_indices == train_data.class_indices)

# exit()

import os

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
# keras.optimizers.Adam(learning_rate=0.0003)

model.compile(loss = keras.losses.SparseCategoricalCrossentropy(),optimizer=keras.optimizers.Adam(learning_rate = 0.0003),metrics = [tf.keras.metrics.SparseCategoricalAccuracy()])

history = model.fit(train_data,epochs = 25,validation_data = val_data,callbacks=[cp_callback])




# # Loads the weights
# model.load_weights(checkpoint_path)

# # Re-evaluate the model
# loss, acc = model.evaluate(test_images, test_labels, verbose=2)
# print("Restored model, accuracy: {:5.2f}%".format(100 * acc))
