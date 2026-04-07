import streamlit as st
import joblib

#모델 로딩
clf = joblib.load("freq.pkl")

def detect_lang(text):
    #알파벳 출현빈도 구하기
    text = text.lower()
    
    cnt = []
    for i in range(26):
        ch = chr(i + ord('a'))
        cnt.append(text.count(ch))

    total = sum(cnt)  #스케일링 하기  
    if total == 0: return "입력이 없습니다" 

    #입력 데이터 준비
    freq = list(map(lambda n: n / total, cnt))

    #예측 predict
    pred = clf.predict([freq])

    #리턴할 문자열
    lang_dic = {
        "en": "영어",
        "fr": "프랑스어",
        "id": "인도네시아어",
        "tl": "타갈로그어"
    }

    return lang_dic[pred[0]]


st.title('외국어 문장 판별')

text = st.text_area('외국어 입력(입력후 CTRL + ENTER)', height=400)

if text:
    st.badge(detect_lang(text))