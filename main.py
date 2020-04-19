import kivy
import Global

from collections import namedtuple

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
# partial is for functions
from functools import partial
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
from random import randint
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from enum import Enum

from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

Vector2 = namedtuple("Vector2", "x y")
Vector2a = namedtuple("Vector2a", "xa ya")
AppTitle = "Cough-O-Meter: A Mobile Respiratory Illness Diagnostic Tool"

emptyBackground = "images/empty.png"
background = "images/background.png"
first_page = "images/first_page.png"
button_pressed = "images/button-pressed.png"
button_unpressed = "images/button-unpressed.png"


class InputMenu(Screen):
    main_aligner = None
    aligners = []
    screen_info = None
    aligner_offset = -15
    screen_number = 0
    mostPoints = 0
    def __init__(self, new_screen_info, new_screen_number):
        Screen.__init__(self)
        self.screen_info = new_screen_info
        self.name = new_screen_info.screen_title
        self.screen_number = new_screen_number
        for screenInfo in new_screen_info.option_sets:
            print("screenInfo.name: " + str(screenInfo.name) + "\n",end="",flush=True)

    def build(self):
        Global.mapSize = Vector2(x=Window.size[0], y=Window.size[1])
                    
        Clock.schedule_interval(self.update, 1.0/60.0)
        print("NAME: " + self.name)
        if self.name == AppTitle:
            self.add_title_buttons()
        else:
            self.add_top_buttons()
            self.add_bottom_buttons()

        self.main_aligner = WidgetAligner(Direction.VERTICAL, (Global.mapSize.x/2, Global.mapSize.y/2), self.aligner_offset)
        self.aligners.append(self.main_aligner)
        self.add_widget(self.main_aligner, index=3)
        print("Map Size: " + str(Global.mapSize.x) + " " + str(Global.mapSize.y)+"\n", end="", flush=True)


        if self.name == AppTitle:
            self.add_titlepage()
        else:
            title_label = Label(text=self.screen_info.screen_title, font_size='30sp', color=[0, 0, 0, 1], font_name= 'Calibri')
            self.main_aligner.add_widget(title_label)
            self.add_background() 



   
        print("Text: " + self.screen_info.screen_title + "\n", end="", flush=True)

        for option_set in self.screen_info.option_sets:
            self.add_option_set((Global.mapSize.x/2, Global.mapSize.y/2), option_set)


    def add_option_set(self, pos, option_set):
        new_option_set = OptionSetWidget(option_set, Direction.HORIZONTAL, pos, 10)
        self.aligners.append(new_option_set.aligner)
        option_set_label = Label(text=option_set.name, font_size='20sp', color=[0, 0, 0, 1], font_name= 'Calibri')
        self.main_aligner.add_new_widget(option_set_label)
        self.main_aligner.add_new_widget(new_option_set.aligner)

    def update(self, dt):
        Global.mapSize = Vector2(x=Window.size[0], y=Window.size[1])
        for aligner in self.aligners:
            aligner.update()
        #print("Total Points: "+str(Global.GetTotalPoints(Global.screen_info_list))+"\n", end="", flush=True)
    def add_bottom_buttons(self):
        new_aligner = WidgetAligner(Direction.HORIZONTAL, (Global.mapSize.x/2, Global.mapSize.y/20), Global.mapSize.x*0.6)
        self.aligners.append(new_aligner)
        self.add_widget(new_aligner)
        next_button = ChangeScreenButton(ScreenButtonType.NEXT)
        new_aligner.add_widget(next_button)
        previous_button = ChangeScreenButton(ScreenButtonType.PREVIOUS)
        new_aligner.add_widget(previous_button)
    def add_top_buttons(self):
        new_aligner = WidgetAligner(Direction.HORIZONTAL, (Global.mapSize.x/2, Global.mapSize.y*19/20), Global.mapSize.x*0.025)
        self.aligners.append(new_aligner)
        self.add_widget(new_aligner)
        new_button = ChangeScreenButton(ScreenButtonType.TARGET, new_screen_name="RESTART")
        new_aligner.add_widget(new_button, len(new_aligner.children))
        pass
    def add_title_buttons(self):
        new_aligner = WidgetAligner(Direction.HORIZONTAL, (Global.mapSize.x/2, Global.mapSize.y/20), Global.mapSize.x*0.6)
        self.aligners.append(new_aligner)
        self.add_widget(new_aligner)
        start_button = ChangeScreenButton(ScreenButtonType.NEXT, new_screen_name="START")
        new_aligner.add_widget(start_button)

    def add_titlepage(self):
        with self.main_aligner.canvas.before:
            self.rect = Rectangle(size=Global.mapSize, source=first_page)
    def add_background(self):
        with self.main_aligner.canvas.before:
            self.rect = Rectangle(size=Global.mapSize, source=background)
    
 
class ScreenButtonType(Enum):
    NEXT = 0
    PREVIOUS = 1
    TARGET = 2

class ChangeScreenButton(Widget):
    aligner_offset = -15
    main_aligner = []
    aligners = []
    button = ObjectProperty(None)
    screen_name = ""
    button_type = ScreenButtonType.NEXT
    def __init__(self,  new_type,  new_center=(0,0), new_screen_name=""):
        Widget.__init__(self)
        self.button_type = new_type
        self.screen_name = new_screen_name
        self.button.center = new_center
        self.button.text = new_type.name
        #self.button.color = [0,0,0,1]
        self.button.background_normal = button_unpressed
        self.button.background_down = button_pressed
        if new_screen_name != "":
            self.button.text = new_screen_name
    def change_screen(self):
        if self.button_type == ScreenButtonType.NEXT:
            Global.screen_manager.transition.direction = 'left'
            if Global.screen_manager.current == 'Symptoms 6':
                sEmpty = EmptyScreen(name="empty")
                Global.screen_manager.add_widget(sEmpty)
                Global.screen_manager.current = "empty"
                Global.screen_manager.switch_to(Results())    
            else:
                Global.screen_manager.current = Global.screen_manager.next()
        elif self.button_type == ScreenButtonType.PREVIOUS:
            Global.screen_manager.transition.direction = 'right'
            Global.screen_manager.current = Global.screen_manager.previous()
        elif self.button_type == ScreenButtonType.TARGET:
            Global.screen_manager.transition.direction = 'left'
            if Global.screen_manager.current_screen.screen_number > Global.screen_manager.get_screen(AppTitle).screen_number:
                Global.screen_manager.transition.direction = 'right'
            Global.screen_manager.current = AppTitle

class ChangeScreenButton2(Widget):
    button = ObjectProperty(None)
    screen_name = ""
    button_type = ScreenButtonType.NEXT
    def __init__(self,  new_type,  new_center=(0,0), new_screen_name=""):
        Widget.__init__(self)
        self.button_type = new_type
        self.screen_name = new_screen_name
        self.button.center = new_center
        self.button.text = new_type.name
        #self.button.color = [0,0,0,1]
        self.button.background_normal = button_unpressed
        self.button.background_down = button_pressed
        if new_screen_name != "":
            self.button.text = new_screen_name
    def change_screen(self):
        if self.button_type == ScreenButtonType.TARGET:
            Global.screen_manager.current = AppTitle
            
            
class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

class WidgetAligner(Widget):
    button = ObjectProperty(None)
    offset = 0
    center = 0, 0
    direction = Direction.HORIZONTAL
    def __init__(self, new_direction, new_pos, new_offset):
        Widget.__init__(self)
        self.direction = new_direction
        self.center = new_pos
        self.offset = new_offset
    def add_new_widget(self, new_widget):
        self.add_widget(new_widget)
    def update(self):
        self.align_children()
    def align_children(self):
        breadth = -self.offset
        for child in self.children:
            breadth += child.size[self.direction.value] + self.offset
        edge = self.center[self.direction.value] - breadth/2

        for child in self.children:
            if self.direction == Direction.HORIZONTAL:
                child.center = edge+child.size[0]/2, self.center[1]
            else: # self.direction == Direction.VERTICAL:
                child.center = self.center[0], edge+child.size[1]/2
            edge += child.size[self.direction.value] + self.offset
#print(""+str()+"\n",end="",flush=True)


class OptionSetWidget(Widget):
    aligner = None
    option_set = None
    option_widgets = []
    current_selection = None
    def __init__(self, new_option_set, new_direction, new_pos, new_offset):
        Widget.__init__(self)
        self.aligner = WidgetAligner(new_direction, new_pos, new_offset)
        self.option_set = new_option_set
        self.add_options()
    def add_options(self):
        for option in self.option_set.options:
            self.add_new_option(option)
    def add_new_option(self, new_option):
        new_option_widget = OptionWidget(new_option, self)
        self.aligner.add_widget(new_option_widget, len(self.aligner.children))
        self.option_widgets.append(new_option_widget)
    def deselect_all(self, selected_option):
        for child in self.aligner.children:
            if child != selected_option:
                child.deselect()

class EmptyScreen(Screen):
    aligner_offset = -15
    main_aligner = []
    aligners = []
    def __init__(self, **kwargs):
        super(EmptyScreen, self).__init__(**kwargs)
        self.build()
    def build(self):
        Global.mapSize = Vector2(x=Window.size[0], y=Window.size[1])  
        Clock.schedule_interval(self.update, 1.0/60.0)
        self.main_aligner = WidgetAligner(Direction.VERTICAL, (Global.mapSize.x/2, Global.mapSize.y/2), self.aligner_offset)
        self.aligners.append(self.main_aligner)
        self.add_widget(self.main_aligner, index=3)
        self.add_background() 
        self.label = Label(text="",font_size = '15sp', pos=[0,25])
        self.add_widget(self.label)
    def update(self, dt):
        Global.mapSize2 = Vector2a(xa=Window.size[0], ya=Window.size[1])
        for aligner in self.aligners:
            aligner.update()
    def add_background(self):
        with self.main_aligner.canvas.before:
            self.rect = Rectangle(size=Global.mapSize, source=emptyBackground)

class Results(Screen):
    main_aligner = []
    aligners = []
    aligner_offset=-15
    def __init__(self, **kwargs):
        super(Results, self).__init__(**kwargs)
        self.build()
    def build(self):
        Global.mapSize2 = Vector2a(xa=Window.size[0], ya=Window.size[1])
        Clock.schedule_interval(self.update, 1.0/60.0)
        c19, cold, flu, asthma, COPD, LC, PH, P, B = Global.GetTotalPoints(Global.screen_info_list)
        allPoints = [c19, cold, flu, asthma, COPD, LC, PH, P, B]
        percentages = [c19/11.2,cold/11.4,flu/12.8,asthma/9.5,COPD/10.7,LC/12.3,PH/11.5,P/13,B/10.2]
        maxPercentage = max(percentages)
        mostPoints = max(allPoints)

        self.main_aligner = WidgetAligner(Direction.VERTICAL, (Global.mapSize.x/2, Global.mapSize.y/2), self.aligner_offset)
        self.aligners.append(self.main_aligner)
        self.add_widget(self.main_aligner, index=3)

        with self.main_aligner.canvas.before:
            self.rect = Rectangle(size=Global.mapSize, source=background)

        self.main_aligner = WidgetAligner(Direction.VERTICAL, (Global.mapSize2.xa/2, Global.mapSize2.ya/2), self.aligner_offset)
        self.aligners.append(self.main_aligner)
        self.add_widget(self.main_aligner)

        if maxPercentage <= 0.01:
            myResult = "You have virtually no chance of having or contracting any respitory conditions"
            myResultTitle = "No Symptoms Met"
            myTips = "- However if you truly do not feel well, consult a doctor."
        elif mostPoints == c19:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting Covid-19.")
            myResultTitle = "Covid-19"
            myTips ="Tips\n - Get in touch with a healthcare provider. \n - Monitor your symptoms, get immediate help if you experience serious symptoms like trouble breathing. \n - Avoid sharing personal items. \n - Wear a face covering \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == cold:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting the common cold.")
            myResultTitle = "Common Cold"
            myTips = "Tips\n - Get more rest.\n - Drink plenty of fluids. \n - If you have a stuffy nose, try adding more moisture to the air using a humidifier. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == flu:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting influenza.")
            myResultTitle = "Influenza"
            myTips = "Tips\n - Get more rest. \n - Drink plenty of fluids. \n - Monitor your symptoms, get immediate help if you experience serious symptoms like trouble breathing. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == asthma:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting asthma.")
            myResultTitle = "Asthma"
            myTips = "Tips\n - Identify asthma triggers and take steps to avoid them. \n - Get your vaccinations. \n - Take your medications.\n - Avoid catching colds. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == COPD:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting chronic obstructive pulmonary disease.")
            myResultTitle = "Chronic Obstructive Pulmonary Disease"
            myTips = "Tips\n - Do more exercise.\n - Eat a healthier diet. \n - Drink plenty of fluids. \n - Use a humidifier. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == LC:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting lung cancer.")
            myResultTitle = "Lung Cancer"
            myTips = "Tips\n - Eat lots of vegetables and fruits. \n - Exercise regularly. \n - Avoid carcinogens and smoke. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == PH:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting pulmonary hypertension.")
            myResultTitle = "Pulmonary Hypertension"
            myTips = "Tips\n - Get plenty of rest. \n - Exercise regularly. \n - Avoid smokes. \n - Eat a healthy diet. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == P:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting pneumonia.")
            myResultTitle = "Pneumonia"
            myTips = "Tips\n - Get plenty of rest. \n - Drink plenty of fluids. \n - Take your medications as prescribed. \n - If you are at risk or don't feel well, consult a doctor."
        elif mostPoints == B:
            if percentages[0]==1:
                output = "a virtually certain chance"
            elif percentages[0] < 1 and percentages[0] >= 0.80:
                output = "a very likely chance"
            elif percentages[0] < 0.80 and percentages[0] >= 0.60:
                output = "a likely chance"
            elif percentages[0] < 0.60 and percentages[0] >= 0.40:
                output = "about as likely a chance as not"
            elif percentages[0] < 0.40 and percentages[0] >= 0.20:
                output = "an unlikely chance"
            elif percentages[0] < 0.20 and percentages[0] > 0.01:
                output = "a very unlikely chance"
            elif percentages[0] <= 0.01:
                output = "virtually no chance"
            myResult = str("You have " + output + " of having or contracting bronchitis.")
            myResultTitle = "Bronchitus"
            myTips = "Tips\n - Avoid chemical fumes, dusts, smoke, and anything else bothering your lungs. \n - Get plenty of rest. \n - Drink plenty of fluids. \n - If you are at risk or don't feel well, consult a doctor."
        self.label = Label(text=myResult,font_size = '15sp', pos=[0,25], color=[0, 0, 0, 1])
        self.add_widget(self.label)
        self.label2 = Label(text=myResultTitle, font_size='40sp',pos=[0,100], color=[0, 0, 0, 1])
        self.add_widget(self.label2)
        self.label3 = Label(text=myTips, font_size='15sp', pos=[0,-50], color=[0, 0, 0, 1])
        self.add_widget(self.label3)
        self.add_top_buttons()

    def add_top_buttons(self):
        new_aligner = WidgetAligner(Direction.HORIZONTAL, (Global.mapSize2.xa/2, Global.mapSize2.ya*19/20), Global.mapSize2.xa*0.025)
        self.aligners.append(new_aligner)
        self.add_widget(new_aligner)
        new_button = ChangeScreenButton2(ScreenButtonType.TARGET, new_screen_name="RESTART")
        new_aligner.add_widget(new_button)
    def update(self, dt):
        Global.mapSize2 = Vector2a(xa=Window.size[0], ya=Window.size[1])
        for aligner in self.aligners:
            aligner.update()



class OptionWidget(Widget):
    button = ObjectProperty(None)
    highlight = ObjectProperty(None)
    option_set = None
    option = None
    isSelected = False
    def __init__(self, new_option, new_option_set):
        Widget.__init__(self)
        self.option = new_option
        self.button.text = self.option.name
        self.option_set = new_option_set
        self.highlight.opacity = 0
        self.button.background_normal = button_unpressed
        self.button.background_down = button_pressed
    def select(self):
        self.option_set.deselect_all(self)
        self.highlight.opacity = 0
        self.option.chosen = True
        self.button.background_normal = button_pressed
        c19, cold, flu, asthma, COPD, LC, PH, P, B = Global.GetTotalPoints(Global.screen_info_list)
        print("Covid-19 Total Points: "+str(c19) + "\n", end="", flush=True)
        print("Cold Total Points: "+str(cold) + "\n", end="", flush=True)
        print("Flu Total Points: "+str(flu) + "\n", end="", flush=True)
        print("Asthma Total Points: "+str(asthma) + "\n", end="", flush=True)
        print("Chronic Obstructive Pulmonary Disease Total Points: "+str(COPD) + "\n", end="", flush=True)
        print("Lung Cancer Total Points: "+str(LC) + "\n", end="", flush=True)
        print("Pulmonary Hypertension Total Points: "+str(PH) + "\n", end="", flush=True)
        print("Pneumonia Total Points: "+str(P) + "\n", end="", flush=True)
        print("Bronchitis Total Points: "+str(B) + "\n", end="", flush=True)
    def deselect(self):
        self.highlight.opacity = 0
        self.option.chosen = False
        self.button.background_normal = button_unpressed


class DiagnosisApp(App):
    def build(self):
        print("\n",end="",flush=True)
        screen_num = 0
        for screen in Global.screen_info_list:
            new_screen = InputMenu(screen, screen_num)
            new_screen.build()
            Global.screen_manager.add_widget(new_screen)
            screen_num += 1
            print("Screen Name " + str(screen.screen_title) + "\n",end="",flush=True)
        screen2 = Results()
        Global.screen_manager.add_widget(screen2)
        #menu = InputMenu(Global.SampleScreen1)
        #menu.build()
        return Global.screen_manager

if __name__ == '__main__':
    DiagnosisApp().run()
