import os
import subprocess

# export PATH="$HOME/.local/bin/:$PATH"

# Path to the cardano-cli binary or use the global one
CARDANO_CLI_PATH = "cardano-cli"
# The `testnet` identifier number
CARDANO_NETWORK_MAGIC = 1097911063
# The directory where we store our payment keys
# assuming our current directory context is $HOME/receive-ada-sample
CARDANO_KEYS_DIR = "keys"
# The total payment we expect in lovelace unit
TOTAL_EXPECTED_LOVELACE = 1000000
print("::.")

# Read wallet address value from payment.addr file
with open(os.path.join(CARDANO_KEYS_DIR, "payment.addr"), 'r') as file:
    walletAddress = file.read()

# We tell python to execute cardano-cli shell command to query the UTXO and read the output data
rawUtxoTable = subprocess.check_output([
    CARDANO_CLI_PATH,
    'query', 'utxo',
    '--testnet-magic', str(CARDANO_NETWORK_MAGIC),
    '--address', walletAddress])

