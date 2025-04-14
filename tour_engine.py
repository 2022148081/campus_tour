import streamlit as st
from text_constants import TEXT, is_korean
from chatbot_gpt import fetch_place_description
from map_utils import render_step_place_map

def run_tour_steps():
    tour_script = st.session_state.tour_script
    step_idx = st.session_state.step_index
    lang = "한국어" if is_korean() else "English"

    # 종료 조건
    if step_idx >= len(tour_script):
        st.success(TEXT["tour_done"][lang])
        st.session_state.show_final_map = True  # ✅ 마지막에 이걸 꼭 True로 설정해야 run_final_step 실행됨
        return

    step = tour_script[step_idx]
    place = step.get("place")
    msg = step.get("msg")

    # 기본 설명 출력
    st.markdown(f"### 🗺️ {TEXT['step_msg'][lang]}")
    if isinstance(msg, list):
        for m in msg:
            st.markdown(f"📍 {m}")
    elif isinstance(msg, str):
        st.markdown(f"📍 {msg}")

    # GPT 설명 출력
    if place:
        if place not in st.session_state.gpt_descriptions:
            gpt_text = fetch_place_description(place)
            st.session_state.gpt_descriptions[place] = gpt_text
        st.info(st.session_state.gpt_descriptions[place])

    # 지도 표시
    if place:
        render_step_place_map(place)

    # 다음 단계 버튼
    if st.button(TEXT["next_step"][lang]):
        st.session_state.step_index += 1
        st.rerun()