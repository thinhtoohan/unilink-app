import streamlit as st

st.title("🎓 UniLink 🎓")
st.divider()
countries_list = []
campuses_list = []
countries = open("countries.txt", "r")
campuses = open("campuses.txt","r")

for country in countries:
    countries_list.append(country)
for campus in campuses:
    campuses_list.append(campus)
usr_country = st.selectbox('Select Home Country',countries_list,index=186)
usr_campus = st.selectbox('Select Your Campus',campuses_list,index=18)
usr_major = st.selectbox('Select Your Major Group',('Sciences and Engineering', 
                                                    'Social Sciences',
                                                    'Arts and Humanities',
                                                    'Natural Sciences',
                                                    'Health Sciences',
                                                    'Business and Economics',
                                                    'Education and Teaching',
                                                    'Fine and Applied Arts',
                                                    'Communications and Media',
                                                    'Law and Legal Studies'))
usr_academic_year = st.selectbox(
    'Select Program Year',
    ('Freshman','Sophomore','Junior','Senior','Masters','PhD'))
if st.button("Search",type="primary"):
    usr_stats = [usr_campus.strip(),usr_country.strip(),usr_major,usr_academic_year]
    st.session_state["usr_stats"] = usr_stats
    st.switch_page("pages/3_🤖_Account.py")