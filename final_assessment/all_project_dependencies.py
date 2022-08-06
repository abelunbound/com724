### make sure to import this python file to all other modules in the program
### user should pip install tensorflow; keras depends on it

import math
from sklearn import preprocessing
from sklearn import metrics
import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Activation, Dense
from keras.layers import LSTM
from matplotlib import pyplot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import io
from datetime import datetime, timedelta
import re
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from math import sqrt
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score