import os
import re
from dotenv import load_dotenv
from openai import OpenAI
from place_data import place_database

# .env에서 OpenAI API 키 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 실제 존재하는 장소 목록과 설명 포함
available_places = list(place_database.keys())
place_list_str = "\n".join([
    f"- {name}: {place.get('desc', '설명 없음')}" for name, place in place_database.items()
])

def fetch_place_description(place_name):
    prompt = f"연세대학교 '{place_name}'에 대해 방문한 학생에게 설명하는 듯한 톤으로 2~3문장으로 소개해줘."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{ "role": "user", "content": prompt }]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❗ GPT 응답 오류: {e}"

def recommend_place_with_gpt(user_input):
    prompt = (
        f"학생이 이렇게 물어봤어: \"{user_input}\"\n\n"
        f"이 학생에게 연세대학교 캠퍼스 내에서 추천해줄 수 있는 장소는 아래 중에 있어:\n"
        f"{place_list_str}\n\n"
        f"위 장소 목록에서만 골라서, 2~3곳을 학생에게 추천해줘. "
        f"주어진 리스트에 포함된 장소에 대한 설명에서 근거를 찾아줘."
        f"각 추천은 '1. 장소명 - 이유' 형식으로 써줘. 목록에 없는 장소는 절대 포함하지 마."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{ "role": "user", "content": prompt }],
            temperature=0
        )
        gpt_text = response.choices[0].message.content.strip()

        # GPT 응답에서 장소명 추출
        matches = re.findall(r"\d\.\s*([가-힣A-Za-z0-9]+)", gpt_text)
        matched_places = [place for place in matches if place in place_database]

        return gpt_text, matched_places
    except Exception as e:
        return f"❗ GPT 오류: {e}", []