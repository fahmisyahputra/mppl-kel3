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

5. After running the python code, fellas can simply go to the link given by flask (127.0.0.1:5000).

![terminal](https://media.discordapp.net/attachments/916254669771276288/1243441966989971467/image.png?ex=66517d12&is=66502b92&hm=e82976d26a807230b2a9afff6e5049800d1d035313ced6287e28f7b247d8df33&=&format=webp&quality=lossless)



Another alternative to test the program is to visit this link below

http://ivanfahmiobi.pythonanywhere.com/