from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        return Label(text="Daily Routine")

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()
