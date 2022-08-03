import requests
import pprint
import json
import pandas as pd

t = pd.DataFrame([])
for page in range(1, 12):
    url = f'https://openapi.gg.go.kr/Publtolt?Key=136b9d03b0514bb2adaad515ad481912&pIndex={page}&pSize=1000&Type=json'

    response = requests.get(url)

    contents = response.text

    json_ob = json.loads(contents)
    body = json_ob['Publtolt'][1]["row"]

    df = pd.DataFrame(body)
    t = pd.concat([t, df])
print(t)


t.to_excel('toilet.xlsx', index=False, encoding='utf-8')