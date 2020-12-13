# -*- coding: utf-8 -*-
import os
import re
import sys
import string
from os.path import basename

PY_MODULE_PATH = "cleared_samples"
FILE_NAME = 'all_words.txt'
PATH_OF_SAMPLES = [os.path.join(PY_MODULE_PATH, file) for file in os.listdir(PY_MODULE_PATH)]

def get_txts():
    topic_dict = {}
    for path in PATH_OF_SAMPLES:
        class_name = basename(path)
        with open(os.path.join(path, FILE_NAME),'r',encoding="utf-8",errors='ignore') as f:
            words = f.readlines()
            words = [w.strip() for w in words if '\n' != w]
            topic_dict[class_name] = words
    return topic_dict

# my_dict = get_txts()