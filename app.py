import streamlit as st
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import numpy as np
import webbrowser

st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Diagnositc Quiz", "More Information", "About me + Contact Us"])
data = np.random.randn(10, 1)

with tab1:
	st.subheader("What is Obstructive Sleep Apnea")
	st.write("")
	col = st.columns(2)
	with col[0]:
		st.write("Obstructive sleep apnea (OSA) is a prevalent sleep disorder characterized by repeated interruptions in breathing during sleep. These interruptions occur when the muscles in the throat relax excessively, causing the airway to narrow or close partially or completely. As a result, the flow of air into the lungs is restricted, leading to brief pauses in breathing. These pauses can occur numerous times throughout the night, disrupting the normal sleep cycle and leading to fragmented and poor-quality sleep.")
		st.write("")
		st.write("The most common symptom of obstructive sleep apnea is loud and persistent snoring. Other symptoms include pauses in breathing during sleep, often witnessed by a bed partner, and gasping or choking sensations as breathing resumes. Individuals with OSA may also experience daytime symptoms such as excessive daytime sleepiness, morning headaches, difficulty concentrating, and irritability. Furthermore, OSA can lead to nocturnal symptoms such as frequent awakenings, night sweats, and a dry or sore throat upon waking.")
		st.image('apneapic.png')
	with col[1]:
		st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
		st.write("Untreated, obstructive sleep apnea can have serious health consequences. The repeated interruptions in breathing lead to oxygen desaturation, putting strain on the cardiovascular system and increasing the risk of hypertension, heart disease, and stroke. OSA is also associated with metabolic disorders such as insulin resistance and type 2 diabetes. Additionally, untreated OSA can contribute to daytime fatigue, impairing cognitive function and increasing the risk of accidents while driving or operating machinery. Moreover, the chronic sleep disruption associated with OSA can negatively impact mood, leading to depression and anxiety in some individuals.")
	st.write("---")
with tab2:
	st.header("Get your AI-backed diagnosis today!")
	st.write("Quiz coming soon!")



with tab3:
	st.subheader("Find out more about OSA")
	st.write("To find out more about OSA, check out our YouTube channel! We post informative videos about all aspects of OSA and hope to spread awareness about this silent killer. ")
	st.video('https://youtu.be/IIKlqbLwS7M')

with tab4:
	col2 = st.columns(2)
	with col2[0]:
		st.subheader("About Me")
		st.write("Hello! I am Ananya Aggarwal, a highschooler in Fremont, CA. I started this project to raise awareness about obstructive sleep apnea, as extrmemly widespread sleep disorder around the world. I was shocked by the number of my own family members and friends who were affected by the disorder and realized the problem is much bigger than expected. After doing research about OSA and its treatments, I realized that a big contributing factor to the lack of patient diagnosis for OSA is the expense and inavailblity of its diagnosis options. The most common diagnosis option for OSA, sleep tests, are expensive and not always easy to access, making it hard for possible OSA pateints to seek early diagnosis and therefore more effective treatment. My intelligent diagnostic quiz briges this gap between suspecting patients and professional diagnosis. The quiz is free to all and available on all web browsers. It provides users a prediction of how at-risk/likely they are to have obstructive sleep apnea, informing them of whether they are should get checked for it soon. My goals with this project are to raise the awareness for OSA in general and to gain popularity for my  quiz to provide a free first step to OSA patient's diagnosis and treatment journey!")
	with col2[1]:
		st.subheader("Contact Us")
		st.write("Contact us here!")
		st.write("Email: apneaassist@gmail.com")
		st.link_button("YouTube", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
		st.link_button("FaceBook", "https://www.facebook.com/profile.php?id=61560444242747")
	

    



			
