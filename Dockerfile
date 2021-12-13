# Specify the base docker image
FROM rcarmo/ubuntu-python

# Upgrade pip 
RUN /usr/local/bin/python3.8 -m pip install --upgrade pip

# Install pipenv to manage python libraries and dependencies 
RUN pip install pipenv

# Create app directory
WORKDIR ../app

# Copy pipenv files
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install python libraries 
RUN pipenv install --system --deploy

# Download and install Pfeature Python library, which is used to calculate 
# molecular features
RUN apt clean && apt update && apt install unzip -y
RUN wget https://github.com/raghavagps/Pfeature/raw/master/PyLib/Pfeature.zip
RUN unzip Pfeature.zip
WORKDIR Pfeature
RUN python setup.py install

# Copy files required to run the model
WORKDIR ../
COPY ["predict.py", "ExtraTreesClassifier_maxdepth50_nestimators200.bin", "./"]

# Expose port to run the app 
EXPOSE 9696

# Run gunicorn to manage web service in deployment properly
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]