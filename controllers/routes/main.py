from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.Flex144.styles.display='none'


    at.Flex309.styles.display='none'
    at.Flex311.styles.display='none'
    at.Flex381.styles.display='none'
    at.Flex383.styles.display='none'

    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.Image27.onClick:
        at.Flex61.styles.left='calc(100px - 100vw)'
    if at.Image26.onClick:
        at.Flex61.styles.left='calc(100px)'

    if at.Image59.onClick or at.Image60.onClick :
        at.Flex144.styles.display='flex'
        at.Flex164.styles.display='none'
    
    if at.Image56.onClick or at.Image57.onClick :
        at.Flex144.styles.display='none'
        at.Flex164.styles.display='flex'

    
    if at.Image131.onClick or at.TextBox257.onClick :
        at.Flex308.styles.display = 'none'
        at.Flex309.styles.display = 'flex'
    
    if at.Image123.onClick or at.TextBox245.onClick :
        at.Flex308.styles.display = 'flex'
        at.Flex309.styles.display = 'none'
    
    
    if at.Image132.onClick or at.TextBox259.onClick :
        at.Flex310.styles.display = 'none'
        at.Flex311.styles.display = 'flex'
    if at.Image124.onClick or at.TextBox246.onClick :
        at.Flex310.styles.display = 'flex'
        at.Flex311.styles.display = 'none'
    
    if at.Image162.onClick or at.TextBox306.onClick :
        at.Flex384.styles.display = 'none'
        at.Flex383.styles.display = 'flex'
    if at.Image160.onClick or at.TextBox302.onClick :
        at.Flex384.styles.display = 'flex'
        at.Flex383.styles.display = 'none'

    if at.Image161.onClick or at.TextBox304.onClick :
        at.Flex382.styles.display = 'none'
        at.Flex381.styles.display = 'flex'
    if at.Image159.onClick or at.TextBox301.onClick :
        at.Flex382.styles.display = 'flex'
        at.Flex381.styles.display = 'none'

        
    
    pass