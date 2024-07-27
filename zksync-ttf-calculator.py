import time
from web3 import Web3
from zksync2.module.module_builder import ZkSyncBuilder
import random

def simulate_ttf(zksync_rpc_url, eth_rpc_url, num_simulations=10):
    # Connect to zkSync and Ethereum
    zk_web3 = ZkSyncBuilder.build(zksync_rpc_url)
    eth_web3 = Web3(Web3.HTTPProvider(eth_rpc_url))

    total_ttf = 0
    for _ in range(num_simulations):
        # Simulate transaction inclusion time on zkSync
        zk_inclusion_time = time.time()
        
        # Simulate waiting for Ethereum finalization (random time between 5 to 15 minutes)
        eth_finalization_time = zk_inclusion_time + random.uniform(300, 900)
        
        # Calculate TTF for this simulation
        ttf = eth_finalization_time - zk_inclusion_time
        total_ttf += ttf
        
        print(f"Simulated TTF: {ttf:.2f} seconds")

        # Simulate waiting between transactions
        time.sleep(1)

    average_ttf = total_ttf / num_simulations
    return average_ttf

# Usage
zksync_rpc_url = "https://mainnet.era.zksync.io"
eth_rpc_url = "https://mainnet.infura.io/v3/YOUR-PROJECT-ID"

try:
    average_ttf = simulate_ttf(zksync_rpc_url, eth_rpc_url)
    print(f"Average Simulated Time to Finality: {average_ttf:.2f} seconds")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    print("Please check your network connection and RPC URLs.")