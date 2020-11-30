from backend import contract
a = contract.functions.insertUser("0x1Ff9023808F8671bc91722989612D63c93032ABf" ,"adfd" , "owner").transact()
print(a)
b = contract.functions.insertUser("0xE818d71ce374C7e84e80389b7322fDb1246C8Cb8" ,"adfd" , "owner").transact()
print(b)

c = contract.functions.transfertokens("0x1Ff9023808F8671bc91722989612D63c93032ABf" , "0xE818d71ce374C7e84e80389b7322fDb1246C8Cb8" , int("1")).transact()
#c = contract.functions.transfertokens("0xE818d71ce374C7e84e80389b7322fDb1246C8Cb8" , "0x1Ff9023808F8671bc91722989612D63c93032ABf" , int("1")).transact()
print(c)

