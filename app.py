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

tab4.subheader("Contact Us")
tab3.write("Hi! I'm Ananya Aggarwal and I'm a junior in high school in the Bay Area. Contact me:")
tab3.link_button("", "https://www.instagram.com/ananya._.aggarwal/")



