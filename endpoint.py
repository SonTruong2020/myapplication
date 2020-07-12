import os
from flask import Flask
from app import gitrepohash

app = Flask(__name__)

@app.route("/")
def endpoint():
    hash = gitrepohash.get_git_repo_hash()
    
    page = '<html><body><h1>'
    for h in hash:
        page += h + '\n'
    page += '<h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))