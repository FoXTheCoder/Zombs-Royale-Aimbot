from PIL import Image
import pyautogui
import sys


color = (253, 200, 118)

def main():
    while True:
        cmd = input("Enter Aimbot Command: ")
        cmd = cmd.lower()
        if cmd == "help":
            print("""\nList of commands:\n  
            help - Displays a List of Commands
            start - Activate the Aimbot
            exit - Exit this Script\n""")
        elif cmd == "start":
            aimbot_go()
        elif cmd == "exit":
            sys.exit()
        else:
            print("\nInvalid command...\n")

def aimbot_go():
    print("\nAimbot Activated!\n")

    while True:
        
        pic = pyautogui.screenshot()

      
        pix_val = list(pic.getdata())

        
        if color in pix_val:
          
            pixel_index = pix_val.index(color)
            yCord = pixel_index % pic.width
            xCord = pixel_index // pic.width

            
            pyautogui.moveTo(yCord, xCord)
        else:
            pass

if __name__ == "__main__":
    main()
