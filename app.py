import streamlit as st
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import numpy as np
import webbrowser

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Diagnositc Quiz", "More Information", "Contact Us"])
data = np.random.randn(10, 1)

tab1.subheader("What is Obstructive Sleep Apnea")
tab1.write("paragraph")

tab2.subheader("Get your AI-backed diagnosis today!")

tab3.subheader("Find out more about OSA")
tab3.write("paragraph")
col = st.columns(2)
	with col[0]:
		st.write("info")
	with col[1]:
		st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')

tab4.subheader("Contact Us & About Me")
col2 = st.columns(2)
  with col[0]
    st.write("contact us here!")
    st.link_button("", "https://www.instagram.com/ananya._.aggarwal/")
  with col[1]
    st.write("learn more about me..."




