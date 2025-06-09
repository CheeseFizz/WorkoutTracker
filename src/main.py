from wx import App

from graphics import *
from utilities import *
from structures import *

def main():

    # Just the Hello World example for now
    app = wx.App()
    # Then a frame.
    frm = AppFrame(None, title="Hello World")

    # Show it.
    frm.Show()

    # Start the event loop.
    app.MainLoop()

if __name__ == "__main__":
    main()