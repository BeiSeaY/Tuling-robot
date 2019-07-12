import pyttsx3
import requests
import json


def Jarvis():
    robot = "http://openapi.tuling123.com/openapi/api/v2"
    while True:
        user_input = input('welcome 贾维斯 >>>')
        engine = pyttsx3.init()
        if user_input == 'quit':
            engine.say("贾维斯qiut")
            engine.runAndWait()
            return "bye,Boss"
        else:
            re = {
                "perception": {
                    "inputText": {
                        "text": user_input
                    }
                },
                "userInfo": {
                    "apiKey": "cf974cc7247b4fa69284377b503b0cd3",
                    "userId": "robot"
                }
            }
            re = json.dumps(re).encode("utf8")
            response = requests.post(robot, re)
            js = json.loads(response.text)
            robot_response = js['results'][0]["values"]["text"]
            print(robot_response)
            engine.say(robot_response)
            engine.runAndWait()

if __name__ == "__main__":
    print(Jarvis())


