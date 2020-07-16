import os
import json

def get_git_repo_hash() :

    version = (os.popen('git tag')).read().split("\n")[0]
    lastcommit = (os.popen('git rev-parse --short HEAD')).read().split("\n")[0]

    hashes = {'Version':version,'lastcommitsha':lastcommit,'description':'pre-interview technical test'}
    myapp = {"myapplication":[hashes]}

    return myapp

if __name__ == "__main__":
    print(json.dumps(get_git_repo_hash(),indent=4))
