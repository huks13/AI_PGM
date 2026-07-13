import os
import subprocess
import asyncio
from datetime import datetime
import edge_tts

# 경기 결과 입력 받는 곳
place = input("경기가 열린 곳은? ")
time_input = input("경기가 열린 시간은? ")
opponent = input("상대 팀은? ")
goals = int(input("손흥민은 몇 골을 넣었나요? "))
aids = int(input("도움은 몇 개인가요? "))
score_me = int(input("손흥민 팀이 넣은 골 수는? "))
score_you = int(input("상대 팀이 넣은 골 수는? "))

# 기사 작성하는 곳
current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분")
news = f"[프리미어 리그 속보({current_time})]\n"
news = news + "손흥민 선수는 " + place + "에서 " + time_input + "에 열린 경기에 출전하였습니다. "
news = news + "상대 팀은 " + opponent + "입니다. "

# 1. 팀 승패 결과 메시지
if score_me > score_you:
    result = "win"
    news = news + "손흥민 선수의 팀이 " + str(score_me) + "골을 넣어 " + str(score_you) + "골을 넣은 상대 팀을 이겼습니다. "
elif score_me < score_you:
    result = "lose"
    news = news + "손흥민 선수의 팀이 " + str(score_me) + "골을 넣어 " + str(score_you) + "골을 넣은 상대 팀에게 졌습니다. "
else:
    result = "draw"
    news = news + "두 팀은 " + str(score_me) + "대" + str(score_you) + "로 비겼습니다. "

# 2. 승패(result)에 따른 손흥민 선수의 활약 메시지
if result == "win":
    if goals > 0 and aids > 0:
        news = news + "손흥민 선수는 " + str(goals) + "골에 도움 " + str(aids) + "개로 승리를 크게 이끌었습니다. "
    elif goals > 0 and aids == 0:
        news = news + "손흥민 선수는 " + str(goals) + "골로 승리를 이끌었습니다. "
    elif goals == 0 and aids > 0:
        news = news + "손흥민 선수는 골은 없지만 도움 " + str(aids) + "개로 승리하는 데 공헌하였습니다. "
    else:
        news = news + "팀은 승리했지만 아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰습니다. "
        
elif result == "lose" or result == "draw":
    if goals > 0 or aids > 0:
        news = news + "손흥민 선수가 " + str(goals) + "골 " + str(aids) + "도움으로 분전했으나, 팀의 패배를 막지는 못했습니다. "
    else:
        news = news + "아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰고, 팀도 아쉬운 결과를 맞이했습니다. "

# 기사 텍스트 출력
print("\n" + news)
print("선희 목소리로 뉴스 음성을 생성하고 있습니다...")

# 파일이 무조건 현재 실행 중인 폴더(0707) 안에 생성되도록 경로 강제 지정
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir, "son_news.mp3")

# edge-tts는 비동기(async) 방식으로 작동하여 별도의 함수 작성이 필요합니다
async def generate_speech():
    # 성우를 선희(ko-KR-SunHiNeural)로 지정합니다
    communicate = edge_tts.Communicate(news, "ko-KR-SunHiNeural")
    await communicate.save(filename)

# 음성 파일 생성 실행
asyncio.run(generate_speech())

# 윈도우 기본 플레이어로 재생
subprocess.run(["cmd", "/c", "start", filename])