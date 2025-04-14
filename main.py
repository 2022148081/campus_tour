import streamlit as st

# 모듈 불러오기
from state_initializer import initialize_session_state
from text_constants import TEXT, is_korean
from department_tour import run_department_tour
from event_tour import run_event_tour
from tour_engine import run_tour_steps
from final_step import run_final_step

# 세션 상태 초기화
initialize_session_state()

# 언어 설정
st.set_page_config(page_title="Yonsei Campus Tour", layout="wide")

if st.session_state.language is None:
    st.markdown("### 언어를 선택하세요 | Choose your language")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🇰🇷 한국어"):
            st.session_state.language = "한국어"
            st.rerun()
    with col2:
        if st.button("🇺🇸 English"):
            st.session_state.language = "English"
            st.rerun()
    st.stop()

# 선택된 언어에 따른 텍스트 세트 선택
lang = "한국어" if is_korean() else "English"

# 앱 제목
st.title(TEXT["title"][lang])
st.markdown("")

# 투어 모드 선택 (계열 기반 or 행사 기반)
if st.session_state.tour_mode is None:
    st.subheader(TEXT["mode_title"][lang])
    col1, col2 = st.columns(2)
    with col1:
        if st.button(TEXT["department_mode"][lang]):
            st.session_state.tour_mode = "department"
            st.rerun()
    with col2:
        if st.button(TEXT["event_mode"][lang]):
            st.session_state.tour_mode = "event"
            st.rerun()
    st.stop()

# 계열 기반 투어 진행
if st.session_state.tour_mode == "department":
    run_department_tour()

# 행사 기반 투어 진행
elif st.session_state.tour_mode == "event":
    run_event_tour()

# 본격적인 투어 진행
if st.session_state.tour_script and st.session_state.confirmed and not st.session_state.show_final_map:
    run_tour_steps()

# 마지막 장소 후 학식/굿즈 & 자유 탐색
if st.session_state.tour_script and st.session_state.confirmed and st.session_state.show_final_map:
    run_final_step()