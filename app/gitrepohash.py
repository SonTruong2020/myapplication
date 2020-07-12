import subprocess

def get_git_version_hash():
    hashes = []
    hashes.append(subprocess.check_output(['git', 'tag']))
    hashes.append(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
    hashes.append('"description" : "pre-interview technical test"')
    
    return hashes

if __name__ == "__main__":
    print(get_git_version_hash())