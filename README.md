THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

THIS SOFTWARE ALSO HAS NO LICENCE BECAUSE COME ON IT'S A FEW LINE OF PYTHON SCRAPED TOGETHER IN A SLEEP DEPRIVED HAZE I DO NOT CARE IF YOU WANT TO REUSE IT IF YOU HONESTLY NEED TO "STEAL" THIS CODE YOU HAVE BIGGER PROBLEMS PERHAPS YOU SHOULD GET A DOG OR A GOLDFISH OR PERHAPS TAKE THAT CRUISE YOU HAVE ALWAYS WANTED.

---

This has been tested with Cajun's Templates, including DFC, (https://github.com/CajunAvenger/Cajun-Style-Templates), the stock MSE templates, and MTG.Design cards.

--- 

USAGE:

Download either the .py file and .bat file, or download one of the precompiled exe files.

(Click the green "Code" button and download the zip.)

Drag and drop your card(s) onto the .bat or exe file.

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