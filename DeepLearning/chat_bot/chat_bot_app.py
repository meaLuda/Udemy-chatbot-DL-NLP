# UTF-8
import numpy as np
import tensorflow as tf
import re
import time

print("testing testing")

###### ----------------1. DATA PREPROCESSING ----------------------
lines = open('/home/eliudluda/Desktop/DataScience/Udemy_tut/DeepLearning/chat_bot/data/movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open('/home/eliudluda/Desktop/DataScience/Udemy_tut/DeepLearning/chat_bot/data/movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

###### -------------- Creating a dictionary to map line and id------------------
id_to_line = {}

for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id_to_line[_line[0]] = _line[4]

print(id_to_line)