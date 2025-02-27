import keyboard
from time import sleep

def changeDifficulty():
    pass

def playGame():
    pass

def showEndResults():
    pass

def main():
    print("Press any key. Press 'esc' to exit.")
    
    while True:
        # Wait for any key press
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            print(f"KEYBOARD INPUT: {event.name}")
        
        # Exit if 'esc' is pressed
        if event.name == 'esc':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
