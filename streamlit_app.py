import streamlit as st
import base64

st.title("Estadísticas Liga Arco Mexicana del Pacífico")
st.write("¿Qué quieres explorar el día de hoy?:")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

st.subheader("LMP Bateo", divider='gray')
bat_image = "field_4.jpg"  

bat_image_encoded = get_base64_image(bat_image)

st.markdown(f'''
<div style="position: relative; display: inline-block; text-align: center;">
  <img src="data:image/jpeg;base64,{bat_image_encoded}" width="300">
  <a href="https://lmp-batting-stats.streamlit.app" target="_blank">
    <button style="
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #4b7240;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 20px;
      cursor: pointer;
      font-size: 16px;
    ">Bateo LMP</button>
  </a>
</div>
''', unsafe_allow_html=True)

st.subheader("Lanzadores LMP", divider='gray')
ball_image = "baseball_2.jpg"

ball_image_encoded = get_base64_image(ball_image)

st.markdown(f'''
<div style="position: relative; display: inline-block; text-align: center;">
  <img src="data:image/jpeg;base64,{ball_image_encoded}" width="300">
  <a href="https://lmp-pitching-stats.streamlit.app" target="_blank">
    <button style="
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #9a1620 ;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 20px;
      cursor: pointer;
      font-size: 16px;
    ">Pitcheo LMP</button>
  </a>
</div>
''', unsafe_allow_html=True)

st.subheader("Uso del Bullpen", divider='gray')
team_image = "bullpen.jpg"

team_image_encoded = get_base64_image(team_image)

st.markdown(f'''
<div style="position: relative; display: inline-block; text-align: center;">
  <img src="data:image/jpeg;base64,{team_image_encoded}" width="300">
  <a href="https://lmp-bullpen.streamlit.app/" target="_blank">
    <button style="
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #724940;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 20px;
      cursor: pointer;
      font-size: 16px;
    ">Bullpen</button>
  </a>
</div>
''', unsafe_allow_html=True)
