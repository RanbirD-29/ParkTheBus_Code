import time
import lgpio

# Configuration (Using your exact GPIO numbers)
PWM_PIN = 19   # PWMA (Speed)
DIR1_PIN = 27  # AI1 (Direction 1)
DIR2_PIN = 17  # AI2 (Direction 2)
STBY_PIN = 26

FREQUENCY = 1000  # 1 kHz PWM frequency



def move_robot_forward(speed):
    """
    Moves the motor forward at the specified speed (0 to 100).
    """
    speed = max(0, min(100, speed)) 
    # Open the default GPIO chip (0)
    h = lgpio.gpiochip_open(0)
     # Initialize direction pins as outputs
    lgpio.gpio_claim_output(h, DIR1_PIN)
    lgpio.gpio_claim_output(h, DIR2_PIN)
    lgpio.gpio_claim_output(h, STBY_PIN)
    lgpio.gpio_write(h, STBY_PIN, 1)
    lgpio.gpio_write(h, DIR1_PIN, 1)
    lgpio.gpio_write(h, DIR2_PIN, 0)
    lgpio.tx_pwm(h, PWM_PIN, FREQUENCY, speed)
    print(f"Motor moving FORWARD at {speed}% speed.")

def move_robot_backward(speed):
    """
    Moves the motor backward at the specified speed (0 to 100).
    """
    speed = max(0, min(100, speed))
    
    lgpio.gpio_write(h, DIR1_PIN, 0)
    lgpio.gpio_write(h, DIR2_PIN, 1)
    lgpio.tx_pwm(h, PWM_PIN, FREQUENCY, speed)
    print(f"Motor moving BACKWARD at {speed}% speed.")

def stop_robot(h):
    """
    Stops the motor by cutting the PWM signal and resetting direction pins.
    """
    lgpio.tx_pwm(h, PWM_PIN, FREQUENCY, 0)
    lgpio.gpio_write(h, STBY_PIN, 0)
    lgpio.gpio_write(h, DIR1_PIN, 0)
    lgpio.gpio_write(h, DIR2_PIN, 0)
    lgpio.gpio_free(h, STBY_PIN)
    lgpio.gpio_free(h, DIR1_PIN)
    lgpio.gpio_free(h, DIR2_PIN)
    lgpio.gpiochip_close(h)
    print("Motor STOPPED.")



# --- Example Test Run ---
try:
   
    # Run test sequence
    move_motor_forward(speed=60)
    time.sleep(2)
    
    stop_motor()
    time.sleep(1)
    
    move_motor_backward(speed=60)
    time.sleep(2)
    
    stop_motor()

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")

finally:
    # Safety cleanup
    print("Cleaning up GPIO resources...")
    stop_motor()
    lgpio.gpiochip_close(h)
    print("Done.")