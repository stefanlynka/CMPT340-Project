# Cough-O-Meter

Cough-O-Meter is a respiratory illness diagnostic tool completed as a final project for CMPT 340.  


## Getting Started

Below is a set of instructions from the [Kivy installation guide](https://kivy.org/doc/stable/installation/installation-windows.html), for the minimum installation required for the tool to work on Windows. Please refer to the full set of [Kivy installation guides](https://kivy.org/doc/stable/gettingstarted/installation.html) for instructions on how to install Kivy on other platforms. 

Before running Kivy, an installation of [Python](https://www.python.org/downloads/windows/) must be present. After installation, check to ensure that Python was successfully installed by running the following in the command line:

```bash
python ––version
```

Now, to install Kivy. First, we need to install the latest pip, wheel, and virtualenv. We can do this by: 
```bash
python -m pip install --upgrade pip wheel setuptools virtualenv
```

Then, to create and activate a virtual environment, we run:

```bash
python -m virtualenv kivy_venv
kivy_venv\Scripts\activate
```

Then, we need to install the dependencies. 

```bash
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
```

Note, for Python 3.5+, angle backend can be used instead of glew. Install angle backend by:

```bash
python -m pip install kivy_deps.gstreamer==0.1.*
```

Finally, to install Kivy, we run:
```bash
python -m pip install kivy==1.11.1
```

## Running the Application

Before continuing, ensure that the Kivy virtual environment is active by checking if the path is prefaced with (kivy_venv) in the command line. 

Now, in the command line, navigate to the CMPT340-Project folder and run:

```bash
python main.py
```
Cough-O-Meter should now be opened in a new window. 

## Example Results
