import streamlit as st
from datetime import date
import random

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="2026 FIFA World Cup",
    page_icon="⚽",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp{
    background:linear-gradient(
        180deg,
        #0f5f2d 0%,
        #107a39 50%,
        #0f5f2d 100%
    );
}

.main-title{
    text-align:center;
    color:white;
    font-size:3rem;
    font-weight:900;
}

.sub-title{
    text-align:center;
    color:#e8ffe8;
    font-size:1.1rem;
}

.card{
    background:white;
    border-radius:18px;
    padding:20px;
    box-shadow:0 4px 15px rgba(0,0,0,0.15);
}

.match-card{
    background:#ffffff;
    border-left:8px solid #00a651;
    border-radius:16px;
    padding:15px;
    margin-bottom:10px;
}

.team{
    font-size:22px;
    font-weight:bold;
}

.bracket{
    background:#f8f8f8;
    padding:15px;
    border-radius:12px;
    margin-bottom:10px;
}

.stButton>button{
    background:#00a651;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 헤더
# --------------------------------------------------
st.markdown(
    """
    <div class='main-title'>⚽ 2026 FIFA World Cup ⚽</div>
    <div class='sub-title'>
    🇺🇸 United States · 🇨🇦 Canada · 🇲🇽 Mexico
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------
# 샘플 경기 데이터
# 실제 운영 시 API 연동 권장
# --------------------------------------------------
matches = {
    "2026-06-19": [
        ("🇺🇸 미국", "🇦🇺 호주"),
        ("🇧🇷 브라질", "🇭🇹 아이티"),
        ("🏴 스코틀랜드", "🇲🇦 모로코"),
    ],

    "2026-06-20": [
        ("🇩🇪 독일", "🇨🇮 코트디부아르"),
        ("🇳🇱 네덜란드", "🇸🇪 스웨덴"),
    ],

    "2026-06-21": [
        ("🇪🇸 스페인", "🇸🇦 사우디아라비아"),
        ("🇧🇪 벨기에", "🇮🇷 이란"),
    ],
}

# --------------------------------------------------
# 날짜 선택
# --------------------------------------------------
st.header("📅 경기 일정 조회")

selected_date = st.date_input(
    "날짜 선택",
    value=date(2026, 6, 19)
)

selected_str = selected_date.strftime("%Y-%m-%d")

if selected_str in matches:

    st.success(f"⚽ {selected_str} 경기 일정")

    for home, away in matches[selected_str]:

        st.markdown(
            f"""
            <div class='match-card'>
                <div class='team'>{home}</div>
                <h2 style='text-align:center;'>VS</h2>
                <div class='team'>{away}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.info("해당 날짜의 경기 정보가 없습니다.")

# --------------------------------------------------
# 승리 확률 분석
# --------------------------------------------------
st.header("📊 AI 승리 확률 분석")

teams = [
    "🇧🇷 브라질",
    "🇦🇷 아르헨티나",
    "🇪🇸 스페인",
    "🇫🇷 프랑스",
    "🏴 잉글랜드",
    "🇩🇪 독일",
    "🇰🇷 대한민국",
    "🇵🇹 포르투갈"
]

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "홈팀",
        teams,
        index=0
    )

with col2:
    team2 = st.selectbox(
        "원정팀",
        teams,
        index=1
    )

if st.button("🔍 승률 분석"):

    seed = abs(hash(team1 + team2))

    random.seed(seed)

    win1 = random.randint(35, 70)
    win2 = 100 - win1

    st.subheader("예상 결과")

    st.write(f"🏆 {team1}: **{win1}%**")
    st.progress(win1)

    st.write(f"🏆 {team2}: **{win2}%**")
    st.progress(win2)

    if win1 > win2:
        st.success(f"예상 우세 팀 👉 {team1}")
    else:
        st.success(f"예상 우세 팀 👉 {team2}")

    st.caption(
        "※ 실제 AI 모델이 아닌 예시 시뮬레이션입니다."
    )

# --------------------------------------------------
# 대진표
# --------------------------------------------------
st.header("🏆 토너먼트 대진표")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class='bracket'>
    <h4>16강</h4>
    🇧🇷 브라질<br>
    🇺🇸 미국
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='bracket'>
    <h4>16강</h4>
    🇫🇷 프랑스<br>
    🇰🇷 대한민국
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='bracket'>
    <h4>8강</h4>
    🇧🇷 브라질
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='bracket'>
    <h4>8강</h4>
    🇫🇷 프랑스
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class='bracket'>
    <h4>🏆 결승</h4>
    🇧🇷 브라질<br>
    VS<br>
    🇫🇷 프랑스
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# 우승 후보
# --------------------------------------------------
st.header("⭐ 우승 후보 파워 랭킹")

ranking = [
    ("🇧🇷 브라질", 95),
    ("🇫🇷 프랑스", 93),
    ("🇦🇷 아르헨티나", 92),
    ("🏴 잉글랜드", 90),
    ("🇪🇸 스페인", 88),
    ("🇩🇪 독일", 87),
    ("🇵🇹 포르투갈", 86),
    ("🇰🇷 대한민국", 78)
]

for team, score in ranking:
    st.write(f"{team} ({score})")
    st.progress(score)

st.divider()

st.markdown(
    """
    <center>
    <h3 style='color:white'>
    ⚽ THE WORLD'S GAME ⚽
    </h3>
    </center>
    """,
    unsafe_allow_html=True
)
