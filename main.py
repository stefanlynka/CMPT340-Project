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

from kivy.uix.widget import Widget

Vector2 = namedtuple("Vector2", "x y")


class InputMenu(Screen):
    main_aligner = None
    aligners = []
    screen_info = None
    aligner_offset = 40
    screen_number = 0
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

        self.add_top_buttons()
        self.add_bottom_buttons()

        self.main_aligner = WidgetAligner(Direction.VERTICAL, (Global.mapSize.x/2, Global.mapSize.y/2), self.aligner_offset)
        self.aligners.append(self.main_aligner)
        self.add_widget(self.main_aligner)
        print("Map Size: " + str(Global.mapSize.x) + " " + str(Global.mapSize.y)+"\n", end="", flush=True)
        title_label = Label(text=self.screen_info.screen_title, font_size='60sp')
        self.main_aligner.add_widget(title_label)
        print("Text: " + self.screen_info.screen_title + "\n", end="", flush=True)

        for option_set in self.screen_info.option_sets:
            self.add_option_set((Global.mapSize.x/2, Global.mapSize.y/2), option_set)

    def add_option_set(self, pos, option_set):
        new_option_set = OptionSetWidget(option_set, Direction.HORIZONTAL, pos, 10)
        self.aligners.append(new_option_set.aligner)
        self.main_aligner.add_new_widget(new_option_set.aligner)

    def update(self, dt):
        Global.mapSize = Vector2(x=Window.size[0], y=Window.size[1])
        for aligner in self.aligners:
            aligner.update()
        #print("Total Points: "+str(self.screen_info.get_total())+"\n", end="", flush=True)
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
        for screen in Global.screen_info_list:
            new_button = ChangeScreenButton(ScreenButtonType.TARGET, new_screen_name=screen.screen_title)
            new_aligner.add_widget(new_button, len(new_aligner.children))
        pass

class ScreenButtonType(Enum):
    NEXT = 0
    PREVIOUS = 1
    TARGET = 2

class ChangeScreenButton(Widget):
    button = ObjectProperty(None)
    screen_name = ""
    button_type = ScreenButtonType.NEXT
    def __init__(self,  new_type,  new_center=(0,0), new_screen_name=""):
        Widget.__init__(self)
        self.button_type = new_type
        self.screen_name = new_screen_name
        self.button.center = new_center
        self.button.text = new_type.name
        if new_screen_name != "":
            self.button.text = new_screen_name
    def change_screen(self):
        if self.button_type == ScreenButtonType.NEXT:
            Global.screen_manager.transition.direction = 'left'
            Global.screen_manager.current = Global.screen_manager.next()
        elif self.button_type == ScreenButtonType.PREVIOUS:
            Global.screen_manager.transition.direction = 'right'
            Global.screen_manager.current = Global.screen_manager.previous()
        elif self.button_type == ScreenButtonType.TARGET:
            Global.screen_manager.transition.direction = 'left'
            if Global.screen_manager.current_screen.screen_number > Global.screen_manager.get_screen(self.screen_name).screen_number:
                Global.screen_manager.transition.direction = 'right'
            Global.screen_manager.current = self.screen_name



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
    def select(self):
        self.option_set.deselect_all(self)
        self.highlight.opacity = 1
        self.option.chosen = True
        print("Total Points: "+str(Global.GetTotalPoints(Global.screen_info_list)) + "\n", end="", flush=True)
    def deselect(self):
        self.highlight.opacity = 0
        self.option.chosen = False





class DiagnosisApp(App):
    def build(self):
        print("\n",end="",flush=True)

        screen_num = 0
        for screen in Global.screen_info_list:
            new_screen = InputMenu(screen, screen_num)
            new_screen.build()
            Global.screen_manager.add_widget(new_screen)
            screen_num += 1
            print("Screen Name " + str(new_screen.name) + "\n",end="",flush=True)


        #menu = InputMenu(Global.SampleScreen1)
        #menu.build()
        return Global.screen_manager

if __name__ == '__main__':
    DiagnosisApp().run()