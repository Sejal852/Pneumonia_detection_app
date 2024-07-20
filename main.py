
# importing the necessary tools
from flask import Flask, render_template, request,redirect, url_for, session
# to let flask interact easily while performing file and folder processes irrespective of operating system
import os
import sys
# load the model using joblib
import joblib
import numpy as np
# Keras

from tensorflow.python.keras.models import load_model
from keras_preprocessing import image

# Flask utils

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
# root directory
webroot = 'src'
static_dir = os.path.join(webroot,'static')
template_dir = os.path.join(webroot,'templates')
# defining the flask app
app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

# load pneumonia model path
PNEUMONIA_MODEL_PATH = 'pneumonia_model.h5'

model = load_model(PNEUMONIA_MODEL_PATH)
def pneumonia_predict(img_path, model):
    img = image.load_img(img_path, target_size=(64, 64)) #target_size must agree with what the trained model expects
    # Preprocessing the image
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    return preds

@app.route('/',methods=['GET','POST'])
def pneumonia():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
        basepath, '', secure_filename(f.filename))
        f.save(file_path)
        # Make prediction
        preds = pneumonia_predict(file_path, model)
        os.remove(file_path)
        if preds == 1:
            res = "Sorry :( you have got the chances of Pneumonia"
        else:
            res = "Congratulations! you are safe from Pneumonia"
        return render_template('pneumonia.html',prediction=res)

    return render_template('pneumonia.html')


port = int(os.environ.get("PORT", 5000))

if __name__=="__main__":
    
    app.run(debug=True,port=port,host="0.0.0.0")