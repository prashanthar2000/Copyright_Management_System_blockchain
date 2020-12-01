# basic_user_contract
Basic etherium contract for storing user using python and flask

### how to run
source venv/bin/activate

run  ganache-cli in a different terminal
python contract.py


u can see contract deployment hash ...etc in ganache 
u can all the function by using contract.function.functionname.call()



##### create site.db
rm backend/site.db
#in python interpreter 
from backend import db 
db.create_all()

### How to run

Clone the git repository or download zip from.

https://github.com/prashanthar2000/Copyright_Management_System_blockchain

Extract the file and store it in the directory with all python installations.
 Then do 
cd  Copyright_Management_System_blockchain-master

pip install -r requirement.txt

in one terminal run
 ganache-cli 

in another terminal run 
python3 app.py

The website will be up and running in local host 
http://127.0.0.1:5000/

We also hosted the site on AWS

http://3.87.2.207:8080/

