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
application.secret_key = "Ranuga D 2008"
application.debug = True


@application.route("/", methods=["POST", "GET"])
def home():
    random_choice = random.choice([1, 2, 3])
    if random_choice == 1:
        model = pickle.load(open("./models/model_BaggingRegressor.pkl", "rb"))
    elif random_choice == 2:
        model = pickle.load(open("./models/model_KNeighborsRegressor.pkl", "rb"))
    else:
        model = pickle.load(open("./models/model_RandomForestRegressor.pkl", "rb"))
    flash("Models Accuracy in testing is over 62.5%", "success")
    flash('DataSet : https://www.kaggle.com/imdevskp/corona-virus-report | User : https://www.kaggle.com/imdevskp | Website : https://www.kaggle.com/','info')
    if request.method == "POST":
        date = request.form["D"]
        date = date.replace("-", "")
        date = np.array([date])
        date_df = pd.DataFrame(date)
        print(date_df)
        results = model.predict(date_df.T)
        flash(
            f"Confirmed : {results[0][0]} | Deaths : {results[0][1]} | Recovered : {results[0][2]} | Active : {results[0][3]} | New Cases : {results[0][4]} | New Deaths : {results[0][5]} | New Recovered : {results[0][6]}",
            "info",
        )
        flash('Note that these predictions are for the whole world not for a specific country. - These predictions may differ for different reasons.','danger')
        return redirect("/")
    else:
        return render_template("home.html")
