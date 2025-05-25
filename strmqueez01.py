import streamlit as st

st.set_page_config(page_title = "Quiz App")
quiz = [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Monaco"], "answer": "Paris"},
    {"question": " 2.5 + 2.5 = ?", "options": ["4", "4.5", "5", "5.5"], "answer": "5"},
    {"question": "Who wrote Hamlet?", "options": ["Shakespeare", "Hemingway", "Tolkien", "Oluwole Soyinka"], "answer": "Shakespeare"},
    {"question": "Where is Dammy Solutions Coaching Clinic located?", "options": ["Enuwa", "Phase 2", "Agbedegbede", "Mokuro"], "answer": "Agbedegbede"},
    {"question": "Who invented the electric bulb?", "options": ["Nikola Tesla", "Marie Curie", "Thomas Edison", "Albert Einstein"], "answer": "Thomas Edison"},
    {"question": "What phenomenon does the water in a narrow tube follow?", "options": ["Surface tension", "Capilarity", "Viscousity", "Friction"], "answer": "Capilarity"},
    {"question": "Which of these is not an European country?", "options": ["Albania", "Northern Ireland", "Switzerland", "Peru"], "answer": "Peru"},
    {"question": "A person who studies the weather is called?", "options": ["Astronaut", "Scientist", "Meteorologist", "Astronomer"], "answer": "Meteorologist"},
    {"question": "Pick the odd one out", "options": ["Consul", "Officer", "Archer", "Director"], "answer": "Archer"},
    {"question": "What is the deepest part of the ocean? ", "options": ["Underground", "Challenger deep", "Mariana trench", "Titan"], "answer": "Mariana trench"},
    {"question": "An example of an eye defect is all but one ", "options": ["Cataract", "Myopia", "Astigmatism", "Optic lobe"], "answer": "Optic lobe"},
    {"question": "The 16th President of the United States of America is?", "options": ["Nelson Mandela", "Abraham Lincoln", "Donald J. Trump", "Joe Biden"], "answer": "Abraham Lincoln"},
    {"question": "According to 'RICH PROF'. The unit of potential difference is? ", "options": ["Farad", "coulumb", "volts", "henry"], "answer": "volts"},
    {"question": "The Popular sci-fi movie MATRIX was first published in what year? ", "options": ["1998", "1999", "2000", "2001"], "answer": "1999"},
    {"question": " 'If God is for us, who can be against us'. This can be found in what book?", "options": ["Psalm", "Proverbs", "Acts of Apostles", "Romans"], "answer": "Romans"},
]

if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None

st.title(" Quiz Application")
st.caption("Developed by Gabriel")

if st.session_state.index >= len(quiz):
    st.balloons()
    
    st.audio("https://www.soundjay.com/human/sounds/applause-8.mp3", autoplay=True)
    st.success(f"🎉 Quiz complete! Your score 🎈🎉✨: {st.session_state.score}/{len(quiz)}")
    if st.button("Restart"):
        st.snow()
        st.image("https://media1.tenor.com/m/HY3hRtyv_CIAAAAC/congrats-proud-of-you.gif")  
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.user_answer = None
    st.stop()

q = quiz[st.session_state.index]
st.subheader(f"Question {st.session_state.index + 1}: {q['question']}")

if not st.session_state.answered:
    st.session_state.user_answer = st.radio(
        "Choose your answer:", q["options"], key=f"q_{st.session_state.index}"
    )

if not st.session_state.answered and st.button("Submit Answer"):
    if st.session_state.user_answer == q["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Incorrect! The correct answer is: {q['answer']}")
    st.session_state.answered = True

if st.session_state.answered:
    if st.button("Next"):
        st.session_state.index += 1
        st.session_state.answered = False
        st.session_state.user_answer = None
        st.rerun()

