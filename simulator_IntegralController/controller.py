class IntegralController:
    def __init__(self, Ki, dt):
        self.Ki = Ki
        self.integral = 0.0
        self.dt = dt

    def reset(self):
        self.integral = 0.0

    def update(self, error):
        self.integral += error * self.dt
        return self.Ki * self.integral