import streamlit as st 
st.title ("About")
st.info(" This is about the page ")
st.success("This is a test")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")

height = st.slider("Enter your height", min_value=0,max_value=200,value=100, step =10)

dic = { 'name': name,'age': age, 'height': height}
df = pd.DataFrame(dic, index = [0])

st.write(df)

