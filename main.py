import streamlit as st
import random

# ----------------------------------
# 페이지 설정
# ----------------------------------
st.set_page_config(
    page_title="기분 따라 듣는 클래식 🎵",
    page_icon="🎻",
    layout="wide"
)

# ----------------------------------
# CSS
# ----------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
    180deg,
    #f7fff5 0%,
    #effced 50%,
    #f7fff5 100%);
}

.main-title{
    text-align:center;
    font-size:3.2rem;
    font-weight:800;
    color:#2f6f3e;
}

.subtitle{
    text-align:center;
    color:#5d8067;
    font-size:1.1rem;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 5px 20px rgba(0,0,0,0.08);
}

.song-card{
    background:#ffffff;
    border-left:8px solid #84d38f;
    padding:18px;
    border-radius:14px;
    margin-bottom:12px;
}

.quote-box{
    background:#dff5e4;
    border-radius:15px;
    padding:18px;
    color:#336644;
}

.stButton>button{
    background:#7fcf8c;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# 데이터
# ----------------------------------
music_data = {

    "😊 행복해요": [
        {
            "title":"모차르트 - 아이네 클라이네 나흐트무지크",
            "composer":"모차르트",
            "desc":"밝고 경쾌한 분위기의 대표적인 클래식",
            "youtube":"https://www.youtube.com/results?search_query=Eine+Kleine+Nachtmusik"
        },
        {
            "title":"비발디 - 사계 중 봄",
            "composer":"비발디",
            "desc":"싱그러운 봄의 에너지가 느껴지는 작품",
            "youtube":"https://www.youtube.com/results?search_query=Vivaldi+Spring"
        }
    ],

    "😌 마음이 편안해지고 싶어요": [
        {
            "title":"드뷔시 - 달빛",
            "composer":"드뷔시",
            "desc":"잔잔하고 따뜻한 밤하늘 같은 음악",
            "youtube":"https://www.youtube.com/results?search_query=Debussy+Clair+de+Lune"
        },
        {
            "title":"사티 - 짐노페디 1번",
            "composer":"에릭 사티",
            "desc":"명상과 휴식에 잘 어울리는 곡",
            "youtube":"https://www.youtube.com/results?search_query=Satie+Gymnopedie+No+1"
        }
    ],

    "😢 위로받고 싶어요": [
        {
            "title":"바흐 - G선상의 아리아",
            "composer":"바흐",
            "desc":"부드럽고 따뜻한 위로를 주는 명곡",
            "youtube":"https://www.youtube.com/results?search_query=Bach+Air+on+the+G+String"
        },
        {
            "title":"쇼팽 - 녹턴 Op.9 No.2",
            "composer":"쇼팽",
            "desc":"감성을 어루만져 주는 아름다운 선율",
            "youtube":"https://www.youtube.com/results?search_query=Chopin+Nocturne+Op+9+No+2"
        }
    ],

    "😴 집중하거나 공부하고 싶어요": [
        {
            "title":"바흐 - 평균율 클라비어",
            "composer":"바흐",
            "desc":"집중력을 높여주는 클래식",
            "youtube":"https://www.youtube.com/results?search_query=Bach+Well+Tempered+Clavier"
        },
        {
            "title":"모차르트 - 피아노 협주곡 21번",
            "composer":"모차르트",
            "desc":"편안하면서도 집중에 도움을 주는 곡",
            "youtube":"https://www.youtube.com/results?search_query=Mozart+Piano+Concerto+21"
        }
    ],

    "😤 스트레스를 날리고 싶어요": [
        {
            "title":"베토벤 - 운명 교향곡",
            "composer":"베토벤",
            "desc":"강렬한 에너지가 느껴지는 작품",
            "youtube":"https://www.youtube.com/results?search_query=Beethoven+Symphony+5"
        },
        {
            "title":"홀스트 - 행성 중 목성",
            "composer":"홀스트",
            "desc":"웅장하고 힘찬 분위기",
            "youtube":"https://www.youtube.com/results?search_query=Holst+Jupiter"
        }
    ],

    "😍 감동을 느끼고 싶어요": [
        {
            "title":"차이콥스키 - 백조의 호수",
            "composer":"차이콥스키",
            "desc":"우아하고 감동적인 선율",
            "youtube":"https://www.youtube.com/results?search_query=Swan+Lake+Tchaikovsky"
        },
        {
            "title":"라흐마니노프 - 피아노 협주곡 2번",
            "composer":"라흐마니노프",
            "desc":"깊은 감성과 감동을 선사하는 명곡",
            "youtube":"https://www.youtube.com/results?search_query=Rachmaninoff+Piano+Concerto+2"
        }
    ]
}

# ----------------------------------
# 헤더
# ----------------------------------
st.markdown(
"""
<div class='main-title'>
🎻 기분 따라 듣는 클래식 🎵
</div>

<div class='subtitle'>
오늘의 감정에 어울리는 클래식 음악을 만나보세요 🌿
</div>
""",
unsafe_allow_html=True
)

# ----------------------------------
# 감성 문구
# ----------------------------------
quotes = [
    "🌱 음악은 마음이 쉬어가는 작은 숲입니다.",
    "☁️ 좋은 음악은 조용히 하루를 위로합니다.",
    "🎹 클래식은 시간을 넘어 마음을 연결합니다.",
    "🌿 오늘의 감정도 소중한 음악이 됩니다.",
]

st.markdown(
f"""
<div class='quote-box'>
{random.choice(quotes)}
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ----------------------------------
# 기분 선택
# ----------------------------------
mood = st.selectbox(
    "💚 지금 어떤 기분인가요?",
    list(music_data.keys())
)

st.write("")

st.subheader("🎼 추천 클래식 목록")

for music in music_data[mood]:

    with st.container():

        st.markdown(
            f"""
            <div class='song-card'>
            <h4>🎵 {music['title']}</h4>
            <b>🎹 작곡가:</b> {music['composer']}<br>
            <b>🌿 설명:</b> {music['desc']}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "▶️ 유튜브에서 듣기",
            music["youtube"]
        )

        st.write("")

# ----------------------------------
# 오늘의 추천
# ----------------------------------
st.markdown("---")

st.subheader("✨ 오늘의 랜덤 클래식")

all_music = []

for mood_list in music_data.values():
    all_music.extend(mood_list)

today_music = random.choice(all_music)

st.success(
    f"🎻 {today_music['title']} | {today_music['composer']}"
)

st.link_button(
    "🎵 지금 감상하기",
    today_music["youtube"]
)

# ----------------------------------
# 푸터
# ----------------------------------
st.markdown("---")

st.markdown(
"""
<center>

<h3 style='color:#4d7c59'>
🌿 마음이 쉬어가는 클래식 정원 🎻
</h3>

오늘도 좋은 음악과 함께하세요 ☘️

</center>
""",
unsafe_allow_html=True
)
