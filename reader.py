class Reader:
    def __init__(self, file_name):
        with open(file_name, "r") as input_file:
            print(input_file.read().split(","))