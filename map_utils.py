import streamlit as st
import folium
from streamlit_folium import st_folium
from place_data import place_database


def print_step_message(step):
    msg = step.get("msg")
    if isinstance(msg, str):
        st.markdown(f"📍 {msg}")
    elif isinstance(msg, list):
        for line in msg:
            st.markdown(f"📍 {line}")


def safe_place_description(place):
    desc = place.get("desc", "정보 없음")
    return str(desc) if not callable(desc) else "설명 없음"


def error_message(context, err):
    st.error(f"❗ {context} 중 오류 발생: {err}")


def get_map_center(tour_script):
    for step in tour_script:
        place_name = step.get("place")
        if isinstance(place_name, str) and place_name in place_database:
            place = place_database[place_name]
            return [place["lat"], place["lon"]]
        elif isinstance(place_name, list):
            for p in place_name:
                if p in place_database:
                    return [place_database[p]["lat"], place_database[p]["lon"]]
    return [37.56039, 126.936751]  # 기본값: 정문


def render_map_and_messages(tour_script):
    center = get_map_center(tour_script)
    m = folium.Map(location=center, zoom_start=16)

    for step in tour_script:
        print_step_message(step)
        place_name = step.get("place")

        if isinstance(place_name, list):
            for name in place_name:
                add_marker(m, name)
        elif isinstance(place_name, str):
            add_marker(m, place_name)

    try:
        st_folium(m, width=700, height=500)
    except Exception as e:
        error_message("지도 렌더링", e)


def add_marker(map_obj, place_name):
    if place_name not in place_database:
        return
    place = place_database[place_name]
    desc = safe_place_description(place)
    try:
        folium.Marker(
            location=[place["lat"], place["lon"]],
            tooltip=place_name,
            popup=folium.Popup(desc, max_width=300)
        ).add_to(map_obj)
    except Exception as e:
        error_message(f"마커 추가 실패: {place_name}", e)


def render_step_place_map(place):
    if not place:
        return
    if isinstance(place, str):
        place = [place]

    m = folium.Map(location=[37.56039, 126.936751], zoom_start=16)

    for name in place:
        add_marker(m, name)

    try:
        st_folium(m, width=700, height=500)
    except Exception as e:
        error_message("단계별 지도 렌더링", e)


def render_final_map():
    m = folium.Map(location=[37.561, 126.937], zoom_start=16)
    for name in ["학생회관", "백양누리"]:
        add_marker(m, name)
    try:
        st_folium(m, width=700, height=500)
    except Exception as e:
        error_message("최종 장소 지도 렌더링", e)


def render_custom_place_map(places):
    if not places:
        return
    m = folium.Map(location=[37.561, 126.937], zoom_start=16)
    for name in places:
        add_marker(m, name)
    try:
        st_folium(m, width=700, height=500)
    except Exception as e:
        error_message("자유 탐색 지도 렌더링", e)