# Importing Required Libraries
import pickle
import os
from bing_image_downloader import downloader

celebrity_list = pickle.load(open('celebrities_name.pkl','rb'))
celebrity_list = [celeb.strip() for celeb in celebrity_list]

actors = os.listdir('data')
actors = [ " ".join(actor.split('_')) for actor in actors ]


download_actors = [celeb for celeb in celebrity_list if celeb not in actors ]

duplicate_actors = ['Kareena Kapoor Khan','Aishwarya Rai Bachchan',\
                    'Priyanka Chopra Jonas','Sonam Kapoor Ahuja','Yami Gautam Dhar',
                    'Ileana D’Cruz','Nushrratt Bharuccha','Richa Chadha']

download_bing_actors = [celeb for celeb in download_actors if celeb not in duplicate_actors ]

downloaded_actors_images = ['Fatima_Sana_Shaikh', 'Imran_Khan', 'Mithun_Chakraborty',\
                            'Rajinikanth', 'Anupam_Kher', 'Diljit_Dosanjh',\
                            'Aditya_Roy_Kapur']

for actor in download_bing_actors:
    downloader.download(actor, limit=100,  output_dir='data', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

pickle.dump(downloaded_actors_images, open('downloaded_actors_images.pkl','wb'))


