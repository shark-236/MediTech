# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='Home', layout='wide')

# Title
st.title('Welcome To Meditech')

# Content
c1,c2 = st.columns(2)
c1.image(Image.open('images/meditechbanner.png'))


st.write(
    """
    MediTech is a conceptualized medical care tracking system. The concept uses the Blockchain and Data farming in an effort to accurately and cheaply track
    patients, care given (along with ailments, symptoms, procedures, and medications), costs incurred. A wallet will be created to tie to each individual user
    to the medical care platform and give them a unique ID. A Cryptocurrency will be created to peg to USD and use only in healthcare systems. Families can
    grouped together and coins will be allocated based on use-case/family needs. The tokens are pegged to a currency to keep from fluctuating. 
    """
)

st.subheader('Methodology')
st.write(
    """
    We use blockchain to log data where each block is a new entry of data
    """
)



c1, c2 = st.columns(2)
with c1:
    st.info('**GitHub: [@MediTech](https://github.com/shark-236/MediTech)**', icon="💻")
with c2:
    st.info('**For: [Columbia Fintech](https://bootcamp.cvn.columbia.edu/fintech/)**', icon="🧠")
