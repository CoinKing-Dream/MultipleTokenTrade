import solana
from solana.rpc.api import Client
from solders.pubkey import Pubkey
import json

def get_token_transaction_history(token_address):
    # Connect to the Solana devnet
    client = Client("https://api.devnet.solana.com")
    # connection = conn("https://api.mainnet-beta.solana.com/") 
    pubkey = Pubkey.from_string(token_address)

    # Market address we will interact with
    # market_address = "9wFFyRfZBsuAha4YcuxcXLKwMxJR43S7fPfQLusDBzvT"
    
    # Get transaction signatures for the token address
    response = client.get_signatures_for_address(pubkey).value
    # signatures_list = [signature for signature in response]
    # response_json = json.dumps(response.getBlockCommitment)
    # print(response["GetSignaturesForAddressResp"])
    # print(response)

    with open("1.txt", "w") as file:
        file.write(str(response) + "\n")

    # Iterate through each signature and fetch detailed info
    # for tx_sig in response['result']:
    #     signature = tx_sig['signature']
        
    #     # Fetch detailed transaction information
    #     tx_info = client.get_confirmed_signature(signature)
    #     print(tx_info)

if __name__ == "__main__":
    token_address = "So11111111111111111111111111111111111111112"
    get_token_transaction_history(token_address)