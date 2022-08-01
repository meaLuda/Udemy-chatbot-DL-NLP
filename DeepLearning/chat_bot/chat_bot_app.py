# UTF-8
import numpy as np
# import tensorflow as tf
import re
import time

print("testing testing")

###### ----------------1. DATA PREPROCESSING ----------------------
lines = open(r'C:\Users\munya\Desktop\Projects\Udemy-chatbot-DL-NLP\DeepLearning\chat_bot\data\movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open(r'C:\Users\munya\Desktop\Projects\Udemy-chatbot-DL-NLP\DeepLearning\chat_bot\data\movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

###### -------------- Creating a dictionary to map line and id------------------
id_to_line = {}

for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id_to_line[_line[0]] = _line[4]

print("First 100 keys:\n",list(id_to_line.keys())[:100])
print("\nLast 100 keys:\n",list(id_to_line.keys())[-100:])
print("\n \n")
print("First 10 Movie lines:\n",list(id_to_line.values())[:10])
print("\nLast 10 Movie lines:\n",list(id_to_line.values())[-10:])