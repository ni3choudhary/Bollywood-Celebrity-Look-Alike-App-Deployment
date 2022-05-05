# Importing Required Libraries
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
import numpy as np
import pickle
from tqdm import tqdm

# Load the actors filenames from pickle file
filenames = pickle.load(open('actors_filenames.pkl','rb'))

# Load the Model
model = VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg')

def feature_extractor(img_path, model):
    '''
    This Function belongs to extract features from the image
    '''
    img = load_img(img_path, target_size = (224,224))
    img_array = img_to_array(img)
    expanded_img = np.expand_dims(img_array,axis=0)
    preprocessed_img = preprocess_input(expanded_img)

    result = model.predict(preprocessed_img).flatten()

    return result


# Extract Features for all the images present in data directory
features = []

for file in tqdm(filenames):
    features.append(feature_extractor(file,model))

pickle.dump(features,open('embedding.pkl','wb'))