import requests
import numpy as np
from os import walk, listdir
from os.path import isfile, join


def get_encoded_vectors(url, edges):
    resp = requests.get(f'{url}/{edges}/')
    embed = resp.json()
    return embed


def load_test_files(test_path = 'test_data'):
    #Load all test file names
    # Load all test sets embedding and construct projection space
    fnames = []
    test_dirs = listdir(test_path)
    for tdirs in test_dirs:
        fnames.extend([join(test_path, tdirs, f) for f in listdir(join(test_path, tdirs))])
    
    embeds = []
    for embed in fnames:
        embeds.append(np.load(embed))
    
    return fnames, embeds