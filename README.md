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

## Usage Example
Using Cough-O-Meter is simple. Once you click start, you will be faced with a series of questions. These questions will be related to your lifestyle, the symptoms you may have, and your overall health. Simply answer the questions truthfully, and in the end, the tool will predict what respiratory illness you may have. 

The following is one set of answers that we provided to obtain "a virtually certain chance of having or contracting Covid-19."
```
How old are you? age>65
Do you have any chronic illnesses or a weakened immune system? yes
Is the current season fall or winter? no
Have you been to crowded areas? yes
Have you had any exposure to smoking cigarettes (firsthand or secondhand)? yes
Do you or have you worked in an environment that exposes you to lung irritants such as dusts and/or chemicals? no
Are you overweight? yes
Are you aware of any family members that have lung cancer? no
Are you aware of any family members that have pulmonary hypertension? no
Have you undergone any type of radiation therapy in the past? no
Have you used drugs (Weight-loss, Illegal, Selective Serotonin Reuptake Inhibitors? no
Do you experience regurgitation or heartburn? no 

Do you have a fever > 37.6 degrees celsius? yes
Have you been coughing? yes
Have you recently started experiencing a loss or alteration of smell or taste? yes
Have you recently started experiencing lingering tiredness? yes
Have you suddenly been experiencing muscle or chest pain lately? yes
Do you currently have a runny or stuffy nose? yes
Do you currently have a sore throat? yes
Have you been having diarrhea recently? yes
Do you currently have a headache? yes
Are you currently experiencing a shortness of breath? yes
Have you been sneezing a lot lately? no
Have you been coughing up blood or a lot of spit or phlegm recently? no
Have you recently been experiencing swelling in your ankles and knees? no
Has your heart been beating a lot faster than normal? no
When you breathe, do you hear wheezing sounds? no
Do you feel a sense of tightness or pressure in your chest? yes
Are you noticing a bluish tint to your lips and/or skin? no
```

