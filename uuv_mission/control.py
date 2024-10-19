# control.py

class PDController:
    def __init__(self, KP=0.15, KD=0.6):
        self.KP = KP
        self.KD = KD
        self.previous_error = 0

    def compute_control_action(self, current_error):
        # Compute the derivative of the error
        derivative_error = current_error - self.previous_error
        
        # Compute the control action
        control_action = self.KP * current_error + self.KD * derivative_error
        
        # Update the previous error
        self.previous_error = current_error
        
        return control_action