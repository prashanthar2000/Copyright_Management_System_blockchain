from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

def create_contract(abi, bytecode):
    #change this with real account
    w3.eth.defaultAccount = w3.eth.accounts[0]
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = Contract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    contract = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
    return contract



contract_interface = {}
with open('./backend/bin/copyrights_sol_UserRecords.bin',  'r') as f:
        contract_interface['bin'] = f.read() 

with open("./backend/bin/copyrights_sol_UserRecords.abi",  'r') as f:
    contract_interface['abi'] = f.read() 

contract = create_contract(contract_interface['abi'] , contract_interface['bin'])
# print(list(contract.functions))

