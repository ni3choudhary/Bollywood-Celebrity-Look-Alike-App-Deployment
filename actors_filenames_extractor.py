# Importing Required Libraries
import os
import pickle

# list data directory
actors = os.listdir('data')

# Extracting filenames from all the sub-directory present in data directory
filenames = []
for actor in actors:
    for file in os.listdir(os.path.join('data',actor)):
        filenames.append(os.path.join('data',actor,file))

# Dump all the actors filenames
pickle.dump(filenames,open('actors_filenames.pkl','wb'))