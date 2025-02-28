import keyboard
from time import time

progressSize = 50
maxScore = 100

# tahle třída z https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class Clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Diff:
    EASY = 50
    MEDIUM = 100
    HARD = 300
    IMPOSSIBLE = 1000

def line():
    print("_"*65)

def changeDifficulty(diff):
    global maxScore

    maxScore = diff

def deleteLastLine():
    print("\033[F", end="")
    print("\033[K", end="")

def progressBar(progress, timeElapsed): # progress je mezi <0,1>
    if progress < 0 or progress > 1:
        return "Wrong progress input"
    
    progress = round(progress, 2)
    
    lineCount = int(progressSize * progress)
    spaceCount = progressSize - lineCount

    if progress < 0.3:
        color = Clr.FAIL
    elif progress < 0.6:
        color = Clr.WARNING
    elif progress < 1:
        color = Clr.OKCYAN
    else:
        color = Clr.OKGREEN

    bar = f"{color}[{'|' * lineCount}{' ' * spaceCount}] {progress * 100} % {int(timeElapsed)} s{Clr.ENDC}"
    return bar

def playGame():
    global running

    while True:
        inp = input(f"{Clr.OKCYAN}Press 'ENTER' without typing anything to start.\nTo change difficulty, type 'EASY', 'MEDIUM' 'HARD' or if you dare 'IMPOSSIBLE' (Default = MEDIUM) (lower case works too)\nPress 'ESC' to exit.\n{Clr.ENDC}").upper()
        if inp == "ESC":
            return
        elif inp in ["EASY", "MEDIUM", "HARD", "IMPOSSIBLE"]:
            changeDifficulty(getattr(Diff, inp))
            print(f"\n{Clr.BOLD}Difficulty changed to {inp}, {getattr(Diff, inp)} charracters {Clr.ENDC}\n")
            continue
        elif inp == "":
            break
        else:
            print(f"\n{Clr.FAIL}Invalid input. Please try again.{Clr.ENDC}\n")

    score = 0
    running = True

    print(f"{Clr.OKGREEN}\t\tSTART{Clr.ENDC}")
    line()
    print()
    timeStart = time()
    while running:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            timeElapsed = round(time() - timeStart, 2)
            score+=1
            if score>1:
                deleteLastLine()
            print(progressBar(score/maxScore, timeElapsed))
        
        if score >= maxScore:
            showEndResults(score, timeElapsed, True)
        
        if event.name == 'esc':
            showEndResults(score, timeElapsed, False)

def showEndResults(score, timeElapsed, won):
    global running
    running = False

    line()
    if won:
        print(f"|\t\t\t|\n|\t{Clr.OKGREEN}Game won!{Clr.ENDC}\t|")
    else:
        print(f"|\t\t\t|\n|\t{Clr.FAIL}Game lost!{Clr.ENDC}\t|")

    print(f"|\t\t\t|\n|\t{Clr.HEADER} time: {timeElapsed} s{Clr.ENDC}\t|\n|\t{Clr.HEADER} score: {score}{Clr.ENDC}\t|\n|\t\t\t|")
    print(f"|{'_'*23}|\n")


def main():
    print(f"\n\n{Clr.OKBLUE}Welcome to {Clr.BOLD}Char chase{Clr.ENDC}{Clr.OKBLUE}. Your goal is to press as many keys on your keyboard as possible.\n Info:\n{Clr.ENDC}")

    playGame()
    input()

    print(f"{Clr.FAIL}Exiting..{Clr.ENDC}")


if __name__ == "__main__":
    main()
