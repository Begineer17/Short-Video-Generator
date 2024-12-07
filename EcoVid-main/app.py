from flask import Flask, render_template
from requests import request, post
from random import choice
from string import ascii_lowercase

app = Flask(__name__)

access_token = ''

#server_endpoint = 'https://chickenitcode.github.io/tiktokAPI/'
server_endpoint = '/'

@app.route('/')
def index():
    try:
        code = request.args.get('code')
        url = 'https://open.tiktokapis.com/v2/oauth/token/'
        url += '?client_key=sbawfn3gsybacj2b99'
        url += '&client_secret=qSRQWq82H5Rj9pNRbo04did0FnbVbqtH'
        url += '&code=' + code.decode('utf8')
        url += '&grant_type=authorization_code'
        url += '&redirect_uri='+ server_endpoint
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        respond = post(url= url, headers= headers)

        return render_template('index.html')
    except:
        return render_template('index.html')

@app.route('/login.html')
def login():
    letters = ascii_lowercase
    state = ''.join(choice(letters) for i in range(23))

    url = 'https://www.tiktok.com/v2/auth/authorize/'
    url += '?client_key=sbawfn3gsybacj2b99'
    url += '&scope=user.info.basic,video.publish,video.upload,user.info.profile,user.info.stats,video.list'
    url += '&response_type=code'
    url += '&redirect_uri=' + server_endpoint
    url += '&state=' + state
    return render_template('login.html', url= url)

if __name__ == '__main__':
    app.run()