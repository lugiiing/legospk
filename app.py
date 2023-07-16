import os
import openai
import streamlit as st
from dotenv import load_dotenv


# from streamlit_chat import message

# 스트림릿이랑 파이썬, vs코드 같은 폴더에
# 이 파일도 같은 폴더에 넣어야하는지는 모르겠움,,

# import streamlit as st
# from io import StringIO

# 경로 /Users/gyuribyun/Documents/legoapp
# 경로 터미널에 입력 후(cd 경로 복붙)
# streamlit run app.py로 링크 받기


# 타이틀 적용, # 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(':santa:레고스파이크 할아버지')

# 캡션 적용
st.caption('레고스파이크 프라임을 이용한 코드를 구성할 때 어떤 블럭을 사용해야할 지 상황에 맞는 도움을 제공하는 친절한 레고할아버지 입니다. 선물:gift:같은 도움을 받아보세요!')


# 마크다운 부가설명
st.markdown('###### 코드가 필요한 상황, 작동 내용, 작동 조건, 입력장치, 출력장치를 각각 입력한다음 :red[코드블럭 추천받기] 버튼을 눌러주세요.:sparkles:')


# 텍스트 입력
situation = st.text_input(
    label='무슨 상황인가요?', 
    placeholder='예시: 자율주행'
)
st.write(f'선택한 상황: :violet[{situation}]')


# 텍스트 입력
condition = st.text_input(
    label='작동 조건이 있나요?', 
    placeholder='예시: 벽에 닿음'
)
st.write(f'선택한 상황: :violet[{condition}]')


# 텍스트 입력
reaction = st.text_input(
    label='어떤 작동이 일어나야 하나요?', 
    placeholder='예시: 모터 멈춤'
)
st.write(f'선택한 상황: :violet[{reaction}]')


# 텍스트 입력
input_sensor = st.text_input(
    label='입력 장치로 무엇을 사용하나요?', 
    placeholder='예시: 거리 센서'
)
st.write(f'선택한 상황: :violet[{input_sensor}]')


# 텍스트 입력
output = st.text_input(
    label='출력 장치로 무엇을 사용하나요?', 
    placeholder='예시: 모터'
)
st.write(f'선택한 상황: :violet[{output}]')

prompt = f'user:[상황- 금고 잠그기, 작동- 모터 돌리기, 조건- 프로그램이 시작될 때, 입력장치- 없음,출력장치- A모터, B모터], bot: [프로그램을 시작할 때, A모터 속도 설정, 지정된 시간만큼 A모터 작동, A모터를 위치로 이동, 상대 모터 위치를 설정, 부드러운 정지], user: [상황- 인식한 색에 따라 소리 내기, 작동- 효과음 재생, 조건- 노란색 인식, 입력장치- 컬러 센서, 출력장치- 스피커], bot: [허브 버튼을 누를 때, 조건 기다리기, 색상?, 재생하기], user: [상황- 힘센서를 눌러 집게 오므렸다 펴기, 작동- 모터 동작, 조건- 힘센서를 누르고 있을 때, 입력장치- 힘센서, 출력장치- 모터], bot:[프로그램을 시작할 때, 무한 루프, 만약 ~라면, 누름?, 모터 시동 출력, 아니면, 지정된 시간만큼 모터 작동, 모터 멈추기], user: [상황- 달리기 경주, 작동- 모터 동작, 조건- 프로그램 시작, 입력장치- 없음, 출력장치- 모터], bot: [프로그램을 시작할 때, 모터 동작 설정, 동작 속도 설정, 지정된 값만큼 이동], user: [상황- 벽에 부딪히면 멈추기, 작동- 모터 멈추기, 조건- 힘센서가 눌림, 입력장치- 힘센서, 출력장치- 모터], bot: [프로그램을 시작할 때, 무한 루프, 만약 ~라면, 누름?, 모터 시동, 아니면, 모터 멈추기], user: [상황- 밝기에 따라 불 끄고 켜기, 작동- 불 끄기, 조건- 밝음, 입력장치- 컬러센서, 출력장치- 라이트 매트릭스], bot: [프로그램을 시작할 때, 무한 루프, 만약 ~라면, 반사광?, 라이트 매트릭스 픽셀 밝기 설정 100. 아니면, 라이트 매트릭스 픽셀 밝기 설정 0], user: [상황- 허브가 흔들릴 때 라이트 픽셀 깜빡임, 흔들리지 않으면 멈추기, 작동- 라이트 픽셀 깜빡임, 조건- 허브 흔들림, 입력장치- 허브 자이로센서, 출력장치- 라이트 매트릭스], bot: [프로그램을 시작할 때, 무한 루프, 만약 ~라면, 허브 흔들림?, 라이트 매트릭스 픽셀 깜빡임, 아니면, 라이트 매트릭스 멈춤], user: [상황- {situation}, 작동- {reaction}, 조건- {condition}, 입력장치- {input_sensor}, 출력장치- {output}], bot'

# 버튼 클릭
button = st.button(':gift:코드블럭 추천받기')

def generate_recommend(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
 
    message = completions["choices"][0]["text"].replace(",", " ]  [ ")
    return message

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


if button:
    output = generate_recommend(prompt)
    st.write(f'{output}')