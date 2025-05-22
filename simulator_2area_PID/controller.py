class PIDController:
    def __init__(self, Kp, Ki, Kd, dt, output_limits=(-0.1, 0.1), integral_limits=(-10, 10)):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.output_limits = output_limits
        self.integral_limits = integral_limits
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, error):
        self.integral += error * self.dt
        self.integral = max(self.integral_limits[0], min(self.integral_limits[1], self.integral))

        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error

        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        return max(self.output_limits[0], min(self.output_limits[1], output))
