##Project home dir.
#Activate vend 
source .venv/bin/activate

#Start server 
app.main:app --reload

#After install update or delete package dependencies freeze the status
pip freeze > requirements.txt


##Pitfall
#Fix ModuleNotFoundError: No module named 'app' 
#https://github.com/tiangolo/fastapi/issues/2582 or https://realpython.com/absolute-vs-relative-python-imports/
export PYTHONPATH=$PWD


export PYTHONPATH=$PWD && source .venv/bin/activate && python app/db/main.py