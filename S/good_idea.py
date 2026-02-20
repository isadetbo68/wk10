class PDFreportgenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        pass

class Excelreportgenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        pass

class Emailsender:
    def __init__(self, recipient):
        self.recipient = recipient
    def send_email(self, report):
        pass