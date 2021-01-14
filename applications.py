from flask import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
import random

application = Flask(__name__)
app = application
@application.route("/", methods=["POST", "GET"])
def home():    
    return "Please work"
