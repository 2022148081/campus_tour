import streamlit as st

def initialize_session_state():
    """Streamlit 세션 상태를 초기화합니다."""
    default_values = {
        "language": None,
        "tour_mode": None,
        "selected_department": None,
        "selected_event": None,
        "tour_script": [],
        "confirmed": False,
        "step_index": 0,
        "show_final_map": False,
        "gpt_descriptions": {},
        "custom_request": "",
        "custom_result": "",
        "custom_places": []
    }

    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value