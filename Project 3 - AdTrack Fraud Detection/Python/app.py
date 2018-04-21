from sklearn import tree
from sklearn.model_selection import train_test_split

from flask import Flask, jsonify, render_template, request, url_for

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)

conn = pymysql.connect(host='35.197.105.177',
                             user='root',
                             password='kaggleuci123',
                             db='kaggleDB')

#query = ("select * from train_sample_cleaned;")
#trainDF = pd.read_sql(query, conn)

@app.route("/")
def index():
	return render_template("index2.html")

###################################################################################################################
#-----DECISION TREE-----
###################################################################################################################
@app.route("/dt")
def decisionTree():
	dtOS = pd.read_sql("SELECT * FROM kaggleDB.dtOS;", conn)
	dtOS = dtOS.to_dict(orient="records")

	dtDevice = pd.read_sql("SELECT * FROM kaggleDB.dtDevice;", conn)
	dtDevice = dtDevice.to_dict(orient="records")

	dtTOD = pd.read_sql("SELECT * FROM kaggleDB.dtTOD;", conn)
	dtTOD = dtTOD.to_dict(orient="records")

	dtDOW = pd.read_sql("SELECT * FROM kaggleDB.dtDOW;", conn)
	dtDOW = dtDOW.to_dict(orient="records")

	dtFinal = []
	dtFinal.append(dtOS)
	dtFinal.append(dtDevice)
	dtFinal.append(dtTOD)
	dtFinal.append(dtDOW)

	return jsonify(dtFinal)

###################################################################################################################
#-----RANDOM FOREST-----
###################################################################################################################
@app.route("/rf")
def randomForest():
	rfOS = pd.read_sql("SELECT * FROM kaggleDB.rfOS;", conn)
	rfOS = rfOS.to_dict(orient="records")

	rfDevice = pd.read_sql("SELECT * FROM kaggleDB.rfDevice;", conn)
	rfDevice = rfDevice.to_dict(orient="records")

	rfTOD = pd.read_sql("SELECT * FROM kaggleDB.rfTOD;", conn)
	rfTOD = rfTOD.to_dict(orient="records")

	rfDOW = pd.read_sql("SELECT * FROM kaggleDB.rfDOW;", conn)
	rfDOW = rfDOW.to_dict(orient="records")

	rfFinal = []
	rfFinal.append(rfOS)
	rfFinal.append(rfDevice)
	rfFinal.append(rfTOD)
	rfFinal.append(rfDOW)

	return jsonify(rfFinal)



@app.route("/tf")
def tensorflow():
	tfOS = pd.read_sql("SELECT * FROM kaggleDB.tfOS;", conn)
	tfOS = tfOS.to_dict(orient="records")

	tfDevice = pd.read_sql("SELECT * FROM kaggleDB.tfDevice;", conn)
	tfDevice = tfDevice.to_dict(orient="records")

	tfTOD = pd.read_sql("SELECT * FROM kaggleDB.tfTOD;", conn)
	tfTOD = tfTOD.to_dict(orient="records")

	tfDOW = pd.read_sql("SELECT * FROM kaggleDB.tfDOW;", conn)
	tfDOW = tfDOW.to_dict(orient="records")

	tfFinal = []
	tfFinal.append(tfOS)
	tfFinal.append(tfDevice)
	tfFinal.append(tfTOD)
	tfFinal.append(tfDOW)

	return jsonify(tfFinal)

@app.route("/KnowYourData")
def KnowYourData():
	return render_template("KnowYourData.html")


@app.route("/tensorflow")
def tensorflow2():
    """Return the dashboard homepage."""
    return render_template("index.html", sample_names= [TF1000e2m, TF2000e2m])#, knowingourdata])

@app.route('/TF1000e2m')
def TF1000e2m():
    query = ("select * from TF_1000E2mm_results;")
    df_1000e2m = pd.read_sql(query, conn)
    df_1000e2m_dict = df_1000e2m.to_dict('records')
    return jsonify(df_1000e2m_dict)

@app.route('/TF2000e2m')
def TF2000e2m():
    query = ("select * from TF2000e2m_results;")
    df_2000e2m = pd.read_sql(query, conn)
    df_2000e2m_dict = df_2000e2m.to_dict('records')
    return jsonify(df_2000e2m_dict)

@app.route('/tf_epoch_results1000.html')
def tf_epoch_results1000():
    return render_template('tf_epoch_results1000.html')

@app.route('/tf_epoch_results2000.html')
def tf_epoch_results2000():
    return render_template('tf_epoch_results2000.html')


if __name__ == "__main__":
    app.run(debug=True)