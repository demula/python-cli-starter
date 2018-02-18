# python-cli-starter

Starter project for python CLI utils

## Init project

```sh
# Copy files
git clone https://github.com/demula/python-cli-starter.git
cd python-cli-starter

# Create a virtual environment to not mess up with your current python installation
virtualenv venv
. venv/bin/activate

# Install required libraries for development
make init
```

## Developing

To manually test the cli util:

```sh
# Install the current code in your venv
make install

# Run your app (using the name you gave it in setup.py, app_cli is the default given for the starter pack)
app_cli --help

# Remember to get out of the venv when you're done developing for the day
deactivate
```

## Testing

Tests are located in `tests/` and run with nose2

```sh
make test
```

## Checking code quality

Coverage and static quality analysis are run with:

```sh
make test_coverage
make check
```

## Generating the documentation

Using sphinx to generate html documentation:

```sh
make generate_docs
```

## Updating requirements file and setup.py file

To override the requirements.txt with the current venv use

```sh
make update_requirements
```

## Packing app for distribution

Package python app as .tar.gz and wheel format

```sh
make dist
```
