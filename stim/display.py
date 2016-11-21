from expy import shared
from expy.colors import *
from .draw import *
from expy.response import *

def clear():
    '''
    Clear the screen

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    shared.win.fill(shared.background_color)
    shared.pg.display.flip()

def show(out_time=False, clean_screen=True, backup=None):
    '''
    Display current canvas buffer, and keep the display during a limited period.

    Parameters
    ----------
    out_time: int(>0), False(default)
        The time limit of current function. 
    clean_screen: True(default), False
        Whether clear the screen after get the screen or not. 
    backup: None, or a screen backup
        Give a prepared screen to display

    Returns
    -------
    None
    '''
    if backup:
        shared.win.blit(backup, (0, 0))
    shared.pg.display.flip()
    if out_time:
        waitForResponse(K_RETURN, out_time)
        if clean_screen:
            clear()

def getScreen(clean_screen=True):
    '''
    Get a backup of current canvas

    Parameters
    ----------
    clean_screen: True(default), False
        Whether clear the screen after get the screen or not. 

    Returns
    -------
    None
    '''
    backup = shared.pg.display.get_surface().convert()
    if clean_screen:
        clear()
    return backup
