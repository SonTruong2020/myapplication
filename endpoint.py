import os
import json

from flask import Flask
from app import gitrepohash

app = Flask(__name__)

@app.route("/")
def endpoint():

    page = '<html><body><h1>'
    page += 'Welcome: Please go to /version to see application version and last commit hash.'
    page += '<h1></body></html>'
    return page


@app.route("/version")
def endpoint1():
 #   page = gitrepohash.get_git_repo_hash()
 #   page = '<html><body><h1>'
 #   page += json.dumps(gitrepohash.get_git_repo_hash(),indent=4)
 #   page += '<h1></body></html>'
    githash =  gitrepohash.get_git_repo_hash()

    return json.dumps(githash,indent=4)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))