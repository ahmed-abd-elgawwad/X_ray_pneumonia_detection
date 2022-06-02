import keras
import tensorflow as tf
# define the model without it top dense layers 
input_model = tf.keras.applications.Xception(weights="imagenet", include_top=False, input_tensor=keras.layers.Input(shape=(256, 256,3)))
# build the VGG16 model as input of the new model
x = input_model.output
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dense(3, activation="softmax")(x)

model = keras.models.Model(inputs=input_model.input, outputs=x)

# compile the model
# compile the model 
model.compile(
              optimizer="adam",
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics = ['accuracy']
)
model.load_weights("best_weights_2 (3).h5")
model.save("Model")
                           