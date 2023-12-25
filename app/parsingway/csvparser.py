

class CSVParser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        print(f"CSVParser: parsing {self.path}")
        # with open(self.path, 'r') as file:
        #    return file.read()
