# Global.py
from collections import namedtuple
from kivy.uix.screenmanager import ScreenManager, Screen

MY_NUMBER = 0
Vector2 = namedtuple("Vector2", "x y")

mapSize = Vector2(x=0, y=0)

screen_info_list = []

def GetTotalPoints(screen_info_list):
    total = 0
    for screen_info in screen_info_list:
        total += screen_info.get_total()
    return total

class ScreenInfo():
    total_score = 0
    def __init__(self, new_screen_title):
        self.option_sets = []
        self.screen_title = new_screen_title
    def add_option_set(self, new_option_set):
        self.option_sets.append(new_option_set)
    def get_total(self):
        total_score = 0
        for option_set in self.option_sets:
            total_score += option_set.get_score()
        return total_score

class OptionSet():
    def __init__(self, option_set_name, option_list):
        self.name = option_set_name
        self.options = option_list
    def add_option(self, new_option):
        self.options.append(new_option)
    def get_score(self):
        for option in self.options:
            if option.chosen == True:
                return option.value
        return 0

class Option():
    name = ""
    value = 0
    chosen = False
    def __init__(self, option_name, option_value):
        self.name = option_name
        self.value = option_value

#Sample Screen 1
SampleScreen1 = ScreenInfo("Sample Screen 1")
screen_info_list.append(SampleScreen1)

SampleOptionSet1 = OptionSet("Sample Options 1", [
    Option("option 1",1),
    Option("option 2",2),
    Option("option 3",3)
])
SampleScreen1.add_option_set(SampleOptionSet1)
SampleOptionSet2 = OptionSet("Sample Options 2", [
    Option("option 4",4),
    Option("option 5",5),
    Option("option 6",6),
    Option("option 6.5", 7)
])
SampleScreen1.add_option_set(SampleOptionSet2)
SampleOptionSet3 = OptionSet("Sample Options 3", [
    Option("option 7",7),
    Option("option 8",8),
    Option("option 9",9)
])
SampleScreen1.add_option_set(SampleOptionSet3)

#Sample Screen 2
SampleScreen2 = ScreenInfo("Sample Screen 2")
screen_info_list.append(SampleScreen2)

SampleOptionSet1 = OptionSet("Sample Options 1", [
    Option("option 10",1),
    Option("option 11",1),
    Option("option 12",2),
    Option("option 13",3),
    Option("Option 14",4)
])
SampleScreen2.add_option_set(SampleOptionSet1)
SampleOptionSet2 = OptionSet("Sample Options 2", [
    Option("option 15",4),
    Option("option 16",5),
    Option("option 17",7)
])
SampleScreen2.add_option_set(SampleOptionSet2)
SampleOptionSet3 = OptionSet("Sample Options 3", [
    Option("option 18",7),
    Option("option 19",8),
    Option("option 20",9),
    Option("option 21",10)
])
SampleScreen2.add_option_set(SampleOptionSet3)

#Sample Screen 3
SampleScreen3 = ScreenInfo("Sample Screen 3")
screen_info_list.append(SampleScreen3)

SampleOptionSet1 = OptionSet("Sample Options 1", [
    Option("option 10",1),
    Option("option 11",1),
    Option("option 12",2),
    Option("option 13",3)
])
SampleScreen3.add_option_set(SampleOptionSet1)
SampleOptionSet2 = OptionSet("Sample Options 2", [
    Option("option 14",4),
    Option("option 15",5),
    Option("option 17",7)
])
SampleScreen3.add_option_set(SampleOptionSet2)
SampleOptionSet3 = OptionSet("Sample Options 3", [
    Option("option 18",7),
    Option("option 19",8),
])
SampleScreen3.add_option_set(SampleOptionSet3)

screen_manager = ScreenManager()