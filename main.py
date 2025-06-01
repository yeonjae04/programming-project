#사용자 선택 처리 함수
def get_choices(choice:str, use_name:str):
    if choice == '1':
        print("\n오늘의 일기를 작성해주세요.")
        diary = input("오늘의 일기를 입력: ")
    
    elif choice == '2':
        date = input("언제 일기를 확인하시겠습니까?(2025-00-00)")
        #print(llm에게 전달해서 그날 일기 요약하게 하기)
    
    elif choice == '3':
        print("\n과거 일기를 분석합니다.")
        #여기서 과거 저장 데이터 바탕으로 분석된 그래프 꺼내기
    
    else:
        print("잘못된 입력입니다. 1~3번 중 하나를 선택하여 주세요.")


