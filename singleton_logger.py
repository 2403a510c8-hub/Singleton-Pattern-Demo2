
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
            print("New Logger instance created")
        else:
            print("Using existing Logger instance")

        return cls._instance

    def add_log(self, msg):
        self.logs.append(msg)
        print("Log added:", msg)

    def get_logs(self):
        return self.logs


# Demonstration
logger1 = Logger()

logger2 = Logger()

print("\nAre both instances same?", logger1 is logger2)

logger1.add_log("First log message")
logger2.add_log("Second log message")

print("\nLogger Entries:")
for log in logger1.get_logs():
    print(log)
