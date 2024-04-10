import re

text = "파이썬###CookBook$$$@@@열공중1234"
result = re.sub(r'[^ㄱ-ㅎ가-힣a-zA-Z]+', '', text)
print(result)
