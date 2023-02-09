import functools
from pathlib import Path
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI"))

@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('NFT_ABI.json')) as f:
        NFT_ABI = json.load(f)
          
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
          
    contract = w3.eth.contract(
        address=contract_address,
        abi=NFT_ABI
    )
          
    return contract
    contract = load_contract()
          
st.title("Mint a New NFT for Patient")
accounts = w3.eth.accounts
address = st.selectbox("Select NFT Owner", options=accounts)
tokenId = contract.functions.lastTokenId().call()
st.write(tokenId)
tokenURI = contract.functions.tokenURI(tokenId).call()
st.write(tokenURI)
NFT_uri = st.text_input("The URI to the NFT")
          
if st.button("Mint NFT"):
    tx_hash = contract.functions.mintToken(uint256 One_Per_Transaction).transact({})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("NFT mined:")
    st.write(dict(receipt))