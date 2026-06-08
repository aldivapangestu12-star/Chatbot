import streamlit as st
from database import faq_database

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Chatbot PMB UPGRISBA",
    page_icon="🎓",
    layout="wide"
)

# ==================================
# LOAD CSS
# ==================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==================================
# DEFAULT MESSAGE
# ==================================

default_message = {
    "role":"assistant",
    "content":
    """
Halo 👋

Selamat datang di Chatbot PMB UPGRISBA.

Silakan tanyakan mengenai:

🎓 Jurusan Sains Data
💰 Biaya Kuliah
🎓 Beasiswa
📅 Jadwal PMB
🏢 Fasilitas
💼 Prospek Karir
"""
}

# ==================================
# SESSION
# ==================================

if "messages" not in st.session_state:
    st.session_state.messages = [default_message]

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("🎓 PMB UPGRISBA")

st.sidebar.info("""
Program Studi S1 Sains Data

✅ Artificial Intelligence

✅ Machine Learning

✅ Big Data

✅ Data Analytics
""")

if st.sidebar.button("🗑️ Reset Chat"):
    st.session_state.messages = [default_message]
    st.rerun()

# ==================================
# HEADER
# ==================================

st.markdown("""
<div class="title-box">
<h1>🎓 Chatbot PMB UPGRISBA</h1>
<p>Program Studi Sains Data</p>
</div>
""", unsafe_allow_html=True)

# ==================================
# DASHBOARD
# ==================================

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-box">
    <h2>1.245</h2>
    <p>Pendaftar</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
    <h2>5</h2>
    <p>Beasiswa</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
    <h2>B</h2>
    <p>Akreditasi</p>
    </div>
    """, unsafe_allow_html=True)

# ==================================
# CHAT
# ==================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input(
    "Tanyakan sesuatu..."
)

if prompt:

    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    response = """
Maaf, informasi belum tersedia.

Silakan hubungi admin PMB.
"""

    text = prompt.lower()

    for keywords, answer in faq_database.items():

        if any(keyword in text for keyword in keywords):

            response = answer
            break

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role":"assistant",
        "content":response
    })
