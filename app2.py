import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('my_cnn_model_rice.h5')

def process_image(img):
    img=img.resize((64, 64)) #boyutu 170 x 170 olarak belirlendi
    img=np.array(img)
    img=img/255.0 #normalize
    img=np.expand_dims(img,axis=0)
    return img



st.title("Prinç Türlerini Sınıflandırma :ear_of_rice: :rice: ")
st.write("Resmi seç ve model princin türünü tahmin etsin")

file=st.file_uploader("Bir Resim Seç",type=['jpg','jpeg','png'])

if file is not None:
    img=Image.open(file)
    st.image(img,caption='Yüklenen Resim')
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

    class_names=['Arborio','Basmati','Ipsala','Jasmine','Karacadag']
    st.write(class_names[predicted_class])