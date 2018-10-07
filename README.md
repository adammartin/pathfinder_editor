# Pathfinder Editor

I created this project really to learn about building a deployable python and pyforms.  It became very enjoyable as a project.  For those that know me you may be shocked that I chose not to TDD this project.  

Basically all the system does is allow the user to navigate and open a save game.  It will then extract that save file and then load the data necessary to allow the players to edit their main character.  The 3 files that matter are header.json (defines the save file name), player.json (where money is stored), and party.json (where the stats are stored).  When saved it will persist the edits and compress them into a new unique .zks safe file.   The file should be unique based off of the current time and it's save label will be pre-pended by "Edited - ".

Feel free to help submit additional features!  I don't plan on long term maintenance of this project as it's been a learning experience for me more then anything.

#### Prerequisites

All instructions assume a mac or linux environment.  Windows instruction will be very similar but pathing will be different.

Python version 3.6 or greater is required with pip installed.

You need to have a virtual env set up.  You can do this with the following command executed at the root fo the project:

```sh
python3 -m venv venv/pathfinder_editor
```

Activate the virtual env

```sh
source venv/pathfinder_editor/bin/activate
```

To install dependencies using pip execute the following command in development environment:

```sh
pip install -r requirements.txt
```

To install dependencies using pip in the production environment use the following command:

```sh
pip install -r requirements.prod.txt
```

To install the local directory for testing and execution purposes use the following command at the root of the project.

```sh
pip install -e .

```

#### Environment Variables

Before running any tasks, be sure to source the build environment variables file:

```sh
. build_variables.sh
```

## Development

If you want to participate in this project and make it long lived, then I suggest treating it like a legacy project and adding tests.  TDD would be a great idea.  I've used some simple scripts that I like from production projects that make life easy.

#### build_editor.sh

This script is probably the one you will use the most.  Under the covers it will run static analysis and if successful will turn around and compile the project into an executable using a python tool called nuitka.   If you want to build this project on a Windows platform you can!  If you want to build it for Linux you can (I don't know why you would)!

```sh
./bin/build_editor.sh
```

#### analyze_and_test.sh

This script will analyze the code base using static analysis and then execute tests.  It is not used much because there are no tests.

```sh
bin/analyze_and_test.sh
```

#### analyze_python.sh

This script will simply execute the static analysis.

```sh
bin/analyze_python.sh
```

#### Run the unit tests

Completely useless right now since we have no tests.

```sh
bin/run_unit_tests.sh
```
