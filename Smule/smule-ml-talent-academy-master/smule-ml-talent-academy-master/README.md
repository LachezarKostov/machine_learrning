# Smule ML Talent Academy

This project will host the source code related to the Smule ML talent academy. 

## Setup

The dependency manager for this project is pipenv. If you do not have it installed, please run.

`sudo -H pip3 install pipenv`

Afterwards, to install the necessary dependencies, simply run

`pipenv install`

Next, register a jupyter kernel:

`pipenv run python -m ipykernel install --user --name=smule`

Finally, you can start the jupyter notebook.

`pipenv run jupyter notebook .`


