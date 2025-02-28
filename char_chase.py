import keyboard
from time import sleep, time

progressSize = 20
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
    print("_"*30)

def changeDifficulty(diff):
    global maxScore

    maxScore = diff

def deleteLastLine():
    print("\033[F", end="")
    print("\033[K", end="")

def progressBar(progress): # progress je mezi <0,1>
    if progress < 0 or progress > 1:
        return "Wrong progress input"
    
    progress = round(progress, 2)
    
    lineCount = int(progressSize * progress)
    spaceCount = progressSize - lineCount

    if progress < 0.4:
        color = Clr.FAIL
    elif progress < 1:
        color = Clr.WARNING
    else:
        color = Clr.OKGREEN

    bar = f"{color}[{'|' * lineCount}{' ' * spaceCount}] {progress * 100} %{Clr.ENDC}"
    return bar

def playGame():
    global running

    while True:
        inp = input(f"{Clr.OKCYAN}Press as much keys as possible, press 'ENTER' without typing anything to start.\nTo change difficulty, type 'EASY', 'MEDIUM' 'HARD' or if you dare 'IMPOSSIBLE' (Default = MEDIUM)\nPress 'ESC' to exit.\n{Clr.ENDC}").upper()
        if inp == "ESC":
            return
        elif inp in ["EASY", "MEDIUM", "HARD", "IMPOSSIBLE"]:
            changeDifficulty(getattr(Diff, inp))
            print(f"{Clr.BOLD}Difficulty changed to {inp}, {getattr(Diff, inp)} charracters {Clr.ENDC}")
            continue
        elif inp == "":
            break
        else:
            print(f"{Clr.FAIL}Invalid input. Please try again.{Clr.ENDC}")

    score = 0
    running = True

    print(f"{Clr.OKGREEN}\tSTART{Clr.ENDC}")
    line()
    print()
    timeStart = time()
    while running:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            score+=1
            if score>1:
                deleteLastLine()
            print(progressBar(score/maxScore))
        
        if score >= maxScore:
            showEndResults(score, timeStart, True)
        
        if event.name == 'esc':
            showEndResults(score, timeStart, False)

def showEndResults(score, timeStart, won):
    global running

    timeElapsed = time() - timeStart
    running = False

    line()
    if won:
        print(f"{Clr.OKGREEN}\n\t Game won!{Clr.ENDC}")
    else:
        print(f"{Clr.FAIL}\n\t Game lost!{Clr.ENDC}")

    print(f"{Clr.HEADER}\n\t time: {round(timeElapsed, 2)} s\n\t score: {score}{Clr.ENDC}\n")


def main():
    print(f"{Clr.OKBLUE}Starting..\n{Clr.ENDC}")

    playGame()

    print(f"{Clr.FAIL}Exiting..{Clr.ENDC}")


if __name__ == "__main__":
    main()
