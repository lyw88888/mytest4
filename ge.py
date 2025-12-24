import streamlit as st
st.set_page_config(page_title='音乐播放器')

music_url =[
    {
        'musicurl':'https://music.163.com/song/media/outer/url?id=3312734747.mp3',
        'imgurl':'http://p2.music.126.net/Qlau9o7vEllouRV9x7qEKg==/109951172215963831.jpg?param=130y130',
        'text':'Pretty-王鹤棣'
        },
    {
        'musicurl':'https://music.163.com/song/media/outer/url?id=3312735541.mp3',
        'imgurl':'http://p1.music.126.net/vJPca_ni17kyiBs82J2LCA==/109951172215963424.jpg?param=130y130',
        'text':'优雅-王鹤棣'
        },
    {
        'musicurl':'https://music.163.com/song/media/outer/url?id=864100675.mp3',
        'imgurl':'https://p1.music.126.net/z5jrOL-OSXWKfQjyPJas8w==/109951163093838994.jpg?param=130y130',
        'text':'For You-王鹤棣'
        },

    ]
if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.image(music_url[st.session_state['ind']]['imgurl'])

st.text(music_url[st.session_state['ind']]['text'])

st.audio(music_url[st.session_state['ind']]['musicurl'])

c1,c2=st.columns(2)

def lastMusic():
    st.session_state['ind']=(st.session_state['ind']-1) % len(music_url)

def nextMusic():
    st.session_state['ind']=(st.session_state['ind']+1) % len(music_url)

with c1:
    st.button('上一首',use_container_width=True,on_click=lastMusic)

with c2:
    st.button('下一首',use_container_width=True,on_click=nextMusic)
