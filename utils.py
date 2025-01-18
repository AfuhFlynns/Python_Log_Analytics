# Handles the date and time format
import datetime
# Handles the paths to files
import os.path


class Log_Handler:
    def handle_log_file(self, level, message, stack_trace):
        # File path setup
        log_path = './logfile.log'
        # Open file in append mode
        f = open(log_path, 'a')
        # Modify file content
        f.write(f'Time: {datetime.datetime.now()}-Level: {level}-Message: {message}-StackTrace: {stack_trace}\n')
        # Close every file after opening
        f.close()

        # Explanation
        # f = open("testfile.txt", "a")
        # f.write("I am the flash genome")
        # f.write(f'here lies exception handling {error_handle()}')

        # f.close()



    def handle_value_error(self):
        try:
            value = int(input("If you would please enter an integer value: "))
            print(f"You entered: {value}")
        except ValueError as error:
            self.handle_log_file("ERROR", "Expected an integer as input but a non-integer value was provided")
        finally:
            print("Well done, you have successfully entered an integer")
            print(value)
