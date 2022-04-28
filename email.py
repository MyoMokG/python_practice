import re

txt = "testemail123@smu.ac.kr와 email456sample@naver.com에서 이메일이 도착하였습니다."

output = re.findall("\S+@[a-z.]+",txt)

print(output)
