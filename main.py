from pathlib import Path
import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import random
import requests

name = input("이름을 입력해주세요.: ")
print(f"{name}님 안녕하세요!")

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
                "content": f"다음 일기를 보고 조언을 해줘.\n{diary}"
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
def get_choices(choice:str, use_name:str):
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

def main():
    #이름 받고 인사하는 부분!
    while True:
        print("\n무엇을 하시겠습니까?")
        print("\n1. 오늘 일기 작성")
        print("\n2. 과거 일기 확인")
        print("\n 3. 과거 일기 분석 보기")
        choice = input("번호를 선택하세요: ").strip()
        get_choices(choice)