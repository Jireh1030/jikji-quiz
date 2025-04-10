import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Jikji Quiz Game", page_icon="📜", layout="centered")

# 제목
st.title("📜 Are You a Jikji Master?")
st.markdown("Test your knowledge about **Jikji**, the world’s first book printed with metal movable type!")

# 퀴즈 데이터
questions = [
    {
        "question": "1. In which year was Jikji printed?",
        "options": ["1455", "1377", "1234", "1501"],
        "answer": "1377",
        "explanation": "Jikji was printed in 1377 at Heungdeok Temple in Korea, predating Gutenberg's Bible by 78 years."
    },
    {
        "question": "2. What does the title 'Jikji Simche Yojeol' mean?",
        "options": ["Wisdom of the East", "The Buddhist Code", "Anthology of Zen Teachings", "Ancient Korean History"],
        "answer": "Anthology of Zen Teachings",
        "explanation": "'Jikji Simche Yojeol' translates to 'Anthology of Zen Teachings on the Mind's Direct Enlightenment'."
    },
    {
        "question": "3. Which country currently holds the only surviving copy of Jikji?",
        "options": ["Korea", "Japan", "Germany", "France"],
        "answer": "France",
        "explanation": "The only surviving copy of Jikji is kept at the National Library of France (BnF)."
    },
    {
        "question": "4. What was revolutionary about Jikji's printing method?",
        "options": ["It was handwritten", "It used colored ink", "It was the first metal movable type print", "It was carved into stone"],
        "answer": "It was the first metal movable type print",
        "explanation": "Jikji was the first known book printed using metal movable type—changing how knowledge was preserved."
    },
    {
        "question": "5. How is Jikji’s legacy continued today?",
        "options": ["It’s sung in rituals", "Through digital storytelling and preservation", "Through sculptures", "It is no longer relevant"],
        "answer": "Through digital storytelling and preservation",
        "explanation": "Jikji’s spirit lives on through projects like InkBit, which reimagine its mission in the digital world."
    }
]

# 점수 변수
score = 0

# 질문 반복
for idx, q in enumerate(questions):
    st.subheader(q["question"])
    choice = st.radio("Select your answer:", q["options"], key=idx)
    if st.button(f"Check Answer {idx + 1}", key=f"btn_{idx}"):
        if choice == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Wrong. The correct answer is: {q['answer']}")
        st.info(f"💡 {q['explanation']}")

# 점수 확인
st.markdown("---")
if st.button("Show Final Score"):
    st.subheader(f"🎯 Your Score: {score} / {len(questions)}")
    if score == 5:
        st.success("🏆 You're a true Jikji Master!")
    elif score >= 3:
        st.info("👍 Good job! You know your Jikji.")
    else:
        st.warning("📘 Keep exploring! Jikji has much to teach.")
