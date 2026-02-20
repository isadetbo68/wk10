class MainWindow(QMainWindow):
    def __init__(self, log_source: ILogSource):
        super().__init__()
        self.log_source = log_source
        self.load_logs()
        self.init_UI()
        self.show()
        self.log_display.setReadOnly(True)
        
    
    def load_logs(self):
        lpgs = self.log_source