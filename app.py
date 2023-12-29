import streamlit as st
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import numpy as np
import webbrowser

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Diagnositc Quiz", "More Information", "Contact Us"])
data = np.random.randn(10, 1)

with tab1:
	st.subheader("What is Obstructive Sleep Apnea")
	st.write("paragraph")

with tab2:
	st.subheader("Get your AI-backed diagnosis today!")

with tab3:
	st.subheader("Find out more about OSA")
	st.write("paragraph")
	col = st.columns(2)
	with col[0]:
		st.write("info")
	with col[1]:
		st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')

with tab4:
	st.subheader("Contact Us & About Me")
	col2 = st.columns(2)
	with col2[0]
		st.write("contact us here!")
    		st.link_button("", "https://www.instagram.com/ananya._.aggarwal/")
 	 with col2[1]
    		st.write("learn more about me..."




