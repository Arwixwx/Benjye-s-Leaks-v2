from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/streaming/')
def streaming():
    titles = []
    dates = []
    links = []
    with open('accounts/streaming.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/vpn/')
def vpn():
    titles = []
    dates = []
    links = []
    with open('accounts/vpn.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/gaming/')
def gaming():
    titles = []
    dates = []
    links = []
    with open('accounts/gaming.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/music/')
def music():
    titles = []
    dates = []
    links = []
    with open('accounts/music.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/admin/', methods=['POST', 'GET'])
def admin_login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['pass']
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
