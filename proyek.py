import streamlit as st
import time
from streamlit_player import st_player

st.title('⏳ Pomodoro App ⏳')
st.caption('*Developed by Kelompok 6*')

st.markdown('''
## Apa itu *pomodoro* ?
Teknik Pomodoro adalah teknik pengaturan waktu yang telah diperkenalkan pada akhir tahun 1980 oleh Fransisco Cirillo. 
Pomodoro sendiri dalam Bahasa Spanyol artinya tomat, Cirillo saat masih menjadi mahasiswa menggunakan kitchen timer berbentuk tomat
sebagai pengatur waktu saat belajar.
''')
st.markdown('''
## Cara Menggunakan Pomodoro App
1. Lengkapi data pada menu di samping kiri terkait nama tugas, waktu fokus, waktu istirahat, dan musik pengiring
2. Tekan tombol *Mulai!* untuk memulai timer
3. Kamu dapat melihat timer berjalan dan player musik di sebelah kanan!
4. Ulangi teknik di atas hingga empat kali
''')

side = st.sidebar
side.subheader('Sesuaikan pomodoro senyamanmu!')
form = side.form('data_pomodoro')
tugas = form.text_input('Nama Tugas')
waktu_fokus = form.number_input('Waktu Fokus (menit)', min_value=1, max_value=120)
waktu_istirahat = form.number_input('Waktu Istirahat (menit)', min_value=1, max_value=60)
url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
event = st_player(url, options=pilihan_musik, key="soundcloud_player")

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
    st.write(event)
    timer_fokus(waktu_fokus)
    timer_istirahat(waktu_istirahat)
    st.write('Klik tombol *Mulai!* untuk mengulangi')
    st.write('---')
    st.caption('Terima kasih telah menggunakan pomodoro app 😊')

           
