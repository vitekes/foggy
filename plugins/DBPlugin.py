import motor

class DBPlugin:
    def __init__(self):
        self.client = motor.MotorClient('localhost', 27017)