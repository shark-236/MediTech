# MediTech
## Fintech Bootcamp Project 3  

Goal: To develop a secure healthcare data ecosystem, complete with a data repository and user platform.  

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

MediTech will then create an NFT for each patient and, within the secure environment, assign their unique IDs and private keys. These relationships will only be accessible by MediTech. The NFT ID is what will be used in the actual trials and hashed onto the blockchain to record trial records and progress.  

Upon trial logs and participation, the records for the trial will be hashed onto the blockhain. This ensures data is immutable and available (which are two major challenges of data in the clinical trial space). An example of this is available in our repository under "Contracts" -> "Update_Log.sol". This file can be uploaded and launched through Remix. Remember to connect Ganache and MetaMask for pseudo-training accounts and contract deployment. Deploying through Remix will also allow us to save the ABI for the contract. The ABI is used to connect the contract through Streamlit to provide clinicians with an easy-to-use interface. The ABI save file, the code that creates the NFT, and the Streamlit NFT interface files are housed in this repo under "Contracts" -> "contracts".   

Streamlit is also used to provide interfaces for initial data logging (along with the trial phase record inputs). Examples of this interface are included in this repository under the "Streamlit" folder.   

For those that could not attend our presentation, the Market Analysis and Regulations portions will be briefly explained in the next section. 

---

## Explanation of Privacy Considerations  

<<<<<<< HEAD
The healthcare industry presents particular challenges specifically regarding data collection and use. To comply with HIPAA and GDPR regulations, MediTech uses a secure server (with only company access) to house patient identifying information. As well, the keys translating the patient and unique NFT IDs are also under MediTech control. The only public information will be the NFT IDs and the trial logs, available on the blockchain. Examples of protected patient information include:  
-Dates of birth  
-Telephone numbers  
-Geographic data  
-Fax numbers  
-Social Security numbers   
-Email addresses  
-Medical record numbers  
-Account numbers  
-Health plan beneficiary numbers  
-Certificate/License numbers  
-Vehicle identifiers and serial numbers (including license plates)  
-Web URLs  
-Device identifiers and serial numbers  
-Internet protocol addresses  
-Full face photos and comparable images  
-Biometric identifiers (i.e. retinal scans, fingerprints)  
-Any unique identifying number or code (except unique codes assigned to code data)  
=======
The healthcare industry presents particular challenges specifically regarding data collection and use. In particular, information relating to the physical or mental health or condition of an individual that is transmitted or maintained by electronic media affords regulatory protections that MediTech needs to comply with (ie. HIPAA in the US requires protection of PHI and GDPR in the EU requires protection of sensitive data). Protected health data includes name, address, dates, phone number, SSN, health plan beneficiary number, biometric IDs, such as a fingerprint, and any other unique identifying characteristics.  

To follow privacy regulations, MediTech uses a secure server (with only company access) to house patient identifying information. In addition, the keys translating the patient and unique NFT IDs are also under MediTech control. The only public information will be the NFT IDs and the trial logs, available on the blockchain. Future iterations will include additional privacy-enhancing techologies, similar to the ones implemented by Monero, with the use of stealth addresses, or PETchain, whereby data is stored securely in a distributed manner and processed in a user-selected execution environment.  
>>>>>>> 865a13e31a5b060caa7cbe4d3016d0a1391b0018

Market analysis shows growth in R&D for pharmaceutical companies and the like. This growth creates the need for easily accessible, transmittable, and immutable data. Of course, MediTech would not disclose patient identifying information without the patient's consent. However, the tracking of trial logs through their phases, and the ability to link NFT IDs through history, will help prove trial success. For more details on the Market Analysis please refer to our presentation (available in this repository). 

---

## Future Iterations and Advancements  

This ecosystem has the potential to expand deep into the medical field. There are additional optimizations for the ecosystem that can be deployed, which we will briefly touch on below:  

NFTs: We will create digital wallets for each patient to house their NFTs securely. They can be wearable devices, such as bracelets, that the patient keeps with them. These wallets will have additional security through biometric identification confirmation (ex. fingerprints).   

Smart Contracts: will see variations invluding initial patient information gatering, consent agreements, and business associate agreements. All contracts will be advanced to include admin permissions, view-only permissions, or restricted access (depending on use-case). The contract ABIs will also allow us to directly gather inputted information and collate them into a secure server database, which can then be de-identified, parsed, and sold.   

Expansion: There is much opportunity for this product to expand further into the medical field; for example, hospitals and doctor’s offices (where medical data is generated) and insurance companies (who have a large need to view and use medical data). This is where the monetization of data comes in and plays to MediTech’s favor as we barter the de-identified data out.   

Crowdfunding: To create funds for initial launch and seed funding. 

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
