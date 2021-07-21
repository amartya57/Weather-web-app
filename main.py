import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

app=Flask(__name__)

weather_def={
            'city':'CITY',
            'temperature': 'TEMPERATURE',
            'description': 'WEATHER DESCRIPTION',
            'icon':'01d',
        }


@app.route('/', methods=['GET','POST'])
def index():
    if(request.method=="POST"):
        city=request.form.get("city")

        url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

        appid='38d97f59b8ccd6b1215001f60b844299'
        appid2='271d1234d3f497eed5b1d80a07b3fcd1'

        r=requests.get(url.format(city,appid2)).json()

        print(r)

        weather={
            'city':city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        
        return render_template('index.html', weather=weather)

    return render_template('index.html', weather=weather_def)

if(__name__=="__main__"):
    app.run(debug=True)
