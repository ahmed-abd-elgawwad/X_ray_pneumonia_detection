from flask import Flask,render_template,request
from keras.preprocessing.image import load_img,img_to_array
import keras 
import numpy as np
import os

# the model
model= keras.models.load_model("model")
app=Flask(__name__)
@app.route("/",methods=["GET"])
async def home_page():
   return  render_template('home.html')

@app.route("/",methods=["POST"])
async def predict():
    image = request.files['imagefile']
    # first remove the old images so that it doesn't take memory 
  
    old_images = os.listdir("./static/images")
    if old_images:
        for file in old_images :
                os.remove(f"./static/images/{file}")
    if image:
        
        image_name= image.filename
        #check if the uploaded file is an image
        if image_name.split(".")[-1] in ["jpg","jpeg","png"]:
            global path
            # full path to the image
            path= "./static/images/"+image_name
            #save the image
            image.save(path)
            # load the image after saving with image resizing for the model input
            img=load_img(path,target_size=(256,256))
            # convert into array and reshape as the model only accept batch 4D
            img=img_to_array(img).reshape(1,256,256,3)
            classes=['NORMAL', 'baterial pneumonia', 'virus pneumonia']
            # predict the image
            prediction= model.predict(img)
            # set the accuray
            acc=str(round(np.max(prediction)*100,2))+" %"
            # get the predicted class
            predicted_class= classes[np.argmax(prediction)]
            # remove the image form image folder 
            
            return render_template('home.html',image_path=path,classname=predicted_class,accuracy=acc)
        else:
            return render_template('home.html',image_path="Not_image",classname=None,accuracy=None)
        
    else:
        return render_template('home.html',image_path=None,classname=None,accuracy=None)
    
    
if __name__=="__main__":
    app.run(debug=True,port=3000)