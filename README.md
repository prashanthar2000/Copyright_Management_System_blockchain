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

