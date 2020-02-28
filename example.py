# 실행 환경 : python3
# 사용 모듈 : request (pip install requests 또는 pip3 install requests)
import requests
import json

token = "" # API KEY 입력

# 글로벌 최신 뉴스
result = requests.get('https://api.moya.ai/globalnews?token=' + token)
result = result.json()
print(result)
# 다음 페이지
nextPage = result['nextPage']

# 다음 페이지 최신 뉴스
# result = requests.get('https://api.moya.ai/globalnews?token=' + token + "&nextPage=" + nextPage)


# 애플과 아마존 최신 뉴스
symbols = "aapl,amzn"
result = requests.get("https://api.moya.ai/globalnews?token=" + token + "&symbol=" + symbols)
result = result.json()
print(result)
# 다음 페이지
nextPage = result['nextPage']

# 다음 페이지 애플과 아마존 최신 뉴스
# result = requests.get("https://api.moya.ai/globalnews?token=" + token + "&symbol=" + symbols + "&nextPage=" + nextPage)

# ID 정보를 이용하여 뉴스 전체 정보 받기
result = requests.get('https://api.moya.ai/globalnews?id=15955748&token=' + token)
result = result.json()
print(result)
