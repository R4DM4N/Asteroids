from collections import ChainMap
from constants import *

defaults = { "SCREEN_WIDTH": 1280,
            "SCREEN_HEIGHT": 720,
            "BACKGROUND": BLACK,
            "LANGUAGE": "ENGLISH",
            "DIFFICULTY": "MEDIUM",
            "PLAYERS": 1,
}
user = {}

settings = ChainMap(user, defaults)

def main():
    title()
    print("User settings test")
    settings["SCREEN_WIDTH"] = 640
    settings["SCREEN_HEIGHT"] = 480

    print("Screen Width:", settings["SCREEN_WIDTH"], " Screen Height:", settings["SCREEN_HEIGHT"])

def title():
    name = ["Ass", "Ter", "Oyds", "Blaster"]
    for word in name:
        print(word.center(40," "))
    print("\n\n Settings")
    options()
    
def options():
    for _, (k,v) in enumerate(settings.items()):
        print(k, v)


if __name__ == "__main__":
    main()
