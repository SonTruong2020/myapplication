#import subprocess
import os

def get_git_repo_hash():
    hashes = []
    tag = os.popen('git tag')
    t = tag.read()
    hashes.append('Version:' + t)

    lastcommit = os.popen('git rev-parse --short HEAD')
    l = lastcommit.read()
    hashes.append('Lastcommitsha: ' + l)
    
    #hashes.append('Flask will fail with subprocess output-  NEED to fix HashRetrieval code !!!!')
    #hashes.append('version: ' + str(subprocess.check_output(['git', 'tag'])))
    #hashes.append('lastcommitsha: ' + str(subprocess.check_output(['git', 'rev-parse', 'HEAD'])))
    hashes.append('description: pre-interview technical test')
    
    return hashes

if __name__ == "__main__":
    print(get_git_repo_hash())