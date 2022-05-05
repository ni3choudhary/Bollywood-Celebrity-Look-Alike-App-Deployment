# Importing Required Libraries
import os
import pickle
import numpy as np
import cv2
from PIL import Image
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from mtcnn import MTCNN
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st 

import warnings
warnings.filterwarnings('ignore')

# Initialise MTCNN detector for face detection
detector = MTCNN()

# Load the Model
model = VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg')

# Load Features list from pickle file
feature_list = pickle.load(open('embedding.pkl','rb'))
# Load actors filenames from pickle file
actors_filenames = pickle.load(open('actors_filenames.pkl','rb'))

# function to upload a file into uploads folder 
def save_uploaded_image(uploaded_image):
    try:
        with open(os.path.join('uploads',uploaded_image.name),'wb') as f:
            f.write(uploaded_image.getbuffer())
        return True
    except:
        return False

# This Function extract features from the image
def extract_features(image_path,model,detector):
    # read image 
    image = cv2.imread(image_path)
    results = detector.detect_faces(image)

    x, y, width, height = results[0]['box']

    face_cropped = image[y:y + height, x:x + width]

    #  extract its features
    face_image = Image.fromarray(face_cropped)
    face_image = face_image.resize((224, 224))

    face_array = np.asarray(face_image)
    face_array = face_array.astype('float32')

    expanded_img = np.expand_dims(face_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img)
    result = model.predict(preprocessed_img).flatten()
    return result

def recommend(feature_list,features):
    similarity = []
    for i in range(len(feature_list)):
        similarity.append(cosine_similarity(features.reshape(1, -1), feature_list[i].reshape(1, -1))[0][0])

    index_position = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[0][0]
    return index_position

# Streamlit app
st.title('Bollywood Celebrity Look alike App')

uploaded_image = st.file_uploader('Choose an image')

if uploaded_image is not None:
    # save the image in a directory
    if save_uploaded_image(uploaded_image):
        # load the image
        display_image = Image.open(uploaded_image)

        # extract the features
        features = extract_features(os.path.join('uploads',uploaded_image.name),model,detector)
        # recommend
        index_position = recommend(feature_list,features)
        predicted_actor = " ".join(actors_filenames[index_position].split('\\')[1].split('_'))
        # display
        col1, col2 = st.columns(2)

        with col1:
            st.header('Your uploaded image')
            st.image(display_image)
        with col2:
            st.header("Looks like " + predicted_actor)
            st.image(actors_filenames[index_position],width=300)




