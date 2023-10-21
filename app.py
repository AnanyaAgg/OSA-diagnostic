import streamlit as st
from ultralytics import YOLO
from PIL import Image
import streamlit as st
import numpy as np

tab1, tab2, tab3 = st.tabs(["Home", "Demo", "About Me"])
data = np.random.randn(10, 1)

tab1.subheader("What is AIML?")
tab1.write("AIML stands for artificial inteligence machine learning. Essentially, AIML is the process of teaching a computer to problem solve and to replicate the human brain's logic to create its own knowledge after being trained with a dataset.")

tab2.subheader("Try the model!")
tab2.markdown (f'''
<style>
.stApp {{
background-image: url("https://images.unsplash.com/photo-1697222691126-c1be7bde3ac5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1248&q=80");
background-size: cover;
}}
</style>
''', unsafe_allow_html=True)

@st.cache_resource
def my_model():
	model = YOLO('best.pt')
	return model
# st.file_uploader sends the image or video from the computer to the server
img = tab2.file_uploader('upload an image of your pet!')

if img is not None:
	im = Image.open(img)
	tab2.image(im)
	mod = my_model()
	res = mod.predict(im)
	temp = res[0].probs.top5
	conf = res[0].probs.top5conf
	conf = conf.tolist()
	col = tab2.columns(2)
	with col[0]:
		for i in temp:
			tab2.write(res[0].names[i])
	with col[1]:
		for i in conf:
			tab2.write(str(i))
	tab2.success('congrats!')
tab3.subheader("About Me!")
tab3.write("Hi! I am a junior in High School and I live in the Bay Area.")




