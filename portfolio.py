import streamlit as st

import google.generativeai as genai
import os
from base64 import b64encode as encode
from datetime import  datetime 

st.set_page_config(layout="wide")
genai.configure(api_key="AIzaSyDFu8KiANB91LVkP_uVZsYy6L1OpV7f60w")#AIzaSyDxB-Zm__lh_wMjs5Kz7PGoY7BOlfv0rCs
model = genai.GenerativeModel('gemini-1.5-flash')
def custom_bg():
    def img_cvt_bs64(image):
        with open(image,'rb') as image:
            data = image.read()
        return encode(data).decode() 
    image = img_cvt_bs64("images/3607424.jpg")

    set_bg =f"""
        <style>
        #root > div:nth-child(1) > div.withScreencast > div > div
        {{
            background-color: #0C0908;
            background-image: url('data:image/png;base64,{image}');
            background-position: center;
            background-size: cover;
        }}
        </style>
        """
    st.markdown(set_bg,unsafe_allow_html=True)

def yogiii():
    st.image("Images//Yogendra.png")
    def profile(img):
        with open(img,'rb') as image:
            data = image.read()
        return encode(data).decode() 
    img = profile("Images/Yogendra.png")
    
def html_file() :
    with open("html files/web.html") as webh:
        st.html(webh.read())
def css_file():
    with open("css files\web.css") as web:
        st.markdown(f"<style> {web.read()}</style>",unsafe_allow_html=True) #markdowm function injects css 
     
def AI():
    persona="""
            You are Yogendra's AI BOT. You help people answer questions about yourself(i.e Yogendra) a male. You are not yogendra's ai bot , you self is yogendra.
            My father's name is Rajendra Prasad Patnaik and mother's name is D. Bhagyalaxmi Patnaik. Jai is my bestfriend , my dance partner, skecthing partner , coding mentor. 
            Anser as if you are responding, dont anser in second or third person.
            if you don't know the anser then you simply say "I can't share this with you , sorry about that...:sweat_smile:". Chief minister of odisha is Mohan Charan Manjhi, Naveen patnaik is the ex CM of Odisha remember it .
            Here is more information about Yogendra. Answer accurately according to asked question.
            Yogendra Patnaik is a student , persuing Btech degree in Computer Science and Engineeing with specialization in Artificial Intelligence and Machine Learning in GIET UNIVERSITY, GUNUPUR.
            Hobbies of Yogendra is Sketching, Dancing, Singing.
            He completed his 10+2 studies from DAV Public school , Jharsuguda, Odisha and 10th from Saint Thomas English School with Subjects Physics, Chemistry, maths and computer application.
            He is from jharsuguda, Odisha . His height is 5.9, current weight is 67 kgs. 
            """ 
    st.title(" ")
    st.title("Yogendra as  :robot_face:")
    
    st.markdown("![Alt Text]()")#, https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif
    
    user_question=st.text_input(label="Ask Anything About Me ", placeholder="Type your query here...")
    if st.button("ASK ", use_container_width=500):
         prompt=persona + user_question
         response=model.generate_content(prompt)
         st.write(response.text)

    st.title(" ")
def Social_media():

    st.header("Social media links :")

    col1,col2,col3=st.columns(3)

    with col1:
        
        st.link_button(label="Instagram" ,url="https://www.instagram.com/_yogiii.22_")

    with col2:
        st.link_button(label="Youtube" ,url="https://www.youtube.com/YOGENDRAFFOfficial")
def skills():
    with open("html files/skills.html") as webh:
        st.html(webh.read())
def Gallery():
    st.title("Gallery")

    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image("Images/yogi1.jpg")
        st.image("Images/yogi2.jpg")
    
    with col2:
        st.image("Images/yogi6.jpg")
        st.image("Images/yogi7.jpg")
        st.image("Images/yogi3.jpg")

    with col3:
        st.image("Images/yogi5.jpg")
        st.image("Images/yogi10.jpg")
        st.image("Images/yogi11.jpg")

    with col4:
        st.image("Images/yogi9.jpg")    
        st.image("Images/yogi4.jpg")
def Sketches(): 
    st.title("Some of My Sketches")

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.image("Images/sk7.jpg")
        st.image("Images/sk5.jpg")
    with col2:
        st.image("Images/sk2.jpg")
        st.image("Images/sk3.jpg")
    with col3:
        st.image("Images/sk4.jpg")
        st.image("Images/sk1.jpg")
    with col4:
        st.image("Images/sk6.jpg")
        st.image("Images/sk0.jpg")
        st.write(" ")
def contact():
    with open("html files/contact.html") as webh:
        st.html(webh.read())
def footer():
    st.subheader(body="" ,divider="rainbow")
    st.write("Copyright@" + str(datetime.now().year) )
def call():
    html_file()
    css_file()
    yogiii()
    AI()
    Social_media()
    skills()
    Gallery()
    Sketches()
    contact()
    footer()
    custom_bg()
call()