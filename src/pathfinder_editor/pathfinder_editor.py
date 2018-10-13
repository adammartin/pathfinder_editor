import atexit
from tkinter import Tk
from widgets.defaults import default_style
from widgets.pathfinder_window import PathfinderTkWindow


def pathfinder_editor():
    root = Tk()
    default_style()
    root.title("Pathfinder Editor")
    app = PathfinderTkWindow(master=root)
    atexit.register(app.on_destroy)
    app.mainloop()
    root.destroy()


if __name__ == '__main__':
    pathfinder_editor()
