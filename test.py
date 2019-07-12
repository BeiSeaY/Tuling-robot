import pyttsx3
from test_project.test02 import Jarvis
from test_project.helloworld import opentxt

engine = pyttsx3.init()
engine.say("wlcome intelligence system ")
engine.runAndWait()


def fn():
    while True:
        user = input('>>>')
        if user == 'quit':
            engine.say("ByeBye，Boss")
            engine.runAndWait()
            break
        if user == "星期五":
            engine.say("Hi，Boss，I am 星期五 I'm going to open and close the application")  # 本地控制
            engine.runAndWait()
            if opentxt() == "bye,Boss":
                break
        if user == "贾维斯":
            engine.say("Hello。Boss，I am 贾维斯 I'm an intelligent robot")  # 智能语音
            engine.runAndWait()
            if Jarvis() == "bye,Boss":
                break
        else:
            engine.say("please valid input command，星期五，贾维斯，quit")
            engine.runAndWait()


if __name__ == "__main__":
    fn()
