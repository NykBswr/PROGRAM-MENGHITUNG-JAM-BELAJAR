import streamlit as st
import time
import streamlit_player
from streamlit_player import st_player, _SUPPORTED_EVENTS
from streamlit_gallery.utils import readme

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
def main():
    with readme("streamlit-player", st_player, __file__):
        c1, c2, c3 = st.columns([3, 3, 2])
        with c3:
            st.subheader("Parameters")
            options = {
                "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
                "progress_interval": 1000,
                "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
                "playing": st.checkbox("Playing", False),
                "loop": st.checkbox("Loop", False),
                "controls": st.checkbox("Controls", True),
                "muted": st.checkbox("Muted", False),
            }
            
            with st.expander("SUPPORTED PLAYERS", expanded=True):
                st.write("""
                - Dailymotion
                - Facebook
                - Mixcloud
                - SoundCloud
                - Streamable
                - Twitch
                - Vimeo
                - Wistia
                - YouTube
                <br/><br/>
                """, unsafe_allow_html=True)
        with c1:
            url = st.text_input("First URL", "https://youtu.be/c9k8K1eII4g")
            event = st_player(url, **options, key="youtube_player")
            st.write(event)
        with c2:
            url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
            event = st_player(url, **options, key="soundcloud_player")
            st.write(event)

if __name__ == "__main__":
    main()

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
