# control.py

class Controller:
    def __init__(self, Kp: float, Kd: float):
        # Proportional and Derivative gains for the controller
        self.Kp_gain = Kp
        self.Kd_gain = Kd
        self.prev_error = 0  # Store the previous timestep error

    def control(self, setpoint: float, feedback: float) -> float:
        # Calculate current error
        current_error = setpoint - feedback
        # Compute the derivative (change in error)
        error_delta = current_error - self.prev_error
        # PD control action: u[t] = Kp * e[t] + Kd * Δe[t]
        control_output = self.Kp_gain * current_error + self.Kd_gain * error_delta
        # Update the previous error for the next timestep
        self.prev_error = current_error
        return control_output
