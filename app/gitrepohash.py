import subprocess

def get_git_repo_hash():
    hashes = []
    hashes.append('Flask will fail with subprocess output-  NEED to fix HashRetrieval code !!!!')
    #hashes.append('version: ' + str(subprocess.check_output(['git', 'tag'])))
    #hashes.append('lastcommitsha: ' + str(subprocess.check_output(['git', 'rev-parse', 'HEAD'])))
    hashes.append('description: pre-interview technical test')
    
    return hashes

if __name__ == "__main__":
    print(get_git_repo_hash())