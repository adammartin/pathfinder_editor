# Pathfinder Editor



## Development

### Setup

#### Prerequisites


Running tasks requires Bash version 4.3 or greater. Check your Bash version with

```sh
bash --version
```

If your version is below this, install a newer version of Bash, e.g.,

```sh
brew install bash
```

Python version 3.6 or greater is required with pip installed.

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


#### Initialize venv



### Tasks

To run all tasks, invoke

```sh
bin/analyze_and_test.sh
```

To invoke individual tasks, see below:

#### Static analysis

```sh
bin/analyze_python.sh
```

#### Run the unit tests

```sh
bin/run_unit_tests.sh
```
