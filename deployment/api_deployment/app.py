from flask import Flask,request, jsonify
import pandas as pd
from joblib import dump,load

# files were created in model traning csv file
regressor = load('api_deployment\house_price_prediction.joblib')
Std_Scaler = load('api_deployment\house_price_prediction_Std_Scaler.joblib')


def getprice(client_data):
    df = pd.DataFrame([client_data])
    df["Living area"] = Std_Scaler.transform(df[["Living area"]])
    price = regressor.predict(df)
    return price[0]# first element in list
# following two used as test 
# dict={"bedroom_count":2,"Living area":100,"Bathrooms":1,"Garden":1,	"Basement":1,"Furnished":0}
# getprice(dict)



app = Flask(__name__)

@app.route('/',methods=["POST",'GET'])
def home():
    
    input_data=request.get_json(force=True)
    price = getprice(input_data)
    price = price.round(0)# rounding the price
    return {"price":price}# returning list as dict
   
if __name__ == '__main__':
    app.run(debug=True, port =5000)

