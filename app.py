from flask import Flask
from bs4 import BeautifulSoup
import requests
import json




app = Flask(__name__)

@app.route("/")
def time_api():


    res = requests.get("http://time.com")
    soup = BeautifulSoup(res.content)
    mydivs = soup.select("div.column.text-align-left.visible-desktop.visible-mobile.last-column a")
    list= []

    for div in mydivs:

        news = div.text
        news=news.replace("\n","")
        if news=="":
            continue
        data = {}
        data['title'] = news
        data['link']= 'http://time.com'+div['href']
        list.append(data)
        print(news)
        print(div['href'])

    #creating json array
    json_data= json.dumps(list)
    print(json.dumps(json_data))
    ret = json.dumps(json_data)
    # formatting jason
    ret =ret.replace('\\',"")
    ret= ret.replace(',',',<br><br>')

    #json returned to http://127.0.0.1:5000/
    return ret


if __name__ == "__main__":
    app.run()
