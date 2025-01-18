# Handles the date and time format
import datetime
# Handles the paths to files
import os.path


class Log_Handler:
    def __init__(self, name):
        self.name = name


    def handle_log_file(self, level, message, stack_trace, user_name):
        # File path setup
        log_path = './logfile.log'
        # Open file in append mode
        f = open(log_path, 'a')
        # Modify file content
        f.write(f'Time: {datetime.datetime.now()},  Level: {level},  Message: {message},  StackTrace: {stack_trace}, Author: {user_name}\n')
        # Close every file after opening
        f.close()

        # Explanation
        # f = open("testfile.txt", "a")
        # f.write("I am the flash genome")
        # f.write(f'here lies exception handling {error_handle()}')

        # f.close()

    def print_user_input(self, value):
        print(f"You entered: {value}")

    def handle_value_error(self):
        try:
            # Handle integer input
            num = int(input("Please enter an integer value: "))
            self.print_user_input(num)
            # Handle float input
            height = float(input("Enter a float "))
            self.print_user_input(height)
        except ValueError as e:
            # Handle exception and log it to the log file
            self.handle_log_file("ERROR", "Input type not allowed!", e, self.name)
            print(f"Sorry you entered an unauthorized value!")
        except KeyboardInterrupt as e:
            self.handle_log_file("WARN", "Keyboard interrupted script execution", e, self.name)
            print(f"Sorry program was interrupted!")
        finally:
            return True

    def handle_division_by_zero_error(self):
        try:
            num1 = 4
            num2 = int(input("Enter a value greater than zero to divide by (4): "))
            result = num1 / num2
        except ValueError as e:
            # Handle exception and log it to the log file
            self.handle_log_file("ERROR", "Input type not allowed!", e, self.name)
            print(f"Sorry you entered an unauthorized value!")
        except ZeroDivisionError as e:
            self.handle_log_file("ERROR", "User entered unauthorized value", e, self.name)
            print(f"Sorry you entered an unauthorized value!")
        except KeyboardInterrupt as e:
            self.handle_log_file("WARN", "Keyboard interrupted script execution", e, self.name)
            print(f"Sorry program was interrupted!")
        finally:
            return True

    def handle_file_write_read_error(self):
        try:
            file_path = str(input("Enter a file path for a file to be read and displayed: "))
            # Open the file in read mode
            read_file = open(f"./{file_path}", "r")
            count = 0
            for line in read_file:
                count = count + 1
                print(f"Line: {count}, {line}\n")
            print("File read complete!!")

            read_file.close()

            file_path = str(input("Enter a file path for a file to write into: "))
            # Open the file in write mode
            write_file = open(f"./{file_path}", "w")
            count = 0
            while count < 3:
                write_file.write(f"Line: {count}, Some text here\n")
                count = count + 1
            print("File write complete!!")

            write_file.close()
        except ValueError as e:
            # Handle exception and log it to the log file
            self.handle_log_file("ERROR", "Input type not allowed!", e, self.name)
            print(f"Sorry you entered an unauthorized value!")
        except FileExistsError as e:
            self.handle_log_file("INFO", "File path does not exist", e, self.name)
            print(f"Sorry you entered a false file path")
        except FileNotFoundError as e:
            self.handle_log_file("ERROR", "File path or file not found", e, self.name)
            print(f"Sorry you entered a false file path")
        except KeyboardInterrupt as e:
            self.handle_log_file("WARN", "Keyboard interrupted script execution", e, self.name)
            print(f"Sorry program was interrupted!")
        finally:
            return True