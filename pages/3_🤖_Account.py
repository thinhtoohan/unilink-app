import streamlit as st
st.title("🎓 UniLink 🎓")
st.divider()
if(st.session_state["usr_stats"]==""):
    st.header("Find peers using our search tool!")
else:
    st.header("Following peers are most similar to you.")
    st.header("Connect with them!")
    usr_stats = st.session_state["usr_stats"]
    def calculateScore(usr1:list[str], usr2:list[str]) -> int:
        matchScore = 0
        eduLevel = {'Freshman':0,
                    'Sophomore':0.2,
                    'Junior':0.4,
                    'Senior':0.6,
                    'Masters':0.8,
                    'PhD':1}
        for i in range(3):
            matchScore+=0.2*(usr1[i]==usr2[i])
        usr1_lvl = eduLevel[usr1[3]]
        usr2_lvl = eduLevel[usr2[3]]
        matchScore+=0.2*(1-abs(usr1_lvl-usr2_lvl))
        return ("%.2f"%matchScore)

    students_list = []
    import json 
    import ast
    scores = []
    # reading the data from the file 
    students = open('students.txt',"r") 
    for student in students:
        students_list.append(json.loads(student))
    for i in students_list:
        for v in i.values():
            v = ast.literal_eval(v)
            score = calculateScore(usr_stats,v)
            scores.append(score)
    n = 3
    # Get indices of the largest n elements
    indices = sorted(range(len(scores)), key=lambda x: scores[x], reverse=True)[:n]
    for index in indices:
        value_list = ast.literal_eval(list(students_list[index].values())[0])
    # reconstructing the data as a dictionary 
    st.markdown("""
    <style>
        .st-emotion-cache-1v0mbdj > img{
        border-radius: 50%;
        }
    </style>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/Avatar_Dog_1.webp",width=100)
        st.subheader(list(students_list[indices[0]])[0])
        value_list = ast.literal_eval(list(students_list[indices[0]].values())[0])
        for a in value_list:
            st.write(a)
        if(st.button("Chat",key="Chat1")):
            st.switch_page("pages/4_💬_Chat.py")
    

    with col2:
        st.image("assets/Avatar_Penguin.webp",width=100)
        st.subheader(list(students_list[indices[1]])[0])
        value_list = ast.literal_eval(list(students_list[indices[1]].values())[0])
        for a in value_list:
            st.write(a)
        if(st.button("Chat",key="Chat2")):
            st.switch_page("pages/4_💬_Chat.py")
    

    with col3:
        st.image("assets/Avatar_Dog_2.webp",width=100)
        st.subheader(list(students_list[indices[2]])[0])
        value_list = ast.literal_eval(list(students_list[indices[2]].values())[0])
        for a in value_list:
            st.write(a)
        if(st.button("Chat",key="Chat3")):
            st.switch_page("pages/4_💬_Chat.py")
  