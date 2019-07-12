import os
import pyttsx3

engine = pyttsx3.init()
def opentxt():
    while True:
        user_input = input('wclocom 星期五 >>>')
        if user_input == "quit":
            engine.say("星期五 quit")
            engine.runAndWait()
            return "bye,Boss"
        if user_input == "opmusic":
            os.startfile(r"C:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe")
        elif user_input == "opdict":
            os.startfile(r"C:\Users\Administrator\AppData\Local\youdao\dict\Application\YoudaoDict.exe")
        elif user_input == "opwx":
            os.startfile(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
        elif user_input == "clmusic":
            os.system("taskkill /F /IM cloudmusic.exe")
        elif user_input == "clwx":
            os.system("taskkill /F /IM WeChat.exe")
        elif user_input == "cldict":
            os.system("taskkill /F /IM YoudaoDict.exe")
        else:
            engine.say("command Error")
        engine.runAndWait()


if __name__ == "__main__":
    opentxt()
