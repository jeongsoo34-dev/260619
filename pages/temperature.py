import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 기본 레이아웃 설정
st.set_page_config(
    page_title="서울 기온 120년 역사 대시보드",
    page_icon="🌡️",
    layout="wide"
)

# 2. 데이터 로드 및 전처리 (캐싱 적용으로 데이터 로딩 속도 최적화)
@st.cache_data
def load_data():
    file_path = "ta_20260619190504.csv"
    
    # UTF-8 인코딩으로 CSV 읽기
    df = pd.read_csv(file_path, encoding='utf-8')
    
    # 컬럼명 양끝 공백 제거 (안전한 컬럼 매칭용)
    df.columns = df.columns.str.strip()
    
    # '날짜' 컬럼 내에 포함된 \t 이나 따옴표 등 특수문자 제거 후 날짜형 변환
    df['날짜'] = df['날짜'].astype(str).str.replace(r'[^\d-]', '', regex=True)
    df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')
    
    # 기온 데이터 중 누락된 값(결측치)이 있는 행은 제거
    df = df.dropna(subset=['평균기온(℃)', '최저기온(℃)', '최고기온(℃)'])
    
    # 분석에 필요한 연도 및 월 컬럼 추가
    df['연도'] = df['날짜'].dt.year
    df['월'] = df['날짜'].dt.month
    
    return df

try:
    # 데이터 불러오기
    df = load_data()
    
    # 대시보드 대문 타이틀
    st.title("🌡️ 서울 기온 타임머신 (1907 ~ 2026)")
    st.markdown("---")
    st.markdown(
        "1907년부터 2026년까지 **약 120년간 축적된 서울의 기온 변화**를 탐색하는 웹 대시보드입니다. "
        "우리가 살고 있는 서울이 과거에 비해 얼마나 따뜻해졌는지 데이터를 통해 확인해보세요."
    )
    
    # 상단 탭 구성
    tab1, tab2, tab3 = st.tabs(["📈 장기 기온 추이", "🏆 역대 기온 기록실", "📅 연도별 월간 분석"])
    
    # ----------------------------------------------------
    # TAB 1: 장기 기온 추이 (지구온난화 흐름 시각화)
    # ----------------------------------------------------
    with tab1:
        st.header("연도별 평균 기온 변화 트렌드")
        st.write("시간이 흐름에 따라 서울의 연평균 기온이 어떻게 변해왔는지 추세를 분석합니다.")
        
        # 연도별 평균값 계산
        yearly_df = df.groupby('연도')[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']].mean().reset_index()
        
        # Plotly를 이용한 반응형 선 그래프 구현
        fig = px.line(yearly_df, x='연도', y='평균기온(℃)', title='서울 연도별 평균 기온 장기 추이')
        fig.add_scatter(x=yearly_df['연도'], y=yearly_df['최고기온(℃)'], mode='lines', name='연평균 최고기온', line=dict(color='#ff4b4b'))
        fig.add_scatter(x=yearly_df['연도'], y=yearly_df['최저기온(℃)'], mode='lines', name='연평균 최저기온', line=dict(color='#0066cc'))
        
        fig.update_layout(
            xaxis_title="연도",
            yaxis_title="기온 (℃)",
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0)
        )
        st.plotly_chart(fig, use_container_width=True)
        st.info("💡 과거 1900년대 초반에 비해 최근으로 올수록 평균 기온 곡선이 확연하게 우상향하는 모습을 관찰할 수 있습니다.")

    # ----------------------------------------------------
    # TAB 2: 역대 기온 기록실 (최고/최저 기온 기네스북)
    # ----------------------------------------------------
    with tab2:
        st.header("🔥 서울 기후 기네스북: 역대 극값 TOP 10")
        st.write("기상 관측 이래 서울에서 가장 더웠던 날과 가장 추웠던 날의 순간을 기록 데이터로 만나보세요.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🥵 역대 최고 기온 TOP 10")
            hot_top10 = df.sort_values(by='최고기온(℃)', ascending=False).head(10).copy()
            hot_top10['날짜'] = hot_top10['날짜'].dt.strftime('%Y-%m-%d')
            st.dataframe(hot_top10[['날짜', '최고기온(℃)', '평균기온(℃)']].reset_index(drop=True), use_container_width=True)
            
        with col2:
            st.subheader("🥶 역대 최저 기온 TOP 10")
            cold_top10 = df.sort_values(by='최저기온(℃)', ascending=True).head(10).copy()
            cold_top10['날짜'] = cold_top10['날짜'].dt.strftime('%Y-%m-%d')
            st.dataframe(cold_top10[['날짜', '최저기온(℃)', '평균기온(℃)']].reset_index(drop=True), use_container_width=True)

    # ----------------------------------------------------
    # TAB 3: 연도별 월간 분석 (특정 연도 돋보기 조회)
    # ----------------------------------------------------
    with tab3:
        st.header("🔍 특정 연도 선택 및 월별 분석")
        st.write("궁금한 연도를 선택하여 해당 해의 1월부터 12월까지 월평균 기온 분포를 확인할 수 있습니다.")
        
        # 데이터 내 존재하는 연도를 역순으로 정렬하여 드롭다운 리스트 생성
        available_years = sorted(df['연도'].unique(), reverse=True)
        selected_year = st.selectbox("조회할 연도를 선택하세요:", available_years)
        
        # 선택한 연도의 데이터 필터링 후 월별 평균 계산
        year_df = df[df['연도'] == selected_year]
        monthly_df = year_df.groupby('월')[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']].mean().reset_index()
        
        # 월별 기온 분포를 입체적인 색상의 막대그래프로 시각화
        fig_month = px.bar(
            monthly_df, 
            x='월', 
            y='평균기온(℃)', 
            title=f"📅 {selected_year}년 월별 평균 기온 분포",
            text_auto='.1f',
            color='평균기온(℃)',
            color_continuous_scale='RdYlBu_r'
        )
        fig_month.update_layout(
            xaxis=dict(tickmode='linear', tick0=1, dtick=1),
            xaxis_title="월",
            yaxis_title="평균 기온 (℃)"
        )
        st.plotly_chart(fig_month, use_container_width=True)

except Exception as e:
    st.error(f"⚠️ 데이터를 로드하거나 대시보드를 생성하는 도중 오류가 발생했습니다.")
    st.error(f"오류 내용 상세: {e}")
    st.info("💡 깃허브 저장소 내에 'ta_20260619190504.csv' 파일이 이 파이썬 스크립트 파일과 동일한 위치에 존재하는지 확인해주세요.")
