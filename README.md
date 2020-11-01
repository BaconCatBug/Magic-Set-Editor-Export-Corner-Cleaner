Usage:

Download either the .py file and .bat file, or download one of the precompiled exe files.

(Click the green "Code" button and download the zip.)

Drag and drop your card onto the .bat or exe file.

Works with multiple images.

---
LIMITATIONS:

Due to the hard limit of 2047 character limit for the command prompt in windows, the .bat version will be limited to how many cards it can handle at once, dependent on the lengths of the full file paths of the cards you drag onto it. If the .bat isn't working with a large number of cards, reduce the number of cards you are dragging onto it.

The .exe version also has a limit to the number of cards you can drag at once, dependent on the lengths of the full file paths of the cards you drag onto it, but it is far higher that the .bat

I was able to do 300+ cards at one with the .exe version in a rather deep folder, while the .bat couldn't even handle 100. With a very short folder path (i.e. C:\New Folder) I was able to do 600+ cards with the .exe version.

---

Requires Pillow to run the bare script:

pip install --upgrade Pillow

---

You can change the New File vs Overwrite behaviour with the overwrite_cards variable at the top of the script. It should be obvious as to what to do.

---

To compile yourself, install Python 3, then do the following in a console:

pip install pyinstaller

pyinstaller -F -w -c _CleanMSECards.py