from pathfinder_editor_widget import PathfinderEditorWidget

def pathfinder_editor():
    from pyforms import start_app
    start_app(PathfinderEditorWidget)


if __name__ == '__main__':
    pathfinder_editor()
