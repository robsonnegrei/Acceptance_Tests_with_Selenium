# Set up

We'll need a few things to install for this section:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)
- install requirements via pip install into the python Virtual env for this project by using requirements.txt file from source directory

### Linux/MacOS
``` bash
source venv/bin/activate
pip install -r requirements.txt 
```

### Windows
``` bash
pip install virtualenv
virtualenv venv
venv\Scripts\Activate.bat
```


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

### Linux/MacOS

```bash
source venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```
### Windows

```bash
venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```