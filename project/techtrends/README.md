# TechTreds Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Run 

To run this application there are 2 steps required:

1. Initialize the database by using the `python3 init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
2.  Run the TechTrends application by using the `python3 app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.
(To turn on debug mode: `export FLASK_ENV=development` first)

https://docs.anaconda.com/anaconda/install/mac-os/
Anaconda3 is already installed in /Users/mommy/opt/anaconda3. Use 'conda update anaconda3' to update Anaconda3.
  conda update anaconda3 //
PackageNotInstalledError: Package is not installed in prefix.
  prefix: /Users/mommy/opt/anaconda3
  package name: anaconda3
source /Users/mommy/opt/anaconda3/etc/profile.d/conda.sh per https://stackoverflow.com/questions/35246386/conda-command-not-found
conda create -n shiny_new_env python=2.7
conda activate new_env// or `source activate <new-env>`?
conda deactivate
conda env remove --name shiny_new_env
  conda init zsh // per https://stackoverflow.com/questions/35246386/conda-command-not-found
  then run `pip freeze > requirements.txt`//see certifi==2020.6.20 for 2.7
https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
https://code.visualstudio.com/docs/python/linting
To lint: set pycodestyle(formerly pep8) as linter in VSCode
https://code.visualstudio.com/docs/python/linting
(conda install -c anaconda pep8//conda uninstall -c anaconda pep8
pep8 -h)
autopep8 --in-place --aggressive --aggressive init_db.py
python interpreter: https://code.visualstudio.com/docs/python/environments : /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /usr/bin/python3
Flask : https://flask.palletsprojects.com/en/2.0.x/installation/

curl -sfL https://get.k3s.io | sh -
sudo zypper --non-interactive install apparmor-parser
