import streamlit as st
from script import TOUR_SCRIPTS
from text_constants import TEXT, is_korean

def run_department_tour():
    lang = "한국어" if is_korean() else "English"

    # 1. 계열 선택
    st.subheader(TEXT["select_dept"][lang])
    departments = list(TOUR_SCRIPTS.keys())
    selected = st.selectbox(" ", departments, key="dept_selectbox")

    if selected:
        st.session_state.selected_department = selected
        st.session_state.tour_script = TOUR_SCRIPTS[selected]
    
    # 2. 코스 미리보기
    if selected and st.button(TEXT["preview_course"][lang]):
        st.subheader(TEXT["course_preview"][lang])
        places = []
        for step in st.session_state.tour_script:
            place = step.get("place")
            if isinstance(place, list):
                places.extend(place)
            elif isinstance(place, str):
                places.append(place)

        unique_places = list(dict.fromkeys(places))  # 중복 제거
        for p in unique_places:
            st.markdown(f"- 📍 {p}")
        
        st.session_state.confirmed = False  # 다시 미리보기 누를 경우 초기화

    # 3. 코스 확정 버튼
    if st.session_state.tour_script and not st.session_state.confirmed:
        if st.button(TEXT["confirm_course"][lang]):
            st.session_state.confirmed = True
            st.session_state.step_index = 0
            st.rerun()