import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from inference import infer
import time
import base64

st.set_page_config(page_icon="", page_title="Project2")

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



img2 =get_img_as_base64("Final_image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:Final_image/png;base64,{img2}");
background-size: 80% ;
background-position: center ;
background-repeat: no repeat;
background-attachment: local;
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
menu = ["Home","Recognition","About"]
choice = st.sidebar.selectbox("Menu",menu)
if choice =="Home":
    st.markdown("<h1 style='text-align: center; color: orange;'>Welcome to Food Image Recognition System</h1>", unsafe_allow_html=True)
if choice == "About":
    #st.subheader("About")
    st.markdown("<h3 style='text-align: center; color: white;'> Built with Streamlit & Python</h3>",unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: orange;'>The main motive of this project is to help the individuals automatically identify the dishes from social media</h3>",unsafe_allow_html=True)

if choice == "Recognition":
    st.markdown("<h1 style='text-align: center; color: orange;'>Food Image Recognition </h1>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; color: orange;'>It recognize 261 types of Indian Food   </h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; color: orange;'>We present the top five predictions and display their ingredients and region of origin.</h4>", unsafe_allow_html=True)


    col1, col2, col3 = st.columns([1,18,1])
    clo2 =st.columns([1,18,1])


    img = 0

    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image




# Uploading the File to the Page
    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png','jpeg'])

# with col1:
#         st.write(' ')

    clo2 =st.columns([1,18,1])
    with col2:



        if uploadFile is not None:


            img = load_image(uploadFile)


            with st.spinner('Wait for it...'):

                list_of_predictions,list_of_prep_times,list_of_regions,list_of_ingredients,pred_prob = infer(uploadFile)
                st.image(img)
                time.sleep(1)





            list_of_predictions = [i.replace('_',' ') for i in list_of_predictions]

        #st.write('The most likely foods are as follows 👇')
        
            st.markdown("<p style='text-align: center; color: white;'>The most likely foods are as follows 👇.</p>", unsafe_allow_html=True)

            if pred_prob[0] > 0.0:
            
            
                st.markdown("""
        #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
        """.format(list_of_predictions[0],list_of_prep_times[0],list_of_regions[0],list_of_ingredients[0]),  unsafe_allow_html=True)
            

#             st.write('* This is ', list_of_predictions[0],". It takes ",list_of_prep_times[0],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[0], ' India.', 'The main ingredients are ',list_of_ingredients[0] ,' .')

            if pred_prob[1] > 0 :
                st.markdown("""
         #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
        """.format(list_of_predictions[1],list_of_prep_times[1],list_of_regions[1],list_of_ingredients[1]),  unsafe_allow_html=True)

#             st.write('* This is ',list_of_predictions[1],". It takes ",list_of_prep_times[1],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[1], ' India.','The main ingredients are ',list_of_ingredients[1] ,' .')

            if pred_prob[2] > 0:
        
                st.markdown("""
         #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>
        """.format(list_of_predictions[2],list_of_prep_times[2],list_of_regions[2],list_of_ingredients[2]),  unsafe_allow_html=True)

#             st.write('* This is ',list_of_predictions[2],". It takes ",list_of_prep_times[2],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[2], ' India.','The main ingredients are ',list_of_ingredients[2] ,' .')

            if pred_prob[3] > 0:
        
                st.markdown("""
         #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>
        """.format(list_of_predictions[3],list_of_prep_times[3],list_of_regions[3],list_of_ingredients[3]),  unsafe_allow_html=True)

#             st.write('* This is ',list_of_predictions[3],". It takes ",list_of_prep_times[3],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[3], ' India.','The main ingredients are ',list_of_ingredients[3] ,' .')

            if pred_prob[4] > 0:
        
                 st.markdown("""
    #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
    """.format(list_of_predictions[4],list_of_prep_times[4],list_of_regions[4],list_of_ingredients[4]),  unsafe_allow_html=True)
        
        

#             st.write('* This is ',list_of_predictions[4],". It takes ",list_of_prep_times[4],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[4], ' India.','The main ingredients are ',list_of_ingredients[4] ,' .')







        #st.write("Image Uploaded Successfully")
                 st.markdown("<p style='text-align: center; color: white;'>Image Uploaded Successfully</p>", unsafe_allow_html=True)
            else:
        #st.write("Make sure you image is in JPG/PNG Format.")
        
               st.markdown("<p style='text-align: center; color: white;'>Make sure you image is in JPG/PNG Format.</p>", unsafe_allow_html=True)
