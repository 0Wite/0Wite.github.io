import requests

#LINE API必須設定
url = "https://notify-api.line.me/api/notify"
access_token = 'FpABRaqzi4Q2/4mTYyKKLuzaxRjVll9IDrFqI7/M1fDleIxLjoYfYPMS3OKAf7d2cl8VpPnvB/1DJi53oKWsz1FjKbFDOE0TA1a2uxhfje9mEyH+IPQGuYnxSOo/H0BzpG3hnLWiD4ywV/gKTVrSrQdB04t89/1O/w1cDnyilFU='
headers = {'Authorization': 'Bearer ' + access_token}

#message送信
message = 'test'
payload = {'message': message}
r = requests.post(url, headers=headers, params=payload,)