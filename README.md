How to run app.py without installing dependencies globally (using venv)

*Recommended if fellas want to test the code in local (work folder), without having to install python and the dependencies/library globally.

*We give the dependency lists in the requirements.txt file

*Open the terminal

1. Creating new venv in the work folder

```
python -m venv venv
```

2. Activate the venv

```
./venv/scripts/activate
```

3. Install the dependencies from the `requirements.txt` file in the venv

```
pip install -r requirements.txt
```

4. After installing the dependencies, fellas can run the python code.
```
python app.py
```
