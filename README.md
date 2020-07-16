# myapplication

This is may first application to explore docker containers and CI/CD pipeline.

The application should pull its own latest GIT project tag and commit sha, and display it in a web wrapper inside a docker container.
Updates to the repository will automatically trigger Travis to run unit tests against the latest commit.

Application: 
Application can be run using Python.
python endpoint.py

Docker Build:
  docker build -t myapplication .
run:
  docker run -p 5000:5000 --rm -it myapplication


Full details of application logic:
The application consists of 3 components.

gitrepohash.py: This module retrieves the repo tag and latest commit sha and return a list with all information to be presented on a web endpoint.
    
    Outstanding issues: None
                        

test_gitrepohash.py:  This is the unit test module for gitrepohash.
                      As gitrepohash does not have arguments, the unit test does not really do much.
                      It only check if the gitrepohash was successully executed. It's purely used as a pipeline task for Travis.
    
    Oustanding issues: Depending on the developement of gitrepohash.py, this module need to be extended to test both the gitrepohash and the web wrapper modules.
    

Endpoint.py:  This module is the web wrapper to present data from gitrepohash.
              Module runn successfully on local shell, but will not display full repo data in a docker container.
              
    Outstanding issues: Json data not properly formatted.
 
 
 Project status: Still under development.
 
