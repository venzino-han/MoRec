import requests
import logging
import traceback

def send_message(mssaage):
    try:
        url = "https://hooks.slack.com/services/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" # 
        header = {'Content-type': 'application/json'}
        icon_emoji = ":slack:"
        username = "TEST"
        attachments = [{
            "color": "#cb0000",
            "text": f"{mssaage}"
        }]

        data = {"username": username, "attachments": attachments, "icon_emoji": icon_emoji}
        print(data)

        # 메세지 전송
        return requests.post(url, headers=header, json=data)
        
    except Exception as e:
        print("Slack Message 전송에 실패했습니다.")
        print("에러 내용 : " + e)

        exit(0)
 
