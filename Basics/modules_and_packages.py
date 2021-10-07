#Writing modules
#game.py
#import the draw module

import draw

def play_game():
    ...

def main()
    result = play_game()
    draw.draw_game(result)

if __name__ == '__main__':
    main()

#draw.py
def draw_game():
    ...

def clear_screen(screen):
    ...

#Importing module objects to the current namespace
#game.py
#Import the draw module
from draw import draw_game
def main():
    result = play_game()
    draw_game(result)

#Import all objects from a module
from draw import *

def main():
    result = play_game()
    draw_game(result)

#custom import name
#game.py
#import the draw module
if visual_mode:
    #in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    #this can either be visual or textual depending on visual_mode
    draw.draw_game(result)

#Module initialization
def draw_game():
    #when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main _screen as a singleton
main_screen = Screen()



#Extending module load path
PYTHONPATH=/foo python game.py
sys.path.append("/foo") #execute before import command

#Exploring built-in modules
#import the library
import urllib

#use it
urllib.urlopen(...)
help(urllib.urlopen)
#we can look for which functions are implemented in each module by using the dir function:
#>>>import urllib
#>>>dir(urllib)
# Writing packages
import foo.bar
from foo import bar

#__init__.py
__init__.py:
__all__ = ["bar"]
