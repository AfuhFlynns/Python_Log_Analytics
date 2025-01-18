# Import utils data
from "utils.py" import Log_Handler

class App:
    def __init__(self, name):
        self.name = name

    def get_user_name(self):
        user_name = input("Enter your name here: ")
        return user_name

    def intro(self):
        print("**** This is simple log analytics program ****")

    def call_utils_methods(self):
        log_handler = Log_Handler()

    def app(self):
        self.intro()
        self.name = self.get_user_name()
        self.call_utils_methods()
