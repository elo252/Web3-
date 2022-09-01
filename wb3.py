import json
from web3 import Web3

#INUFRA URL

# infura_url = "https://mainnet.infura.io/v3/8af24cf730d0454086a33f5dd2f15682"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected())
# # print(web3.eth.blockNumber)

# # balance = web3.eth.getBalance("0xf90Ed73c8834Ac3Af4c056D0211e598595A55d37")
# # print("Balance in wei:")
# # print(balance)

# # abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_value","type":"uint256"}],"name":"burnFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"tokenName","type":"string"},{"name":"tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]')
# # address = "0xdD0324d0E75aa3e26Ade717a438E579cAb8f41bB"

# # contract = web3.eth.contract(address=address, abi=abi)
# # print(contract)

# # totalSupply = contract.functions.totalSupply().call()
# # print(web3.fromWei(totalSupply, 'ether'))

#GANACHE URL


# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
# print(web3.isConnected())
# print(web3.eth.blockNumber)

# #Sending Crypto 
# #Two accounts

acc_1 = "0x1957692Dd43f56E0E7f19AfFE28F460a72A26E78" #Username sort off private key => signing transactions
# acc_2 = "0xB695476A823bd7716884b4553AF67BDa626B1648"

# private_key = "a2d7317e0ad26e3ebb4b6a367b514b241c730d3b9af018d637a4b1f0f39fc2a3" #acc_1



# #get nonce
# nonce = web3.eth.getTransactionCount(acc_1)
# #build transaction acc to the structure

# tx = {
#     'nonce': nonce,
#     'to': acc_2,
#     'value': web3.toWei(1, 'ether'),
#     'gas':200000,
#     'gasPrice': web3.toWei('50','gwei')   
# }

# #sign transcartion
# signed_tx = web3.eth.account.signTransaction(tx, private_key)

# #send transcation
# tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# #get hash
# print(web3.toHex(tx_hash))

#INTERACTING WITH SMART CONTRACTS ON REMIX

# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
# print(web3.isConnected())



# abi = json.loads('[{"constant":false,"inputs":[],"name":"firstGreet","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
# address = web3.toChecksumAddress("0x3D526d17A5E29De129CF609e9A21c4444978449f")

# contract = web3.eth.contract(address=address, abi=abi)


# contract.functions.firstGreet().call()
# print(contract.functions.greet().call())

# tx_hash = contract.functions.setGreeting('Call this function').transact()

# web3.eth.waitForTransactionReceipt(tx_hash)

# print('Updated :{}' .format(contract.functions.greet().call()))

#Deploy smart contract on blockchain 
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

abi = json.loads('[{"constant":false,"inputs":[],"name":"firstGreet","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
bytc = '608060405234801561001057600080fd5b50610480806100206000396000f300608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063402fda2614610067578063a41368621461007e578063cfae3217146100e7578063ef690cc014610177575b600080fd5b34801561007357600080fd5b5061007c610207565b005b34801561008a57600080fd5b506100e5600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610255565b005b3480156100f357600080fd5b506100fc61026f565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561013c578082015181840152602081019050610121565b50505050905090810190601f1680156101695780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561018357600080fd5b5061018c610311565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101cc5780820151818401526020810190506101b1565b50505050905090810190601f1680156101f95780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6040805190810160405280600581526020017f48656c6c6f000000000000000000000000000000000000000000000000000000815250600090805190602001906102529291906103af565b50565b806000908051906020019061026b9291906103af565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103075780601f106102dc57610100808354040283529160200191610307565b820191906000526020600020905b8154815290600101906020018083116102ea57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103a75780601f1061037c576101008083540402835291602001916103a7565b820191906000526020600020905b81548152906001019060200180831161038a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103f057805160ff191683800117855561041e565b8280016001018555821561041e579182015b8281111561041d578251825591602001919060010190610402565b5b50905061042b919061042f565b5090565b61045191905b8082111561044d576000816000905550600101610435565b5090565b905600a165627a7a72305820de5fcd6a098c7d1d29ae52e30baaaf730e20607e737473b50154b7dd04bcde8e0029'


Greeter = web3.eth.contract(abi=abi, bytecode= bytc)

tx_hash = Greeter.constructor().transact()

print(tx_hash)