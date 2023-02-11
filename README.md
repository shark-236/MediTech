# MediTech
## Fintech Bootcamp Project 3  

Goal: To develop a secure healthcare data ecosystem. complete with a data repository and user platform.  

MediTech is the company responsible for integrating and launching the various components of the ecosystem. We start with data collection, storage, de-identification, and deployment. MediTech makes use of the following technologies to see the data through its lifecycle:  
-Blockchain (for smart contracts and data logging)  
-Streamlit (user interface)  
-NFTs (for unique, anonymous user identification)  

Beyond the technologies we will also touch on the regulatory environment and a market analysis pertinent to the scope of this product launch, which encapsulates the use and need for patient data in clinical research trials.   

Lastly, the documentation and presentation will highlight future iterations and advancements of MediTech's proposed product. 

---

## Technologies

To build our ecosystem we have employed the following:  
-Streamlit  
-Solidity  
-Remix Ethereum IDE  
-MetaMask  
-Ganache  
-Python  

Implementation of these programs is outlined in the 'imports' of each program file (available in this repository). 

---

## Installation Guide

The Remix IDE is a web-based program and requires no installation. The Remix IDE can be found at remix.ethereum.org.  

If installation of Ganache is required, please visit the Ganache download page:  
https://trufflesuite.com/ganache/   

If installation of MetaMask is required, please visit the MetaMask download page:  
https://metamask.io/download/  

If installation of Streamlit is required, run the following code in your terminal:  
pip install streamlit  

Note: We are not partnered with, sponsored by, or otherwise affiliated with Ganache, MetaMask, or Streamlit in any way. 

---

## Usage

In its practical state, the MediTech ecosystem works as such: 

First, a clinical trial participant (henceforth referred to as "patient") and clinical trial agree on participation. To import initial patient data, patient identification will be hashed into an initial upload via smart contracts on a private blockchain. Other initial contracts include consent agreements and business agreements. This data is then fed into a secure MediTech server to protect patient privacy.   

MediTech will then create an NFT for each patient and, within the secure environment, assign theur unique IDs and private keys. These relationships will only be accessible by MediTech. The NFT ID is what will be used in the actual trials and hashed onto the blockchain to record trial records and progress.  

Upon trial logs and participation, the records for the trial will be hashed onto the blockhain. This ensures data is immutable and available (which are two major challenges of data in the clinical trial space). An example of this is available in our repository under "Contracts" -> "Update_Log.sol". This file can be uploaded and launched through Remix. Remember to connect Ganache and MetaMask for pseudo-training accounts and contract deployment. Deploying through Remix will also allow us to save the ABI for the contract. The ABI is used to connect the contract through Streamlit to provide clinicians with an easy-to-use interface. The ABI save file, the code that creates the NFT, and the Streamlit NFT interface files are housed in this repo under "Contracts" -> "contracts".   

Streamlit is also used to provide interfaces for initial data logging (along with the trial phase record inputs). Examples of this interface are included in this repository under the "Streamlit" folder.   

For those that could not attend our presentation, the Market Analysis and Regulations portions will be briefly explained in the next section. 

---

## Explanation of Compliance Considerations  

---

## Contributors

Yan Huang  
Shahrukh Alam   
Jorge Villacreses  
Christopher Swanson  
Boris Gorelenkov  
Maria Angeles Bonany

---

## License

Columbia Engineering: FinTech Bootcamp, Aug. 2022 - Feb. 2023