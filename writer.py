import os


class Writer:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, message):
        if os.path.isfile(self.file_name):
            with open(self.file_name, "r") as input_file:
                data = input_file.read()
            with open(self.file_name, "w+") as output_file:
                output_file.write(data)
                output_file.write("\n")
                output_file.write(message)
        else:
            with open(self.file_name, "w+") as output_file:
                output_file.write(message)

