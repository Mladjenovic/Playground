- Information about creating/runing docker

  - To build the docker image run `docker build --tag python-docker .` from the root direcotory
  - To run the image inside a container use `docker run -d -p 5000:5000 python-docker`
  - To stop the container `docker stop <container-name>`

- Debugging info for vs code

  - launch.json is the configuration file for vs code

- Virtual environment info
  - First create a venv runing `python3 -m venv /path/to/new/virtual/environment`
  - To activate the environment use `myenv/Scripts/activate` from console
  - requirements.txt will contain all the modules needed for virtual environment
  - To save the current modules form pip use the command `python pip freeze > requirements.txt`
  - To install the modules from requirements.txt use `pip install -r requirements.txt`
