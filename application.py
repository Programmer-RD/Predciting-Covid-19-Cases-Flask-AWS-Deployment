from flask import *
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
import random

application = Flask(__name__)
app = application
app.secret_key = 'RANUGA D 2008'
@application.route("/", methods=["POST", "GET"])
def home():
    model = pickle.load(open("./models/model_RandomForestRegressor.pkl", "rb"))
    flash("Models Accuracy in testing is over 62.5% the accuracy may change", "success")
    flash('DataSet : https://www.kaggle.com/imdevskp/corona-virus-report | User : https://www.kaggle.com/imdevskp | Website : https://www.kaggle.com/','info')
    if request.method == "POST":
        date = request.form["D"]
        date = date.replace("-", "")
        date = np.array([date])
        date_df = pd.DataFrame(date)
        results = model.predict(date_df.T)
        flash(
            f"Confirmed : {round(results[0][0])} | Deaths : {round(results[0][1])} | Recovered : {round(results[0][2])} | Active : {round(results[0][3])} | New Cases : {round(results[0][4])} | New Deaths : {round(results[0][5])} | New Recovered : {round(results[0][6])}",
            "info",
        )
        flash('Note that these predictions are for the whole world not for a specific country. - These predictions may differ for different reasons.','danger')
        return redirect("/")
    else:
        return render_template("./home.html")
if __name__ == "__main__":
    app.run()
