import random
from pygame import time
import launchpad_py as launchpad
import os
import requests
import webbrowser as wb
import threading
import time as t
lp = launchpad.Launchpad()
lp.Open()

def main():
    setupleds()
    while True:
        buts = lp.ButtonStateRaw()
        if buts != []:
            butnummber = buts[0]
            butstate = buts[1]
            if butstate == True:
                if butnummber == 200:
                    rauf()
                elif butnummber == 201:
                    runter()
                elif butnummber == 205:
                    ledon()
                elif butnummber == 206:
                    ledoff()
                elif butnummber == 8:
                    lampeon()
                elif butnummber == 24:
                    lampeoff()
                elif butnummber == 120:
                    shutdown()
                elif butnummber == 0:
                    stop()
                elif butnummber == 112:
                    lul = threading.Thread(target=opentodo)
                    lul.start()
                    lp.LedCtrlRaw(112, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(112, 0, 3)
                elif butnummber == 113:
                    lul = threading.Thread(target=openfirefox)
                    lul.start()
                    lp.LedCtrlRaw(113, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(113, 0, 3)
                elif butnummber == 114:
                    lul = threading.Thread(target=opentermius)
                    lul.start()
                    lp.LedCtrlRaw(114, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(114, 0, 3)
                elif butnummber == 115:
                    lul = threading.Thread(target=openserver)
                    lul.start()
                    lp.LedCtrlRaw(115, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(115, 0, 3)
                elif butnummber == 97:
                    lul = threading.Thread(target=openmail)
                    lul.start()
                    lp.LedCtrlRaw(97, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(97, 0, 3)
                elif butnummber == 116:
                    lul = threading.Thread(target=openyt)
                    lul.start()
                    lp.LedCtrlRaw(116, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(116, 0, 3)
                elif butnummber == 80:
                    lul = threading.Thread(target=openword)
                    lul.start()
                    lp.LedCtrlRaw(80, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(80, 0, 3)
                elif butnummber == 81:
                    lul = threading.Thread(target=openpowerpoint)
                    lul.start()
                    lp.LedCtrlRaw(81, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(81, 0, 3)
                elif butnummber == 82:
                    lul = threading.Thread(target=openexel)
                    lul.start()
                    lp.LedCtrlRaw(82, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(82, 0, 3)
                elif butnummber == 83:
                    lul = threading.Thread(target=openteams)
                    lul.start()
                    lp.LedCtrlRaw(83, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(83, 0, 3)
                elif butnummber == 98:
                    lul = threading.Thread(target=openwh)
                    lul.start()
                    lp.LedCtrlRaw(98, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(98, 0, 3)
                elif butnummber == 99:
                    lul = threading.Thread(target=opendc)
                    lul.start()
                    lp.LedCtrlRaw(99, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(99, 0, 3)
                elif butnummber == 100:
                    lul = threading.Thread(target=openpycharm)
                    lul.start()
                    lp.LedCtrlRaw(100, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(100, 0, 3)
                elif butnummber == 84:
                    lul = threading.Thread(target=opencc)
                    lul.start()
                    lp.LedCtrlRaw(84, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(84, 0, 3)
                elif butnummber == 96:
                    lul = threading.Thread(target=openexplorer)
                    lul.start()
                    lp.LedCtrlRaw(96, 3, 1)
                    time.wait(560)
                    lp.LedCtrlRaw(96, 0, 3)
                elif butnummber == 207:
                    rainbow()
                elif butnummber == 204:
                    normal()
                elif butnummber == 64:
                    lp.ButtonFlush()
                    lp.LedCtrlString("Tim!", 0, 3, -1)
                    setupleds()
                elif butnummber == 48:
                    print("nice")
                    lp.ButtonFlush()
                    nice()
                    setupleds()
                print(butnummber)
                #t.sleep(1)
            else:
                t.sleep(1)

def setupleds():
    lp.ButtonFlush()
    lp.LedCtrlRaw(0, 0, 3)
    lp.LedCtrlRaw(200, 0, 3)
    lp.LedCtrlRaw(201, 0, 3)
    lp.LedCtrlRaw(205, 0, 3)
    lp.LedCtrlRaw(206, 0, 3)
    lp.LedCtrlRaw(8, 0, 3)
    lp.LedCtrlRaw(24, 0, 3)
    lp.LedCtrlRaw(120, 0, 3)
    lp.LedCtrlRaw(112, 0, 3)
    lp.LedCtrlRaw(113, 0, 3)
    lp.LedCtrlRaw(114, 0, 3)
    lp.LedCtrlRaw(115, 0, 3)
    lp.LedCtrlRaw(97, 0, 3)
    lp.LedCtrlRaw(116, 0, 3)
    lp.LedCtrlRaw(80, 0, 3)
    lp.LedCtrlRaw(81, 0, 3)
    lp.LedCtrlRaw(82, 0, 3)
    lp.LedCtrlRaw(83, 0, 3)
    lp.LedCtrlRaw(98, 0, 3)
    lp.LedCtrlRaw(99, 0, 3)
    lp.LedCtrlRaw(100, 0, 3)
    lp.LedCtrlRaw(84, 0, 3)
    lp.LedCtrlRaw(96, 0, 3)
    lp.LedCtrlRaw(207, 0, 3)
    lp.LedCtrlRaw(204, 0, 3)
    lp.LedCtrlRaw(64, 0, 3)
    lp.LedCtrlRaw(48, 0, 3)

def nice():
    z = 0
    while z < 1200:
        time.wait(random.randint(0,30))
        lp.LedCtrlRaw(random.randint(0, 127), random.randint(0, 3), random.randint(0, 3))
        z = z+1



def runter():
    print("runter")
    uff = requests.get("http://10.0.1.73:8087/set/hm-rega.0.4168.ProgramExecute?value=true")
    lp.LedCtrlRaw(201, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(201, 0, 3)

def rauf():
    print("rauf")
    uff = requests.get("http://10.0.1.73:8087/set/hm-rega.0.4156.ProgramExecute?value=true")
    lp.LedCtrlRaw(200, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(200, 0, 3)

def stop():
    print("stop")
    uff = requests.get("http://10.0.1.73:8087/set/hm-rega.0.4180.ProgramExecute?value=true")
    lp.LedCtrlRaw(0, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(0, 0, 3)

def shutdown():
    print("Shutdown")
    lp.LedCtrlRaw(120, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(120, 0, 3)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def ledon():
    print("LED ON")
    uff = requests.get("http://10.0.1.73:8087/set/wled.0.483fda499ffa.on?value=true")
    lp.LedCtrlRaw(205, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(205, 0, 3)

def ledoff():
    print("LED OFF")
    uff = requests.get("http://10.0.1.73:8087/set/wled.0.483fda499ffa.on?value=false")
    lp.LedCtrlRaw(206, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(206, 0, 3)

def lampeon():
    print("Lampe On")
    uff = requests.get("http://10.0.1.50/4/off")
    lp.LedCtrlRaw(8, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(8, 0, 3)

def lampeoff():
    print("Lampe Off")
    uff = requests.get("http://10.0.1.50/4/on")
    lp.LedCtrlRaw(24, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(24, 0, 3)

def opentodo():
    print("Open Todo")
    os.system("C:\\Verknüpfungen\\Microsoft.lnk")

def openfirefox():
    print("Open Firefox")
    os.system("C:\\Verknüpfungen\\firefox.exe.lnk")

def opentermius():
    print("Open Termius")
    os.system("C:\\Users\\Tim\\AppData\\Local\\Programs\\Termius\\Termius.exe")

def openmail():
    print("Open Mail")
    os.system("C:\\Verknüpfungen\\Mail.lnk")

def openserver():
    print("Open Server")
    wb.open("https://10.0.1.40:8006/#v1:0:=node%2Fpve:4:5:19::::11:")

def openyt():
    print("Open YT")
    wb.open('https://www.youtube.com/')

def openword():
    print("Open Word")
    os.system("C:\\Verknüpfungen\\WINWORD.EXE.lnk")

def openpowerpoint():
    print("Open PowerPoint")
    os.system("C:\\Verknüpfungen\\POWERPNT.EXE.lnk")

def openexel():
    print("Open Exel")
    os.system("C:\\Verknüpfungen\\EXCEL.EXE.lnk")

def openteams():
    print("Open Teams")
    os.system("C:\\Verknüpfungen\\MicrosoftTeams.lnk")

def opendc():
    print("Open Dc")
    os.system("C:\\Users\\Tim\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")

def openwh():
    print("Open whatsapp")
    os.system('C:\\Users\\Tim\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

def openpycharm():
    print("Open Pycharm")
    os.system("C:\\Verknüpfungen\\pycharm64.exe.lnk")

def opencc():
    print("Open CreativeCloud")
    os.system("C:\\Verknüpfungen\\CreativeCloud.exe.lnk")

def openexplorer():
    print("Open Explorer")
    os.system("C:\\Windows\\explorer.exe")

def rainbow():
    print("WLED RAINBOW")
    uff = requests.get("http://10.0.1.73:8087/set/wled.0.483fda499ffa.seg.0.fx?value=9")
    lp.LedCtrlRaw(207, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(207, 0, 3)

def normal():
    print("Wled normal")
    uff = requests.get("http://10.0.1.73:8087/set/wled.0.483fda499ffa.seg.0.fx?value=0")
    lp.LedCtrlRaw(204, 3, 1)
    time.wait(560)
    lp.LedCtrlRaw(204, 0, 3)

main()