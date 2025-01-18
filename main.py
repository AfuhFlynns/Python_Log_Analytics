# Import utils data
from utils import Log_Handler

class App:
    def __init__(self):
        self.name = "John Dalton"
        self.successful = False

    def get_user_name(self):
        user_name = input("Please enter your name here: ")
        return user_name

    def intro(self):
        print("**** This is simple log analytics program ****")

    def call_utils_methods(self):
        log_handler = Log_Handler(self.name)

        if self.name == "":
            self.name = "User"

        print(f"\n******** Hello, {self.name} do the following ********")
        self.successful = log_handler.handle_value_error()

        if self.successful == True:
            self.successful = log_handler.handle_division_by_zero_error ()

        if self.successful == True:
            self.successful = log_handler.handle_file_write_read_error()

    def app(self):
        self.intro()
        self.name = self.get_user_name()
        self.call_utils_methods()


if __name__ == "__main__":
    app = App()
    app.app()
