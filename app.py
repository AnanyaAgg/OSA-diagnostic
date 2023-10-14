import streamlit as st
from ultralytics import YOLO
from PIL import Image
st.title('my classification app')
st.markdown (f'''
<style>
.stApp {
background-image: url("https://img.freepik.com/free-vector/abstract-medical-wallpaper-template-design_53876-61802.jpg?w=1800&t=st=1689312423~exp=1689313023~hmac=b81f19f0fa8493e07a3a32fc33ca6365ad7aaf99cdc2bbb02c18eaa5e5c77da0");
background-size: cover;
}
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

