from pathfinder_editor_widget import PathfinderEditorWidget

def pathfinder_editor():
    from pyforms import start_app
    start_app(PathfinderEditorWidget, geometry=(200, 200, 800, 200))


if __name__ == '__main__':
    pathfinder_editor()
