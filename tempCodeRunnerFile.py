from flask import Flask , render_template , request
import requests

app = Flask(__name__)

@app.route('/')
def render_page():
    return render_template('index.html')

@app.route('/activity', methods = ['GET','POST'])
def get_activity():
    aces = request.form.get('accessibility')
    if aces == 'easy':
        aces = 0
    elif aces == 'medium':
        aces = 0.5
    else :
        aces = 1

    at_type = request.form.get('type')
    no_p = request.form.get('participants')
    price = request.form.get('price')

    params = {'accessibility':aces,'type':at_type,'participants': no_p,'price':price}

 

    response = requests.get('http://www.boredapi.com/api/activity/',params=params)
    data = response.json()


    if not any(i == 'error' for i in data):
        act = data['activity']
        return f"{act}"
    else:
        return f"No acitvity exists"
    

    #return f"aces {aces} ,{at_type},{no_p},{price} , /n {data}"
    

if __name__=='__main__':
    app.run(host = '0.0.0.0',port= 8000, debug= True)
