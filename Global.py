# Global.py
from collections import namedtuple
from kivy.uix.screenmanager import ScreenManager, Screen

MY_NUMBER = 0
Vector2 = namedtuple("Vector2", "x y")
Vector2a = namedtuple("Vector2a", "xa ya")

mapSize = Vector2(x=0, y=0)
mapSize2 = Vector2a(xa=0, ya=0)

screen_info_list = []

def GetTotalPoints(screen_info_list):
    totalC19 = 0
    totalCold = 0
    totalFlu = 0
    totalAsthma = 0 
    totalCOPD = 0
    totalLC = 0
    totalPH = 0
    totalP = 0
    totalB = 0
    cC19 = 0
    cCold = 0
    cFlu = 0
    cAsthma = 0 
    cCOPD = 0
    cLC = 0
    cPH = 0
    cP = 0
    cB = 0
    for screen_info in screen_info_list:
        cC19,cCold,cFlu,cAsthma,cCOPD,cLC,cPH,cP,cB = screen_info.get_total()
        totalC19 += cC19
        totalCold += cCold
        totalFlu += cFlu
        totalAsthma += cAsthma
        totalCOPD += cCOPD
        totalLC += cLC
        totalPH += cPH
        totalP += cP
        totalB += cB
    return totalC19,totalCold,totalFlu,totalAsthma,totalCOPD,totalLC,totalPH,totalP,totalB

class ScreenInfo():
    def __init__(self, new_screen_title):
        self.option_sets = []
        self.screen_title = new_screen_title
    def add_option_set(self, new_option_set):
        self.option_sets.append(new_option_set)
    def get_total(self):
        totalvalue = 0
        totalvalue2 = 0
        totalvalue3 = 0
        totalvalue4 = 0
        totalvalue5 = 0
        totalvalue6 = 0
        totalvalue7 = 0
        totalvalue8 = 0
        totalvalue9 = 0
        cvalue = 0
        cvalue2 = 0
        cvalue3 = 0
        cvalue4 = 0
        cvalue5 = 0
        cvalue6 = 0
        cvalue7 = 0
        cvalue8 = 0
        cvalue9 = 0
        for option_set in self.option_sets:
            cvalue,cvalue2,cvalue3,cvalue4,cvalue5,cvalue6,cvalue7,cvalue8,cvalue9 = option_set.get_score()
            totalvalue += cvalue
            totalvalue2 += cvalue2
            totalvalue3 += cvalue3
            totalvalue4 += cvalue4
            totalvalue5 += cvalue5
            totalvalue6 += cvalue6
            totalvalue7 += cvalue7
            totalvalue8 += cvalue8
            totalvalue9 += cvalue9
        return totalvalue,totalvalue2,totalvalue3,totalvalue4,totalvalue5,totalvalue6,totalvalue7,totalvalue8,totalvalue9

class OptionSet():
    def __init__(self, option_set_name, option_list):
        self.name = option_set_name
        self.options = option_list
    def add_option(self, new_option):
        self.options.append(new_option)
    def get_score(self):
        for option in self.options:
            if option.chosen == True:
                return option.value,option.value2,option.value3,option.value4,option.value5,option.value6,option.value7,option.value8,option.value9
        return 0,0,0,0,0,0,0,0,0

class Option():
    name = ""
    value = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0
    value6 = 0
    value7 = 0
    value8 = 0
    value9 = 0
    chosen = False
    def __init__(self, option_name, option_value, option_value2, option_value3, option_value4, option_value5, option_value6, option_value7, option_value8, option_value9 ):
        self.name = option_name
        self.value = option_value
        self.value2 = option_value2
        self.value3 = option_value3
        self.value4 = option_value4
        self.value5 = option_value5
        self.value6 = option_value6
        self.value7 = option_value7
        self.value8 = option_value8
        self.value9 = option_value9

# Title Page
TitlePage = ScreenInfo("Cough-O-Meter: A Mobile Respiratory Illness Diagnostic Tool")
screen_info_list.append(TitlePage)

#Sample Screen 1
SampleScreen1 = ScreenInfo("Risk Factors 1")
screen_info_list.append(SampleScreen1)

Screen1OptionSet1 = OptionSet("How old are you?", [
    Option("age<1 ", 0,1,1,0,0,0,0,1,0),
    Option("1<age<2",0,0,1,0,0,0,0,1,0),
    Option("2<age<6",0,0,1,0,0,0,0,0,0),
    Option("6<age<65",0,0,0,0,0,0,0,0,0),
    Option("age>65", 1,0,1,0,0,0,0,1,0)
])
SampleScreen1.add_option_set(Screen1OptionSet1)
Screen1OptionSet2 = OptionSet("Do you have any chronic illnesses or a weakened immune system?", [
    Option("yes",1,1,1,0,1,0,0,1,0),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen1.add_option_set(Screen1OptionSet2)
Screen1OptionSet3 = OptionSet("Is the current season fall or winter?", [
    Option("yes",  0,1,0,0,0,0,0,0,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
SampleScreen1.add_option_set(Screen1OptionSet3)

#Sample Screen 2
SampleScreen2 = ScreenInfo("Risk Factors 2")
screen_info_list.append(SampleScreen2)

Screen2OptionSet1 = OptionSet("Have you been to crowded areas?", [
    Option("yes",1,1,1,0,0,0,0,0,0),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen2.add_option_set(Screen2OptionSet1)
Screen2OptionSet2 = OptionSet("Have you had any exposure to smoking cigarettes (firsthand or secondhand)?", [
    Option("yes",1,1,0,1,1,1,0,1,1),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen2.add_option_set(Screen2OptionSet2)
Screen2OptionSet3 = OptionSet("Do you or have you worked in an environment that exposes \n     you to lung irritants such as dusts and/or chemicals?", [
    Option("yes",0,0,0,1,1,1,1,0,1),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen2.add_option_set(Screen2OptionSet3)

#Sample Screen 3
SampleScreen3 = ScreenInfo("Risk Factors 3")
screen_info_list.append(SampleScreen3)

Screen3OptionSet1 = OptionSet("Are you overweight?", [
    Option("yes",1,0,0,1,0,0,1,0,0),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen3.add_option_set(Screen3OptionSet1)
Screen3OptionSet2 = OptionSet("Are you aware of any family members that have lung cancer?", [
    Option("yes",0,0,0,0,0,1,0,0,0),
    Option("no", 0,0,0,0,0,0,0,0,0),
])
SampleScreen3.add_option_set(Screen3OptionSet2)
Screen3OptionSet3 = OptionSet("Are you aware of any family members that have pulmonary hypertension?", [
    Option("yes",0,0,0,0,0,0,1,0,0),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen3.add_option_set(Screen3OptionSet3)

#Sample Screen 4
SampleScreen4 = ScreenInfo("Risk Factors 4")
screen_info_list.append(SampleScreen4)

Screen4OptionSet1 = OptionSet("Have you undergone any type of radiation therapy in the past?", [
    Option("yes",0,0,0,0,0,1,0,0,0),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen4.add_option_set(Screen4OptionSet1)
Screen4OptionSet2 = OptionSet("Have you used drugs (Weight-loss, Illegal, Selective Seretonin Reuptake Inhibitors)?", [
    Option("yes",0,0,0,0,0,0,1,0,0),
    Option("no",   0,0,0,0,0,0,0,0,0)
])
SampleScreen4.add_option_set(Screen4OptionSet2)
Screen4OptionSet3 = OptionSet("Do you experience regurgitation or heartburn?", [
    Option("yes",0,0,0,0,0,0,0,0,1),
    Option("no", 0,0,0,0,0,0,0,0,0)
])
SampleScreen4.add_option_set(Screen4OptionSet3)

#symptoms screen 1
Symptoms = ScreenInfo("Symptoms 1")
screen_info_list.append(Symptoms)

SymptomsOptionSet1 = OptionSet("Do you have a Fever > 37.6 degrees celsius?", [
    Option("yes",1,0.2,1,0,0,0,0,1,0.2),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms.add_option_set(SymptomsOptionSet1)
SymptomsOptionSet2 = OptionSet("Have you been coughing?", [
    Option("yes",1,1,1,1,1,1,1,1,1),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms.add_option_set(SymptomsOptionSet2)
SymptomsOptionSet3 = OptionSet("Have you recently started experiencing a loss or alteration of smell or taste?", [
    Option("yes",0.6,0.5,0.5,0,0,0.3,0,0,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms.add_option_set(SymptomsOptionSet3)

#symptoms screen 2
Symptoms2 = ScreenInfo("Symptoms 2")
screen_info_list.append(Symptoms2)

Symptoms2OptionSet1 = OptionSet("Have you recently started experiencing lingering tiredness?", [
    Option("yes",0.5,0.5,1,0.5,1,1,1,0.5,1),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms2.add_option_set(Symptoms2OptionSet1)
Symptoms2OptionSet2 = OptionSet("Have you suddenly been experiencing muscle or chest pain lately?", [
    Option("yes",0.2,1,1,1,0.7,1,0.5,1,0.8),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms2.add_option_set(Symptoms2OptionSet2)
Symptoms2OptionSet3 = OptionSet("Do you currently have a runny or stuffy nose?", [
    Option("yes",0.2,1,0.5,0,0,0,0,0,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms2.add_option_set(Symptoms2OptionSet3)

#symptoms screen 3
Symptoms3 = ScreenInfo("Symptoms 3")
screen_info_list.append(Symptoms3)

Symptoms3OptionSet1 = OptionSet("Do you currently have a sore throat? ", [
    Option("yes",0.5,1,0.5,0,0,0,0,0,0.8),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms3.add_option_set(Symptoms3OptionSet1)
Symptoms3OptionSet2 = OptionSet("Have you been having diarrhea recently?", [
    Option("yes",0.2,0,0.3,0,0,0,0,0.5,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms3.add_option_set(Symptoms3OptionSet2)
Symptoms3OptionSet3 = OptionSet("Do you currently have a headache?", [
    Option("yes",0.5,0.2,1,0,0,1,0,0,0.8),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms3.add_option_set(Symptoms3OptionSet3)

#symptoms screen 4
Symptoms4 = ScreenInfo("Symptoms 4")
screen_info_list.append(Symptoms4)

Symptoms4OptionSet1 = OptionSet("Are you currently experiencing a shortness of breath?", [
    Option("yes",0.5,0,0,1,1,1,1,1,0.8),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms4.add_option_set(Symptoms4OptionSet1)
Symptoms4OptionSet2 = OptionSet("Have you been sneezing a lot lately?", [
    Option("yes",0,1,0,0,0,0,0,0,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms4.add_option_set(Symptoms4OptionSet2)
Symptoms4OptionSet3 = OptionSet("Have you been coughing up blood or a lot of spit or phlegm recently?", [
    Option("yes",0,0,0,0,1,1,0,0.5,0.2),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms4.add_option_set(Symptoms4OptionSet3)

#symptoms screen 5
Symptoms5 = ScreenInfo("Symptoms 5")
screen_info_list.append(Symptoms5)

Symptoms5OptionSet1 = OptionSet("Have you recently been experiencing swelling in your ankles and knees?", [
    Option("yes",0,0,0,0,0,0,1,0,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms5.add_option_set(Symptoms5OptionSet1)
Symptoms5OptionSet2 = OptionSet("Has your heart been beating a lot faster than normal? ", [
    Option("yes",0,0,0,1,0.5,0,1,1,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms5.add_option_set(Symptoms5OptionSet2)
Symptoms5OptionSet3 = OptionSet("When you breathe, do you hear wheezing sounds?", [
    Option("yes",0,0,0,1,1,1,0,0.5,0.8),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms5.add_option_set(Symptoms5OptionSet3)

#symptoms screen 6
Symptoms6 = ScreenInfo("Symptoms 6")
screen_info_list.append(Symptoms6)

Symptoms6OptionSet1 = OptionSet("Have you recently been experiencing swelling in your ankles and knees?", [
    Option("yes",1,0,0,1,1,1,1,0,0.8),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms6.add_option_set(Symptoms6OptionSet1)
Symptoms6OptionSet2 = OptionSet("Has your heart been beating a lot faster than normal? ", [
    Option("yes",0,0,0,0,0.5,0,1,1,0),
    Option("no",0,0,0,0,0,0,0,0,0)
])
Symptoms6.add_option_set(Symptoms6OptionSet2)

ResultsNeeded = ScreenInfo("")
screen_info_list.append(ResultsNeeded)


screen_manager = ScreenManager()