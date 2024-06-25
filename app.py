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
	engInfo = "What is Obstructive Sleep Apnea? Obstructive sleep apnea (OSA) is a prevalent sleep disorder characterized by repeated interruptions in breathing during sleep. These interruptions occur when the muscles in the throat relax excessively, causing the airway to narrow or close partially or completely. As a result, the flow of air into the lungs is restricted, leading to brief pauses in breathing. These pauses can occur numerous times throughout the night, disrupting the normal sleep cycle and leading to fragmented and poor-quality sleep. The most common symptom of obstructive sleep apnea is loud and persistent snoring. Other symptoms include pauses in breathing during sleep, often witnessed by a bed partner, and gasping or choking sensations as breathing resumes. Individuals with OSA may also experience daytime symptoms such as excessive daytime sleepiness, morning headaches, difficulty concentrating, and irritability. Furthermore, OSA can lead to nocturnal symptoms such as frequent awakenings, night sweats, and a dry or sore throat upon waking. Untreated, obstructive sleep apnea can have serious health consequences. The repeated interruptions in breathing lead to oxygen desaturation, putting strain on the cardiovascular system and increasing the risk of hypertension, heart disease, and stroke. OSA is also associated with metabolic disorders such as insulin resistance and type 2 diabetes. Additionally, untreated OSA can contribute to daytime fatigue, impairing cognitive function and increasing the risk of accidents while driving or operating machinery. Moreover, the chronic sleep disruption associated with OSA can negatively impact mood, leading to depression and anxiety in some individuals."
	hindiInfo = "ऑब्सट्रक्टिव स्लीप एपनिया क्या है? ऑब्सट्रक्टिव स्लीप एपनिया (ओएसए) एक प्रचलित नींद विकार है, जिसमें नींद के दौरान सांस लेने में बार-बार रुकावट आती है। ये रुकावट तब होती है जब गले की मांसपेशियां अत्यधिक शिथिल हो जाती हैं, जिससे वायुमार्ग संकीर्ण या आंशिक या पूरी तरह से बंद हो जाता है। नतीजतन, फेफड़ों में हवा का प्रवाह प्रतिबंधित हो जाता है, जिससे सांस लेने में थोड़ी रुकावट आती है। ये रुकावट रात भर में कई बार हो सकती है, जिससे सामान्य नींद चक्र बाधित होता है और खंडित और खराब गुणवत्ता वाली नींद आती है ऑब्सट्रक्टिव स्लीप एपनिया में तेज और लगातार खर्राटे आते हैं। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए वाले व्यक्तियों को दिन के समय अत्यधिक नींद आना जैसे लक्षणों का भी अनुभव हो सकता है इसके अलावा, सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन, ओएसए के कारण रात में बार-बार जागना, रात में पसीना आना और जागने पर गले में सूखापन या खराश जैसे लक्षण हो सकते हैं। अनुपचारित, ऑब्सट्रक्टिव स्लीप एपनिया के गंभीर स्वास्थ्य परिणाम हो सकते हैं। सांस लेने में बार-बार रुकावट से ऑक्सीजन की कमी हो जाती है, जिससे हृदय प्रणाली पर दबाव पड़ता है और उच्च रक्तचाप, हृदय रोग और स्ट्रोक का खतरा बढ़ जाता है। ओएसए इंसुलिन प्रतिरोध और टाइप 2 मधुमेह जैसे चयापचय संबंधी विकारों से भी जुड़ा है। इसके अतिरिक्त, अनुपचारित ओएसए दिन के समय थकान, संज्ञानात्मक कार्य को ख़राब कर सकता है और ड्राइविंग या मशीनरी चलाते समय दुर्घटनाओं के जोखिम को बढ़ा सकता है। इसके अलावा, ओएसए से जुड़ी पुरानी नींद की गड़बड़ी मूड पर नकारात्मक प्रभाव डाल सकती है, जिससे कुछ व्यक्तियों में अवसाद और चिंता हो सकती है।"
	spanInfo = "¿Qué es la apnea obstructiva del sueño? La apnea obstructiva del sueño (AOS) es un trastorno del sueño frecuente que se caracteriza por interrupciones repetidas de la respiración durante el sueño. Estas interrupciones ocurren cuando los músculos de la garganta se relajan excesivamente, lo que hace que las vías respiratorias se estrechen o se cierren parcial o completamente. Como resultado, el flujo de aire hacia los pulmones se restringe, lo que provoca breves pausas en la respiración. Estas pausas pueden ocurrir numerosas veces durante la noche, lo que altera el ciclo normal del sueño y provoca un sueño fragmentado y de mala calidad. La apnea obstructiva del sueño son ronquidos fuertes y persistentes. Otros síntomas incluyen pausas en la respiración durante el sueño, a menudo presenciadas por un compañero de cama, y ​​sensación de jadeo o asfixia cuando se reanuda la respiración. Las personas con AOS también pueden experimentar síntomas diurnos como somnolencia diurna excesiva, por la mañana. Dolores de cabeza, dificultad para concentrarse e irritabilidad. Además, la AOS puede provocar síntomas nocturnos como despertares frecuentes, sudores nocturnos y garganta seca o dolor al despertar. La apnea obstructiva del sueño no tratada puede tener graves consecuencias para la salud. Las repetidas interrupciones de la respiración provocan una desaturación de oxígeno, lo que ejerce presión sobre el sistema cardiovascular y aumenta el riesgo de hipertensión, enfermedades cardíacas y accidentes cerebrovasculares. La AOS también se asocia con trastornos metabólicos como la resistencia a la insulina y la diabetes tipo 2. Además, la AOS no tratada puede contribuir a la fatiga diurna, perjudicando la función cognitiva y aumentando el riesgo de accidentes al conducir o utilizar maquinaria. Además, la interrupción crónica del sueño asociada con la AOS puede afectar negativamente al estado de ánimo, provocando depresión y ansiedad en algunos individuos."
	languages = {"English": engInfo, "Spanish": spanInfo, "Hindi": hindiInfo}

	query_parameters = st.experimental_get_query_params()
	if "lang" not in query_parameters:
  	  st.experimental_set_query_params(lang="en")
  	  st.experimental_rerun()


	def set_language() -> None:
	    if "selected_language" in st.session_state:
	        st.experimental_set_query_params(
   	         lang=languages.get(st.session_state["selected_language"])
   	     )


	sel_lang = st.radio(
	    "Language",
 	   options=languages,
	    horizontal=True,
	    on_change=set_language,
	    key="selected_language",
	)

	st.markdown(f"Selected Language: {sel_lang}")
	st.write(sel_lang)

		
	st.subheader("What is Obstructive Sleep Apnea")
	st.write("")
	col = st.columns(2)
	with col[0]:
		st.markdown(f"""{query_parameters.get("lang")[0]}""")
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
	with st.form("my_form"):
		with st.expander("What is your gender by birth?"):
			genre = st.radio("", ["male", "female", "prefer not to say"])
		st.slider('What is your age?', 1, 100)
		st.text_input("What is your occupation?")
		st.slider("On average, what is your daily sleep duration in hours?", 1, 24)
		st.slider("How much do you weigh? in lbs", 1, 300)
		st.slider("How tall are you? in inches", 1, 84)
		st.text_input("What is your blood pressure?")
		st.number_input("What is your heart rate?")
		st.number_input("On average, how many steps do you take in a day?")

		'''For the following questions, answer on a scale of 0-5 about the last month, where 0 = never, 1 = 1-3 days, 2 = ~1 day per week, 3 = 2-4 nights per week, 4 = 5-6 nights per week, nd 5 = almost every night'''
		st.slider("Experienced difficulty falling asleep?", 0, 5)
		st.slider("Woken up at night and easily fell asleep again?", 0, 5)
		st.slider("Woken up and had difficulty falling asleep again / difficulty staying asleep?", 0, 5)
		st.slider("Non-restorative sleep? i.e. feeling tired or worn-out after getting a usual amount of sleep", 0, 5)
		
		'''For the following questions, answer on a scale of 0-4 about the last month, where 0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, and 4 = very often'''
		st.slider("How often have you been upset because of something that happened unexpectedly?", 0, 4)
		st.slider("How often have you felt that you were unable to control the important things in your life?", 0, 4)
		st.slider("How often have you felt nervous and stressed?", 0, 4)
		st.slider("How often have you felt confident about your ability to handle your personal problems?", 0, 4)
		st.slider("How often have you felt that things were going your way?", 0, 4)
		st.slider("How often have you found that you could not cope with all the things that you had to do?", 0, 4)
		st.slider("How often have you been able to control irritations in your life?", 0, 4)
		st.slider("How often have you felt that you were on top of things?", 0, 4)
		st.slider("How often have you been angered because of things that happened that were outside of your control?", 0, 4)
		st.slider("How often have you felt difficulties were piling up so high that you could not overcome them?", 0, 4)
			  
		st.form_submit_button('Submit my picks')



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
	

    



			
