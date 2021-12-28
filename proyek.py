import streamlit as st
from streamlit_player import st_player
import time

st.markdown('''
## WELCOME TO MY PROGRAM* ?
Disini kita akan belajar dan mendengarkan sesuatu yang unik.
''')

side = st.sidebar
side.subheader('Sesuaikan pomodoro senyamanmu!')
form = side.form('data_pomodoro')
tugas = form.text_input('Nama Tugas')
waktu_fokus = form.number_input('Waktu Fokus (menit)', min_value=1, max_value=120)
waktu_istirahat = form.number_input('Waktu Istirahat (menit)', min_value=1, max_value=60)
# Embed a youtube video
st_player("https://youtu.be/CmSKVW1v0xM")

# Embed a music from SoundCloud
st_player("https://soundcloud.com/imaginedragons/demons")

mulai = form.form_submit_button('Mulai !')

waktu_fokus *= 60
waktu_istirahat *= 60

def timer_fokus(waktu_fokus):
    with col1.empty():
        while waktu_fokus:
            mins, secs = divmod(waktu_fokus, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.subheader(f"⏳ Waktu fokus *{timer}* ⏳")            
            time.sleep(1)
            waktu_fokus -= 1
            st.success("🔔 Waktu fokus selesai! Anda dapat istirahat sejenak")

def timer_istirahat(waktu_istirahat):
    with col1.empty():
        while waktu_istirahat:
            mins, secs = divmod(waktu_istirahat, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.subheader(f"⏳ Waktu istirahat *{timer}* ⏳")            
            time.sleep(1)
            waktu_istirahat -= 1
            st.error("⏰ Waktu istirahat selesai!")

if mulai:
    st.header(tugas)
    col1, col2 = st.columns(2)
    col1.write('*Tetaplah fokus hingga timer selesai!*')
    col2.write('Putar musikmu disini!')
    timer_fokus(waktu_fokus)
    timer_istirahat(waktu_istirahat)
    st.write('Klik tombol *Mulai!* untuk mengulangi')
    st.write('---')
    st.caption('Terima kasih telah menggunakan pomodoro app 😊')
