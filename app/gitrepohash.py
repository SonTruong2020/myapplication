import subprocess

def get_git_repo_hash():
    hashes = []
    hashes.append('version: ')
    hashes.append(subprocess.check_output(['git', 'tag']))
    hashes.append('lastcommitsha: ')
    hashes.append(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
    hashes.append('description: pre-interview technical test')
    
    return hashes

if __name__ == "__main__":
    print(get_git_repo_hash())