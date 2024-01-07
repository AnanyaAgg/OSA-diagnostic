import streamlit as st
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import numpy as np
import webbrowser

st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Diagnositc Quiz", "More Information", "Contact Us"])
data = np.random.randn(10, 1)

with tab1:
	st.subheader("What is Obstructive Sleep Apnea")
	st.write("paragraph")

with tab2:
	st.header("Get your AI-backed diagnosis today!")
	"""general questions"""
	with st.expander():
		genre = st.radio("What is your age?", ["<20", "20-30", "30-40", "40-50", "50-60", ">60"])
	with st.expander():
		genre = st.radio("What is your gender by birth?", ["male", "female", "prefer not to say"])
	with st.expander():
		genre = st.radio("How much do you weigh?"), ["<100 lbs", "100-150 lbs", "150-200 lbs", ">200 lbs"])
	with st.expander():
		genre = st.radio("How tall are you? (ft, in)"), ["how wld i use double quotes in text?"])

	"""experience with common symptoms"""
	with st.expander():
		genre = st.radio("How often do you snore?"), ["almost every day", "3-4 times a week", "less than that"])
	with st.expander():
		genre = st.radio("Do you snore loudly (louder than talking or loud enough to be heard through closed doors)"), ["yes", "no"])
	with st.expander():
		genre = st.radio("Has anyone noticed that you quit breathing during your sleep?"), ["yes, multiple times", "yes, only once or twice", "no, never"])
	with st.expander():
		genre = st.radio("Do you use any medication (pills, gummies, etc.) to fall asleep?"), ["almost every day", "3-4 times a week", "less than that"])
	with st.expander():
		genre = st.radio("Are you tired after sleeping?"), ["almost every day", "3-4 times a week", "less than that"])
	with st.expander():
		genre = st.radio("Are you tired during awake time?"), ["almost every day", "3-4 times a week", "less than that"])
	with st.expander():
		genre = st.radio("Have you ever nodded off or fallen asleep while driving? If yes, how often?"), ["yes, aLmost every day", "yes, at least once a week", "yes, very rarely", "no. never"])
	with st.expander():
		genre = st.radio("Do you often have headaches in the morning?"), ["almost every day", "3-4 times a week", "less than that"])
	with st.expander():
		genre = st.radio("Do you have trouble remembering things?"), ["almost every day", "3-4 times a week", "less than that"])
	with st.expander():
		genre = st.radio("Do you have trouble with basic problem-solving/logic questions?"), ["almost every day", "3-4 times a week", "less than that"])
	
	"""other health questions"""
	with st.expander():
		genre = st.radio("Do you have or are you being trated for high blood pressure"), ["yes, no"])
	with st.expander():
		genre = st.radio("Do you have any known heart problems?"), ["yes, no"])
	with st.expander():
		genre = st.radio("Has anyone in your family died from heart problems?"), ["yes, no"])
	with st.expander():
		genre = st.radio("Has anyone in your family died from a stroke?"), ["yes, no"])
	with st.expander():
		genre = st.radio("Have you ever eenn told by a doctor that you are at risk for OSA"), ["yes, no"])
	with st.expander():
		genre = st.radio("Does/did anyone in your family and/or ancestry have OSA that you are aware of?"), ["yes, no"])



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
	with col2[0]:
		st.write("contact us here!")
		st.markdown("[![Click me](icon.jpeg)](https://www.instagram.com/ananya._.aggarwal/)")
		st.link_button("", "https://www.instagram.com/ananya._.aggarwal/")
	with col2[1]:
		st.write("learn more about me...")



    



			
