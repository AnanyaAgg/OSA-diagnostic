import streamlit as st
from ultralytics import YOLO
from PIL import Image
st.title('my classification app')
st.markdown (f'''
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
img = st.file_uploader('upload an image of your pet!')

if img is not None:
	im = Image.open(img)
	st.image(im)
	mod = my_model()
	res = mod.predict(im)
	temp = res[0].probs.top5
	conf = res[0].probs.top5conf
	conf = conf.tolist()
	col = st.columns(2)
	with col[0]:
		for i in temp:
			st.write(res[0].names[i])
	with col[1]:
		for i in conf:
			st.write(str(i))
	st.success('congrats!')




