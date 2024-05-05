import streamlit as st

st.title("🎓 UniLink 🎓")
st.divider()
if 'usr_stats' not in st.session_state:
    st.session_state['usr_stats'] = ''
st.header("Connect. Collaborate. Succeed.")
st.markdown('<div style="text-align: justify;">Welcome to UniLink, the ultimate platform for students to connect with peers across all California State University campuses. Our goal is to build a vibrant community that brings together students who share similar academic interests or cultural backgrounds, fostering collaboration and creating lasting connections.</div>', unsafe_allow_html=True)
st.header("What We Offer")
st.markdown('- <div style="text-align: justify;">Major-Based Communities: Find and connect with other students pursuing the same major, whether you\'re a Freshman or a PhD candidate. Share resources, discuss coursework, and collaborate on projects with peers who understand your academic journey.</div>',unsafe_allow_html=True)
st.markdown('- <div style="text-align: justify;">Country-Based Communities: Whether you\'re an international student or a student interested in specific cultures, you can find others from the same country or region. Share your experiences, celebrate traditions, and build a supportive network.</div>',unsafe_allow_html=True)
st.markdown('- <div style="text-align: justify;">Cross-Campus Collaboration: Our app bridges the gap between campuses, allowing you to expand your network across the entire California State University system. Gain insights from students at other campuses and create opportunities for intercampus collaboration.</div>',unsafe_allow_html=True)
st.header("Get Started Today")
st.markdown('<div style="text-align: justify;">Join UniLink and start connecting with students from your major or country, across all California State University campuses. Whether you\'re looking to collaborate on academic projects, make new friends, or build a professional network, UniLink is here to help you succeed.</div>',unsafe_allow_html=True)