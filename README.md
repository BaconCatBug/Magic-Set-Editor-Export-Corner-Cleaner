Usage:

Download either the .py file and .bat file, or download one of the precompiled exe files.

(Click the green "Code" button and download the zip.)

Drag and drop your card onto the .bat or exe file.

Works with multiple images.

---

Requires Pillow to run the bare script:

pip install --upgrade Pillow

---

You can change the New File vs Overwrite behaviour with the overwrite_cards variable at the top of the script. It should be obvious as to what to do.

---

To compile yourself, install Python 3, then do the following in a console:

pip install pyinstaller

pyinstaller -F -w -c _CleanMSECards.py