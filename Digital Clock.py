from threading import *
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from datetime import datetime
from time import sleep

#Window.size = (x,y)

class Digital_Clock(App):

    class Task1(Thread):
        
        def run(self):
            self.current = datetime.now()
            self.time = self.current.strftime("%H:%M:%S")
            self.s, self.m, self.h = int(self.time[6:]), int(self.time[3:5]), int(self.time[0:2])

            if self.h > 9:
                self.h -= 12

            while True:
                self.s += 1
                if self.s > 59:
                    self.s = 0
                    self.m += 1
                if self.m > 59:
                    self.m = 0
                    self.h += 1
                if self.h > 23:
                    self.h = 0
                if self.s < 10:
                    self.c = '0'
                else:
                    self.c = ''
                if self.m < 10:
                    self.b = '0'
                else:
                    self.b = ''
                if self.h < 10:
                    self.a = '0'
                else:
                    self.a = ''
                
                root.display.text = self.a + str(self.h) + ' : ' + self.b + str(self.m) + ' : ' + self.c + str(self.s)
                sleep(1)
            

    def build(self):
        self.display = Button(text = 'Testing', font_size = '100dp', color = [1, 1, 1, 1], size_hint = (0.7,0.3), 
                            pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}, background_normal = '', background_down = '', 
                            background_color = [0, 0, 0, 1])

        t1 = self.Task1()
        t1.start()
        return self.display



root = Digital_Clock()

if __name__ == '__main__':
    root.run()
