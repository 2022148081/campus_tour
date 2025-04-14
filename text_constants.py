import streamlit as st

# 언어 상태 가져오기 (기본값: 한국어)
def get_language():
    return st.session_state.get("language", "한국어")

def is_korean():
    return get_language() == "한국어"

# 다국어 텍스트 딕셔너리
TEXT = {
    "title": {
        "한국어": "🎓 연세대학교 캠퍼스 투어 챗봇",
        "English": "🎓 Yonsei University Campus Tour Chatbot"
    },
    "mode_title": {
        "한국어": "어떤 방식으로 투어를 시작할까요?",
        "English": "How would you like to start your tour?"
    },
    "department_mode": {
        "한국어": "🎓 희망 계열로 투어할래요",
        "English": "🎓 Tour by Department"
    },
    "event_mode": {
        "한국어": "🎉 축제 장소 중심으로 볼래요",
        "English": "🎉 Explore Festival Locations"
    },
    "select_dept": {
        "한국어": "👀 관심 있는 계열을 선택하세요",
        "English": "👀 Select your department of interest"
    },
    "preview_course": {
        "한국어": "🚶 투어 코스 미리 보기",
        "English": "🚶 Preview Tour Course"
    },
    "course_preview": {
        "한국어": "🔍 방문할 장소 미리 보기",
        "English": "🔍 Places to be visited"
    },
    "confirm_course": {
        "한국어": "✅ 이대로 투어 진행할래요",
        "English": "✅ Start the Tour"
    },
    "next_step": {
        "한국어": "➡️ 다음 장소로 이동하기",
        "English": "➡️ Go to the Next Location"
    },
    "last_step": {
        "한국어": "🎁 학식이나 기념품샵 둘러보기",
        "English": "🎁 Explore Cafeteria or Gift Shop"
    },
    "final_step_title": {
        "한국어": "🍽️ 학식 & 🎁 연세 굿즈샵",
        "English": "🍽️ Cafeteria & 🎁 Yonsei Goods Shop"
    },
    "more_places": {
        "한국어": "🙋 더 보고 싶은 장소가 있나요?",
        "English": "🙋 Would you like to see more places?"
    },
    "custom_prompt": {
        "한국어": "원하는 장소나 키워드를 입력하세요:",
        "English": "Enter a place or keyword you'd like to explore:"
    },
    "custom_button": {
        "한국어": "🔎 GPT에게 추천받기",
        "English": "🔎 Ask GPT for Recommendations"
    },
    "gpt_result": {
        "한국어": "#### GPT 추천 결과",
        "English": "#### GPT Recommendations"
    },
    "no_match": {
        "한국어": "❗ 지도에 표시할 수 있는 장소가 없습니다.",
        "English": "❗ No valid places found to display on the map."
    },
    "tour_done": {
        "한국어": "✅ 투어가 완료되었습니다!",
        "English": "✅ The tour has been completed!"
    },
    "step_msg": {
        "한국어": "이동 경로 및 장소 설명이에요!",
        "English": "Here’s your route and the place description!"
    }
}