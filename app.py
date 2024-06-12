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
	st.write("")
	col = st.columns(2)
	with col[0]:
		st.write("Obstructive sleep apnea (OSA) is a prevalent sleep disorder characterized by repeated interruptions in breathing during sleep. These interruptions occur when the muscles in the throat relax excessively, causing the airway to narrow or close partially or completely. As a result, the flow of air into the lungs is restricted, leading to brief pauses in breathing. These pauses can occur numerous times throughout the night, disrupting the normal sleep cycle and leading to fragmented and poor-quality sleep.")
		st.write("The most common symptom of obstructive sleep apnea is loud and persistent snoring. Other symptoms include pauses in breathing during sleep, often witnessed by a bed partner, and gasping or choking sensations as breathing resumes. Individuals with OSA may also experience daytime symptoms such as excessive daytime sleepiness, morning headaches, difficulty concentrating, and irritability. Furthermore, OSA can lead to nocturnal symptoms such as frequent awakenings, night sweats, and a dry or sore throat upon waking.")
	with col[1]:
		st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
		st.write("Untreated obstructive sleep apnea can have serious health consequences. The repeated interruptions in breathing lead to oxygen desaturation, putting strain on the cardiovascular system and increasing the risk of hypertension, heart disease, and stroke. OSA is also associated with metabolic disorders such as insulin resistance and type 2 diabetes. Additionally, untreated OSA can contribute to daytime fatigue, impairing cognitive function and increasing the risk of accidents while driving or operating machinery. Moreover, the chronic sleep disruption associated with OSA can negatively impact mood, leading to depression and anxiety in some individuals.")
with tab2:
	st.header("Get your AI-backed diagnosis today!")
	'''general questions'''
	with st.expander("What is your age?"):
		genre = st.radio("", ["<20", "20-30", "30-40", "40-50", "50-60", ">60"])
	with st.expander("What is your gender by birth?"):
		genre = st.radio("", ["male", "female", "prefer not to say"])
	with st.expander("How much do you weigh?"):
		genre = st.radio("", ["<100 lbs", "100-150 lbs", "150-200 lbs", ">200 lbs"])
	with st.expander("How tall are you? (ft, in)"):
		genre = st.radio("", ["how wld i use double quotes in text?"])

	"""experience with common symptoms"""
	with st.expander("How often do you snore?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"])
	with st.expander("Do you snore loudly (louder than talking or loud enough to be heard through closed doors)"):
		genre = st.radio("", ["yes", "no"])
	with st.expander("Has anyone noticed that you quit breathing during your sleep?"):
		genre = st.radio("", ["yes, multiple times", "yes, only once or twice", "no, never"])
	with st.expander("Do you use any medication (pills, gummies, etc.) to fall asleep?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"], key = 1)
	with st.expander("Are you tired after sleeping?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"], key = 2)
	with st.expander("Are you tired during awake time?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"], key = 3)
	with st.expander("Have you ever nodded off or fallen asleep while driving? If yes, how often?"):
		genre = st.radio("", ["yes, aLmost every day", "yes, at least once a week", "yes, very rarely", "no. never"], key = 4)
	with st.expander("Do you often have headaches in the morning?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"], key = 5)
	with st.expander("Do you have trouble remembering things?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"], key = 6)
	with st.expander("Do you have trouble with basic problem-solving/logic questions?"):
		genre = st.radio("", ["almost every day", "3-4 times a week", "less than that"], key = 7)
	
	"""other health questions"""
	with st.expander("Do you have or are you being trated for high blood pressure"):
		genre = st.radio("", ["yes", "no"], key = 8)
	with st.expander("Do you have any known heart problems?"):
		genre = st.radio("", ["yes", "no"], key = 9)
	with st.expander("Has anyone in your family died from heart problems?"):
		genre = st.radio("", ["yes", "no"], key = 10)
	with st.expander("Has anyone in your family died from a stroke?"):
		genre = st.radio("", ["yes", "no"], key = 11)
	with st.expander("Have you ever eenn told by a doctor that you are at risk for OSA"):
		genre = st.radio("", ["yes", "no"], key = 12)
	with st.expander("Does/did anyone in your family and/or ancestry have OSA that you are aware of?"):
		genre = st.radio("", ["yes", "no"], key = 13)



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



    



			
