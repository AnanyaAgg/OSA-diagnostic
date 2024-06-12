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
		st.write("")
		st.write("The most common symptom of obstructive sleep apnea is loud and persistent snoring. Other symptoms include pauses in breathing during sleep, often witnessed by a bed partner, and gasping or choking sensations as breathing resumes. Individuals with OSA may also experience daytime symptoms such as excessive daytime sleepiness, morning headaches, difficulty concentrating, and irritability. Furthermore, OSA can lead to nocturnal symptoms such as frequent awakenings, night sweats, and a dry or sore throat upon waking.")
		st.image('https://sa1s3optim.patientpop.com/assets/images/provider/photos/2429309.png')
	with col[1]:
		st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
		st.write("Untreated, obstructive sleep apnea can have serious health consequences. The repeated interruptions in breathing lead to oxygen desaturation, putting strain on the cardiovascular system and increasing the risk of hypertension, heart disease, and stroke. OSA is also associated with metabolic disorders such as insulin resistance and type 2 diabetes. Additionally, untreated OSA can contribute to daytime fatigue, impairing cognitive function and increasing the risk of accidents while driving or operating machinery. Moreover, the chronic sleep disruption associated with OSA can negatively impact mood, leading to depression and anxiety in some individuals.")
with tab2:
	st.header("Get your AI-backed diagnosis today!")
	st.write("Quiz coming soon!")



with tab3:
	st.subheader("Find out more about OSA")
	col = st.columns(2)
	with col[0]:
		st.write("To find out more about OSA, check out our YouTube channel! We post informative videos about all aspects of OSA and hope to spread awareness about this silent killer. ")
	with col[1]:
		st.video('https://youtu.be/IIKlqbLwS7M')

with tab4:
	st.subheader("Contact Us & About Me")
	col2 = st.columns(2)
	with col2[0]:
		st.write("contact us here!")
		st.markdown("[![Click me](icon.jpeg)](https://www.instagram.com/ananya._.aggarwal/)")
		st.link_button("", "https://www.instagram.com/ananya._.aggarwal/")
	with col2[1]:
		st.write("learn more about me...")



    



			
