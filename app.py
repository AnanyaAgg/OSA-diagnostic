import streamlit as st
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import numpy as np
import webbrowser
import joblib

st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Diagnositc Quiz", "More Information", "About me + Contact Us"])
data = np.random.randn(10, 1)

@st.cache_resource
def load_model():
	mod = joblib.load('best_random_forest_model.joblib')
	return mod

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
	if sel_lang=="English":
		st.subheader("What is Obstructive Sleep Apnea?")
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
	if sel_lang=="Spanish":
		st.subheader("¿Qué es la apnea obstructiva del sueño?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("La apnea obstructiva del sueño (AOS) es un trastorno del sueño frecuente que se caracteriza por interrupciones repetidas de la respiración durante el sueño. Estas interrupciones ocurren cuando los músculos de la garganta se relajan excesivamente, lo que hace que las vías respiratorias se estrechen o se cierren parcial o completamente. Como Como resultado, el flujo de aire hacia los pulmones se restringe, lo que provoca breves pausas en la respiración. Estas pausas pueden ocurrir numerosas veces durante la noche, interrumpiendo el ciclo normal del sueño y provocando un sueño fragmentado y de mala calidad.")
			st.write("")
			st.write("El síntoma más común de la apnea obstructiva del sueño son los ronquidos fuertes y persistentes. Otros síntomas incluyen pausas en la respiración durante el sueño, a menudo presenciadas por un compañero de cama, y ​​sensaciones de jadeo o asfixia a medida que se reanuda la respiración. Las personas con AOS también pueden experimentar síntomas diurnos como somnolencia diurna excesiva, dolores de cabeza matutinos, dificultad para concentrarse e irritabilidad. Además, la AOS puede provocar síntomas nocturnos como despertares frecuentes, sudores nocturnos y garganta seca o dolor al despertar.")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("La apnea obstructiva del sueño no tratada puede tener graves consecuencias para la salud. Las repetidas interrupciones de la respiración provocan una desaturación de oxígeno, lo que ejerce presión sobre el sistema cardiovascular y aumenta el riesgo de hipertensión, enfermedades cardíacas y accidentes cerebrovasculares. La AOS también se asocia con trastornos metabólicos como la resistencia a la insulina y la diabetes tipo 2. Además, la AOS no tratada puede contribuir a la fatiga diurna, perjudicando la función cognitiva y aumentando el riesgo de accidentes al conducir o utilizar maquinaria. Además, la interrupción crónica del sueño asociada con la AOS puede afectar negativamente el estado de ánimo y provocar depresión y ansiedad en algunas personas.")
		st.write("---")
	if sel_lang=="Hindi":
		st.subheader("ऑब्सट्रक्टिव स्लीप एपनिया क्या है?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("ऑब्सट्रक्टिव स्लीप एपनिया का सबसे आम लक्षण जोर से और लगातार खर्राटे लेना है। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए से पीड़ित व्यक्तियों को दिन में अत्यधिक नींद आना, सुबह सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन जैसे लक्षणों का भी अनुभव हो सकता है। इसके अलावा, ओएसए रात में लक्षण पैदा कर सकता है जैसे बार-बार जागना, रात में पसीना आना और जागने पर गला सूखना या दर्द होना।")
			st.write("")
			st.write("ऑब्सट्रक्टिव स्लीप एपनिया का सबसे आम लक्षण जोर से और लगातार खर्राटे लेना है। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए से पीड़ित व्यक्तियों को दिन में अत्यधिक नींद आना, सुबह सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन जैसे लक्षणों का भी अनुभव हो सकता है। इसके अलावा, ओएसए रात में लक्षण पैदा कर सकता है जैसे बार-बार जागना, रात में पसीना आना और जागने पर गला सूखना या दर्द होना।")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("अनुपचारित, ऑब्सट्रक्टिव स्लीप एपनिया के गंभीर स्वास्थ्य परिणाम हो सकते हैं। सांस लेने में बार-बार रुकावट से ऑक्सीजन की कमी हो जाती है, जिससे हृदय प्रणाली पर दबाव पड़ता है और उच्च रक्तचाप, हृदय रोग और स्ट्रोक का खतरा बढ़ जाता है। ओएसए इंसुलिन प्रतिरोध और टाइप 2 मधुमेह जैसे चयापचय संबंधी विकारों से भी जुड़ा है। इसके अतिरिक्त, अनुपचारित ओएसए दिन के समय थकान, संज्ञानात्मक कार्य को ख़राब कर सकता है और ड्राइविंग या मशीनरी चलाते समय दुर्घटनाओं के जोखिम को बढ़ा सकता है। इसके अलावा, ओएसए से जुड़ी पुरानी नींद की गड़बड़ी मूड पर नकारात्मक प्रभाव डाल सकती है, जिससे कुछ व्यक्तियों में अवसाद और चिंता हो सकती है।")
		st.write("---")


	
with tab2:
	st.header("Get your AI-backed diagnosis today!")
	with st.form("my_form"):
		with st.expander("What is your gender by birth?"):
			genre = st.radio("", ["male", "female"])
		age = st.slider('What is your age?', 1, 100)
		oc = st.text_input("What is your occupation?")
		sle = st.slider("On average, what is your daily sleep duration in hours?", 1, 24)
		weight = st.slider("How much do you weigh? in lbs", 1, 300)
		height = st.slider("How tall are you? in inches", 1, 84)
		sbp = st.number_input("What is your Systolic blood pressure?", step=1)
		dbp = st.number_input("What is your Diastolic blood pressure?", step=1)
		hr = st.number_input("What is your heart rate?", step=1)
		steps = st.number_input("On average, how many steps do you take in a day?", step=1)
		physical = st.number_input("On average, how many minutes do you workout in a day?", step=1)

		"""For the following questions, answer on a scale of 0-5 about the last month, where 0 = never, 1 = 1-3 days, 2 = ~1 day per week, 3 = 2-4 nights per week, 4 = 5-6 nights per week, and 5 = almost every night"""
		qs1 = st.slider("Experienced difficulty falling asleep?", 0, 5)
		qs2 = st.slider("Woken up at night and easily fell asleep again?", 0, 5)
		qs3 = st.slider("Woken up and had difficulty falling asleep again / difficulty staying asleep?", 0, 5)
		qs4 = st.slider("Non-restorative sleep? i.e. feeling tired or worn-out after getting a usual amount of sleep", 0, 5)

		"""For the following questions, answer on a scale of 0-4 about the last month, where 0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, and 4 = very often"""
		sl1 = st.slider("How often have you been upset because of something that happened unexpectedly?", 0, 4)
		sl2 = st.slider("How often have you felt that you were unable to control the important things in your life?", 0, 4)
		sl3 = st.slider("How often have you felt nervous and stressed?", 0, 4)
		sl4 = st.slider("How often have you felt confident about your ability to handle your personal problems?", 0, 4)
		sl5 = st.slider("How often have you felt that things were going your way?", 0, 4)
		sl6 = st.slider("How often have you found that you could not cope with all the things that you had to do?", 0, 4)
		sl7 = st.slider("How often have you been able to control irritations in your life?", 0, 4)
		sl8 = st.slider("How often have you felt that you were on top of things?", 0, 4)
		sl9 = st.slider("How often have you been angered because of things that happened that were outside of your control?", 0, 4)
		sl10 = st.slider("How often have you felt difficulties were piling up so high that you could not overcome them?", 0, 4)
			  
		sub = st.form_submit_button('Submit my picks')
		if sub:
			qs = (qs1+qs2+qs3+qs4)//2
			sl = (sl1+sl2+sl3+(4-sl4)+(4-sl5)+sl6+(4-sl7)+(4-sl8)+sl9+sl10)//4
			bmi = (weight/(height**2)) * 703
			if bmi < 18.5:
				bm = 0
			elif bmi >= 18.5 and bmi < 25:
				bm = 1
			elif bmi >= 25 and bmi < 30:
				bm = 2
			else:
				bm = 3
			if genre == 'female':
				gn = 0
			else:
				gn = 1
			inp = [[gn,age,sle,qs,physical,sl,bm,hr,steps,sbp,dbp]]
			model = load_model()
			new = model.predict(inp)
			if new == 0:
				st.write("You have a healthy sleep")
			elif new == 1:
				st.write("You might have Insomnia, please visit a doctor")
			elif new == 2:
				st.write("You might have Sleep Apnea, please visit a doctor")

with tab3:
	st.subheader("Find out more about OSA")
	col3 = st.columns(2)
	with col3[0]: 	
		st.write("To find out more about OSA, check out our YouTube channel! We post informative videos about all aspects of OSA and hope to spread awareness about this silent killer. ")
		st.video('https://youtu.be/IIKlqbLwS7M')
		st.video('https://youtu.be/KGEKz4r5n8Q?si=thuPAv_9QfiZTaEP')
	with col3[1]:
		def embed_facebook_post(post_url):
		    embed_code = f'<iframe src="<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02Ygx3GoSYpXKCBMc9CPH4qqA6riPUCQm5dQWgmtX3Dm4cauEVJyg36KW6N1c4gk7Ll%26id%3D61560444242747&show_text=true&width=500" width="500" height="622" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>" width="500" height="600" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
		    st.markdown(embed_code, unsafe_allow_html=True)
		
		# Example usage
		facebook_post_url = "https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.tipranks.com%2Fnews%2Fpress-releases%2Fpap-therapy-reduces-hospitalizations-by-31-and-er-visits-by-23-for-people-with-obstructive-sleep-apnea-and-comorbid-insomnia&h=AT0AjeDIWDRATF0oCMWJJjjwJXF3j9ugmbMgnn_ucAlUU9lEytUJK_0SDSWU-wbdRYNoDRrJwHCEZ1rCh6z05qGMy6lh70ou07eNzlsFz9jN8UDR7nhKLdMeAj0vi4kkwDUi97_EGg&s=1"
		embed_facebook_post(facebook_post_url)

with tab4:
	col4 = st.columns(2)
	with col4[0]:
		st.subheader("About Me")
		st.write("Hello! I am Ananya Aggarwal, a highschooler in Fremont, CA. I started this project to raise awareness about obstructive sleep apnea, as extrmemly widespread sleep disorder around the world. I was shocked by the number of my own family members and friends who were affected by the disorder and realized the problem is much bigger than expected. After doing research about OSA and its treatments, I realized that a big contributing factor to the lack of patient diagnosis for OSA is the expense and inavailblity of its diagnosis options. The most common diagnosis option for OSA, sleep tests, are expensive and not always easy to access, making it hard for possible OSA pateints to seek early diagnosis and therefore more effective treatment. My intelligent diagnostic quiz briges this gap between suspecting patients and professional diagnosis. The quiz is free to all and available on all web browsers. It provides users a prediction of how at-risk/likely they are to have obstructive sleep apnea, informing them of whether they are should get checked for it soon. My goals with this project are to raise the awareness for OSA in general and to gain popularity for my  quiz to provide a free first step to OSA patient's diagnosis and treatment journey!")
	with col4[1]:
		st.subheader("Contact Us")
		st.write("Contact us here!")
		st.write("Email: apneaassist@gmail.com")
		st.link_button("YouTube", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
		st.link_button("FaceBook", "https://www.facebook.com/profile.php?id=61560444242747")
	

    



			
