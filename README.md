# X_ray_pneumonia_detection
- flask application that takes your x_ray images and predict weather you have pneumonia [baterial or viral ] or not[ normal ]
## Model description 
- using `Transfer learning` we trained a pretrained model `Xception model` on our images changing the last few layers for the case of this problem 
- classification with `three classes` [ bacterial pneumonia , viral pneumonia , normal person ]
## Model performance 
- the model showed nearly `100%` accuracy on the `Test images` 
- all what i did about the model is in the file `model_building_and_training` you can check it.
