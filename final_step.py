import streamlit as st
from text_constants import TEXT, is_korean
from chatbot_gpt import recommend_place_with_gpt
from map_utils import render_final_map, render_custom_place_map

def run_final_step():
    lang = "한국어" if is_korean() else "English"

    st.subheader(TEXT["final_step_title"][lang])

    # 🧭 학식 & 굿즈샵 버튼
    if st.button(TEXT["last_step"][lang]):
        st.session_state.show_final_map = True
        st.rerun()

    # 학식 & 굿즈샵 지도 렌더링
    if st.session_state.show_final_map:
        st.markdown("🍽️ **학생회관**, 🎁 **백양누리 지하 굿즈샵**을 둘러볼 수 있어요!")
        render_final_map()

    # 자유 질문
    st.markdown("---")
    st.subheader(TEXT["more_places"][lang])
    user_input = st.text_input(TEXT["custom_prompt"][lang], key="custom_input")

    if st.button(TEXT["custom_button"][lang]):
        if user_input.strip():
            gpt_result, matched_places = recommend_place_with_gpt(user_input)
            st.session_state.custom_result = gpt_result
            st.session_state.custom_places = matched_places
            st.rerun()

    if st.session_state.get("custom_result"):
        st.markdown(TEXT["gpt_result"][lang])
        st.write(st.session_state.custom_result)

        if st.session_state.custom_places:
            render_custom_place_map(st.session_state.custom_places)
        else:
            st.warning(TEXT["no_match"][lang])