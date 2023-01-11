import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

Builder.load_file("./all_alarm_screen.kv")
Builder.load_file("./new_alarm_screen.kv")
Builder.load_file("./menu.kv")

class AllAlarmScreen(Screen):
    pass

class NewAlarmScreen(Screen):
    pass

class AlarmScreen(Screen):
    pass

class MainApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(AlarmScreen(name='alarm_screen'))
        sm.add_widget(NewAlarmScreen(name='new_alarm_screen'))
        sm.add_widget(AllAlarmScreen(name='all_alarm_screen'))
        sm.current = 'alarm_screen'
        return sm

if __name__ == '__main__':
    MainApp().run()
