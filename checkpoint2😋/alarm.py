def main():
    is_armed = True
    motion_detected = True
    door_open = False
    is_night = False
    display_alarm(is_armed, motion_detected, door_open,is_night)

def display_alarm(i, ms, dp, n):
    if i:
        if ms:
            print("INTRUDER ALERT!!! CALLING 911 XD")
        if dp:
            print("Alert: The door is open.")
    else:
        if n and ms:
            print("Welcome home! Turning the lights on.")


main()