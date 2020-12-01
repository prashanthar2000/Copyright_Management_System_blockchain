# Copyright Management System

Blockchain for Copyright management. This platform can be used to commit and verify various copyright relating transactions, this platform is implemented on the concepts of blockchain making it more secure for the transaction and verification of the copyright issues.

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

##### create site.db
rm backend/site.db
#in python interpreter 
from backend import db 
db.create_all()
