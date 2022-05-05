# Bollywood-Celebrity-Look-Alike-App-Deployment 
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg)](https://www.kaggle.com/datasets/sushilyadav1998/bollywood-celeb-localized-face-dataset) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

The demo will take an image and detects all faces in it. If a face is found then it will indentify which celebrity looks the face most closely. The demo will display the resulting celebrity with his image and name along with the uploaded image.

### Dataset
You can find the dataset [here.](https://www.kaggle.com/datasets/sushilyadav1998/bollywood-celeb-localized-face-dataset)

• This repository consists of files required for end to end implementation of Bollywood Celebrity Look Alike ___Machine Learning Web App___ created with ___Streamlit___ on ___Heroku___ platform.

## setup
- Clone the repository : https://github.com/ni3choudhary/Bollywood-Celebrity-Look-Alike-App-Deployment.git
- Inside the project root directory, Create Python Virtual Environment and activate it using below commands 
```console
$ python3 -m venv env
``` 

Activate Virtual Environment
```console
$ .env/bin/activate 
          OR
$ .\env\Scripts\activate
```
Install Libraries using below command
```console
$ pip install -r requirements.txt
```
I have tried to add some more actors images into the original data. For this we need to run some python file to get those data into the format we want.

## The Files explained
Use the files as following to create the demo from scratch or create your own demo in an adapted way.

* **1.** First create a **data** folder and combine all the three dataset folder downloded from kaggle.

* **2. scraper.py** to scrape for some more bollywood celebrity images which will give you a celebrity list pickle file.

* **3. data_downloader.py** to download the images which are not present in kaggle dataset.

* **4. rename_files.py** to rename the files in one format.

* **5. face_crop_mtcnn.py to only get the faces from the freshly downloaded images from data_downloader.py file.

* **6. actors_filenames_extractor.py to extract filenames from all the sub-directory present in data directory.

* **7. feature_extractor.py to create embeddings for all faces present in data directory.

- Now run app.py on terminal to start local server.
```console
$ streamlit run app.py
```

• Please do ⭐ the repository, if it helped you in anyway.


