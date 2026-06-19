import streamlit as st

st.set_page_config(
    page_title="🌈 MBTI 진로 탐험",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
}

.title-box{
    background: linear-gradient(90deg,#667eea,#764ba2);
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0 8px 20px rgba(0,0,0,0.2);
}

.result-box{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
}

.job-card{
    background:linear-gradient(135deg,#84fab0,#8fd3f4);
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
    color:#222;
    font-size:20px;
    font-weight:bold;
}

.info-card{
    background:#fff8dc;
    padding:15px;
    border-radius:15px;
    border-left:8px solid orange;
}

.stButton>button{
    background:linear-gradient(90deg,#ff9966,#ff5e62);
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 데이터
# -----------------------------
mbti_jobs = {
    "INTJ": {
        "desc":"🧠 전략적 사고와 문제 해결 능력이 뛰어난 유형",
        "jobs":["👨‍💻 AI 개발자","🔬 연구원","📈 데이터 분석가","🏗️ 건축가","⚙️ 엔지니어"]
    },
    "INTP": {
        "desc":"💡 창의적이고 논리적인 탐구형",
        "jobs":["💻 프로그래머","🔭 과학자","📚 교수","🧩 시스템 설계자","🤖 로봇공학자"]
    },
    "ENTJ": {
        "desc":"👑 리더십과 추진력이 강한 유형",
        "jobs":["🏢 CEO","📊 경영 컨설턴트","💰 투자 전문가","⚖️ 변호사","📣 마케팅 총괄"]
    },
    "ENTP": {
        "desc":"🚀 혁신과 아이디어가 넘치는 유형",
        "jobs":["🎤 기업가","📱 스타트업 창업가","🎬 콘텐츠 기획자","📢 광고기획자","💼 사업개발 전문가"]
    },
    "INFJ": {
        "desc":"🌱 통찰력과 공감 능력이 뛰어난 유형",
        "jobs":["🧑‍🏫 교사","🩺 상담사","✍️ 작가","🌍 사회운동가","🎨 디자이너"]
    },
    "INFP": {
        "desc":"🎨 이상주의적이고 창의적인 유형",
        "jobs":["✍️ 소설가","🎼 작곡가","🎨 일러스트레이터","🧑‍⚕️ 심리상담사","🎥 영화감독"]
    },
    "ENFJ": {
        "desc":"🤝 사람들을 이끄는 따뜻한 리더",
        "jobs":["👨‍🏫 교사","🎤 강사","👩‍💼 인사담당자","🤗 상담사","🌟 코치"]
    },
    "ENFP": {
        "desc":"🎉 열정적이고 창의적인 유형",
        "jobs":["🎬 PD","🎤 방송인","📢 마케터","📝 작가","🌈 크리에이터"]
    },
    "ISTJ": {
        "desc":"📋 책임감 있고 체계적인 유형",
        "jobs":["🏦 회계사","⚖️ 공무원","👮 경찰관","📊 감사관","📁 행정가"]
    },
    "ISFJ": {
        "desc":"💖 성실하고 배려심이 많은 유형",
        "jobs":["🩺 간호사","👩‍🏫 교사","🏥 의료행정가","🤝 사회복지사","📚 사서"]
    },
    "ESTJ": {
        "desc":"🏆 조직 관리 능력이 뛰어난 유형",
        "jobs":["🏢 관리자","💼 경영자","📈 프로젝트 매니저","⚖️ 판사","🏛️ 행정가"]
    },
    "ESFJ": {
        "desc":"😊 친절하고 협력적인 유형",
        "jobs":["🩺 간호사","👩‍🏫 교사","🎉 행사기획자","🤝 사회복지사","🏨 호텔리어"]
    },
    "ISTP": {
        "desc":"🔧 실용적이고 문제 해결 능력이 뛰어난 유형",
        "jobs":["✈️ 파일럿","🔧 정비사","👨‍💻 개발자","🚗 자동차 엔지니어","🛰️ 기술전문가"]
    },
    "ISFP": {
        "desc":"🎨 감각적이고 예술적인 유형",
        "jobs":["🎨 디자이너","📸 사진작가","🎵 음악가","💄 메이크업 아티스트","🌸 플로리스트"]
    },
    "ESTP": {
        "desc":"⚡ 활동적이고 도전적인 유형",
        "jobs":["💼 영업 전문가","🏅 스포츠 선수","📺 방송인","🚓 경찰관","🎤 이벤트 진행자"]
    },
    "ESFP": {
        "desc":"🌟 사교적이고 에너지가 넘치는 유형",
        "jobs":["🎬 배우","🎤 가수","📺 MC","🎉 이벤트 플래너","✈️ 승무원"]
    }
}

# -----------------------------
# 헤더
# -----------------------------
st.markdown("""
<div class="title-box">
<h1>🌈 MBTI 진로 탐험관 🚀</h1>
<h3>✨ 나의 MBTI로 미래 직업 찾기 ✨</h3>
</div>
""", unsafe_allow_html=True)

st.write("")
st.balloons()

# -----------------------------
# 선택
# -----------------------------
mbti = st.selectbox(
    "🎯 MBTI를 선택하세요",
    list(mbti_jobs.keys())
)

st.write("")

if st.button("🔮 추천 직업 보기"):
    
    info = mbti_jobs[mbti]

    st.markdown("""
    <div class="result-box">
    """, unsafe_allow_html=True)

    st.success(f"🎉 당신의 MBTI는 {mbti} 입니다!")

    st.markdown(f"""
    <div class="info-card">
    <h3>{info['desc']}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🌟 추천 직업 TOP 5")

    for job in info["jobs"]:
        st.markdown(
            f"<div class='job-card'>{job}</div>",
            unsafe_allow_html=True
        )

    st.write("")

    st.info(
        "📚 진로 선택은 MBTI만으로 결정되지 않습니다. "
        "관심 분야, 적성, 가치관, 경험을 함께 고려해 보세요!"
    )

    st.progress(100)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 하단
# -----------------------------
st.write("")
st.markdown("---")
st.markdown(
    "<h3 style='text-align:center;'>🚀 꿈을 향해 한 걸음! 🌈✨</h3>",
    unsafe_allow_html=True
)
