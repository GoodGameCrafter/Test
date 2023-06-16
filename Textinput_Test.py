from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class MainWin(Screen):
    def __init__(self):
        super(MainWin,self).__init__()
        self.name = "main"
        textinput = ObjectProperty(None)

    def toSecond(self,val:int):
        sm.current = "second"
        Win2(val)

    def setText(self,filepathname:str,val:int):
        if val == 0:
            print(filepathname,val)
            self.textinput.text = filepathname

class Win2(Screen):
    def __init__(self,val:int = 0):
        super(Win2, self).__init__()
        self.name = "second"
        self.val = val

    def toMain(self,val:int):
        sm.current = "main"

    def openFile(self, filepathname: str):
        if filepathname != []:
            sm.current = "main"
            MainWin().setText(filepathname[0],self.val)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("test.kv")
sm = WindowManager()
screens = [MainWin(),Win2()]
for screen in screens:
    sm.add_widget(screen)
sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()
