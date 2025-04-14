import streamlit as st
from script import event_places_dict
from text_constants import TEXT, is_korean

def run_event_tour():
    lang = "한국어" if is_korean() else "English"

    # 1. 축제 선택
    event_names = list(event_places_dict.keys())
    selected = st.selectbox("🎪 행사 이름을 선택하세요", event_names, key="event_selectbox")

    if selected:
        st.session_state.selected_event = selected
        st.session_state.tour_script = event_places_dict[selected]

    # 2. 코스 미리보기
    if selected and st.button(TEXT["preview_course"][lang]):
        st.subheader(TEXT["course_preview"][lang])
        places = [step["place"] for step in st.session_state.tour_script if "place" in step]
        unique_places = list(dict.fromkeys(places))
        for p in unique_places:
            st.markdown(f"- 📍 {p}")

        st.session_state.confirmed = False  # 다시 미리보기 누르면 초기화

    # 3. 코스 확정 버튼
    if st.session_state.tour_script and not st.session_state.confirmed:
        if st.button(TEXT["confirm_course"][lang]):
            st.session_state.confirmed = True
            st.session_state.step_index = 0
            st.rerun()