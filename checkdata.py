from lib2to3.pgen2.pgen import DFAState
import numpy as np
import pandas as pd
from collections import Counter
from numpy.random import shuffle
import cv2

train_data = np.load('new_train_data.npy',allow_pickle=True)