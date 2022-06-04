## X_ray Pneumonia Classification
![classification](https://i.imgur.com/jZqpV51.png)
 * Using open source image dataset from kaggle [DataSet_link](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) the data is classified into two main classes
    * Normal 
    * Pneumonia
 * Extract the Pneumonia classes `Viral/Bacterial` we made the data of **Three classes**
    * Normal 
    * Viral pneumonia
    * Bacterial pneumonia 
 * Using the **Transfer learning** aproach , we used **Xception Model** with the pre_trained weights of the **Imagenet** and allow only the last few layers to be trained
 ---
### Model Performance:
* the model trained over nearlly 40 epochs and reached `100%` accuracy on the both **Test/Train/Val Sets** which is somthing wierd 😂.
---
### Model deployment :
* The deployment is done using **Flask** with simple UI that take the image and predict the class.

