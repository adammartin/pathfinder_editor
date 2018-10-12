import wx
from pathfinder_editor_window import PathfinderEditorWindow


def pathfinder_editor():
    app = wx.App()
    frm = PathfinderEditorWindow(None, title='Pathfinder Editor')
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    pathfinder_editor()
