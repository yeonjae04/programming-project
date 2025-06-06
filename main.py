from pathlib import Path
import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import random
import requests

name = input("이름을 입력해주세요.:")

#사용자의 일기 데이터 저장 함수
DATA_SAVE = Path("diary_data")
DATA_SAVE.mkdir(exist_ok = True)

def save_diary_dta(date_str, name, diary, summary, advice, emotion):
    """
    하루치 일기 데이터를 JSON 파일로 저장합니다
    
    Parameters:
    -date_str (str): 날짜 (예: 2025-06-01)
    -name (str): 사용자 이름
    -diary (str): 원본 일기 텍스트
    -summary (str): 요약 텍스트
    -advice (str): 조언 텍스트
    -emotion(dict): 감정 분석 결과 
    """
    data = {
        "name": name,
        "data": date_str,
        "diary": diary,
        "summary": summary,
        "advice": advice,
        "emotion": emotion
    }

    file_path = DATA_SAVE / F"{date_str}_{name}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"{date_str} 일기가 저장되었습니다!->{file_path}")

#사용자 일기 요약 함수
def get_summary(diary):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer <OPENROUTER_API_KEY>",
            "Content-Type": "application/json"
  },
        data=json.dumps({
            "model": "meta-llama/llama-3.3-8b-instruct:free",
            "messages": [
            {
                "role": "user",
                "content": f"다음 일기를 분석하고 그를 토대로 요약해줘. \n{diary}"
            } 
    ],
    
  })
)
    if response.ok:
        result = response.json()
        output = result["choices"][0]["message"]["content"]
        return output
    else:
        print("요청실패")

#사용자 일기 조언 함수
def get_advice(diary):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer <OPENROUTER_API_KEY>",
            "Content-Type": "application/json"
  },
        data=json.dumps({
            "model": "meta-llama/llama-3.3-8b-instruct:free",
            "messages": [
            {
                "role": "user",
                "content": f"다음 일기를 요약하고 감정 분석과 조언을 해줘.\n{diary}"
            } 
    ],
    
  })
)
    if response.ok:
        result = response.json()
        output = result["choices"][0]["message"]["content"]
        return output
    else:
        print("요청실패")

#사용자 선택 처리 함수
def get_choices(choice:str):
    if choice == '1':
        print("\n오늘의 일기를 작성해주세요.")
        diary = input("오늘의 일기를 입력: ")

        summary = get_summary(diary)
        advice = get_advice(diary)
        print("\n 요약:",summary)
        print("\n 조언:",advice)
    
    elif choice == '2':
        date = input("언제 일기를 확인하시겠습니까?(2025-00-00)")
        #print(llm에게 전달해서 그날 일기 요약하게 하기)
    
    elif choice == '3':
        print("\n과거 일기를 분석합니다.")
        #여기서 과거 저장 데이터 바탕으로 분석된 그래프 꺼내기
    
    else:
        print("잘못된 입력입니다. 1~3번 중 하나를 선택하여 주세요.")

#사용자 질문 함수
def main():

    while True:
        print("\n무엇을 하시겠습니까?")
        print("\n1. 오늘 일기 작성")
        print("\n2. 과거 일기 확인")
        print("\n3. 과거 일기 분석 보기")
        choice = input("번호를 선택하세요: ").strip()
        get_choices(choice)

