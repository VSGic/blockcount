import requests    
import settings
from web3 import Web3, HTTPProvider

#NET First point########################
#Set here basic data node
base_url = settings.ethereum_pow_fork
########################################

def get_lastBlocks(base_url): 
	block_info = {
		"jsonrpc":"2.0",
		"method":"eth_blockNumber",
		"params":[],"id":1
		}
	response = requests.post(f"{base_url}", json=block_info)
	resp_data = response.json()
	last_block = int(resp_data['result'],16)
	return last_block

last_block = get_lastBlocks(base_url)

chainid_prototype = Web3(HTTPProvider(base_url))
Chain_first_prototype = chainid_prototype.eth.chain_id
output_first_prototype = str(Chain_first_prototype)

print("Last block on control ethereum node " + base_url + " is: " + str(last_block) + " and chainId is " + output_first_prototype)
c_node = last_block

#NET Second point########################
#Set here node that should be checked
base_url = settings.ethereum_infura
#########################################
last_block = get_lastBlocks(base_url)

chainid_prototype = Web3(HTTPProvider(base_url))
Chain_second_prototype = chainid_prototype.eth.chain_id
output_second_prototype = str(Chain_second_prototype)

print("Last block on monitored ethereum node " + base_url + " is: " + str(last_block) + " and chainId is " + output_second_prototype)
m_node = last_block

status = abs(c_node - m_node)

if status == 0:
	print("Ethereum nodes synchronized!")
elif 300 > status > 0:
	print("Ethereum nodes have differs a bit!")
else:
	print("Alert! Problem with node!") 	

 