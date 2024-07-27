# Time to Finality Latency simulator for zkSync


# Overview
This project is a Time to Finality (Latency) simulator for zkSync, developed using Python and the web3 library. It aims to simulate and measure the latency involved in reaching finality on the zkSync Layer 2 protocol. zkSync is a Layer 2 scaling solution for Ethereum, designed to increase throughput and reduce gas fees while maintaining the security and decentralization of the Ethereum mainnet.

# Features
Simulation of Transaction Latency: Simulates the time taken for transactions to achieve finality on zkSync.
Web3 Integration: Utilizes the web3 library to interact with the zkSync and Ethereum networks.
Customizable Simulations: Allows users to set the number of simulations to run for more accurate average latency measurements.
Real-time Results: Prints simulated Time to Finality (TTF) for each transaction and calculates the average TTF over multiple simulations.
Installation

# Clone the repository:

git clone https://github.com/yourusername/zkSync-latency-simulator.git
cd zkSync-latency-simulator

# Install the required dependencies:

pip install -r requirements.txt

# Usage
Configure the zksync_rpc_url and eth_rpc_url in the script or use your own URLs:

zksync_rpc_url = "https://mainnet.era.zksync.io"
eth_rpc_url = "https://mainnet.infura.io/v3/YOUR-PROJECT-ID"

# Run the simulator:

python simulate.py
