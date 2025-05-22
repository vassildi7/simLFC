import numpy as np

class IntegralController:
    def __init__(self, Ki, dt, deadband=1e-6, output_limits=(-np.inf, np.inf)):
        self.Ki = Ki
        self.dt = dt
        self.deadband = deadband
        self.output_limits = output_limits
        self.integral = 0.0

    def reset(self):
        self.integral = 0.0

    def update(self, error):
        if abs(error) > self.deadband:
            self.integral += error * self.dt

        # Compute raw output
        output = self.Ki * self.integral

        # Apply output limits
        output = max(self.output_limits[0], min(output, self.output_limits[1]))

        return output

