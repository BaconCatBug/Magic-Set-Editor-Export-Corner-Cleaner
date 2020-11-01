# You need these installed to run the bare script
# pip install --upgrade Pillow
from PIL import Image
from os import system
from sys import argv
from pathlib import Path

if len(argv)<2:
    print("*************************************************************************\n"
          "***Don't run this on it's own. Drag images onto the batch file or exe.***\n"
          "*************************************************************************")
    system("pause")
    exit(0)
# overwrite_cards = True
overwrite_cards = False

coords = ([0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],
          [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
          [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
          [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
          [4, 0], [4, 1], [4, 2], [4, 3],
          [5, 0], [5, 1], [5, 2],
          [6, 0], [6, 1],
          [7, 0], [7, 1],
          [8, 0],
          [9, 0])
# Gets the files dragged
filteredFileList = []
for elem in argv[1:]:
    filteredFileList.append(elem)
# Runs the conversion for each png file.
for e_FilteredFilename in filteredFileList:
    try:
        print("*****")
        print("Cleaning "+ str(Path(e_FilteredFilename).stem))
        img = Image.open(e_FilteredFilename)
        img = img.convert("RGBA")
        pixdata = img.load()
        width, height = img.size
        borderColour = pixdata[13, 13]
        if width == 752:
            temp1 = list(range(0, 17))
            temp2 = list(range(width // 2 - 17, width // 2 + 17))
            temp3 = list(range(width - 17, width))
            cornerXRange = temp1 + temp2 + temp3
        else:
            temp1 = list(range(0, 17))
            temp2 = list(range(width - 17, width))
            cornerXRange = temp1 + temp2

        for x in cornerXRange:
            for y in range(0, 17):
                pixdata[x, y] = borderColour

        borderColour = pixdata[13, height - 14]
        for x in cornerXRange:
            for y in range(0, 17):
                pixdata[x, height - 1 - y] = borderColour

        for e_Replace in range(0, len(coords)):
            pixdata[coords[e_Replace][0], coords[e_Replace][1]] = (0, 0, 0, 0)
            pixdata[width - 1 - coords[e_Replace][0], coords[e_Replace][1]] = (0, 0, 0, 0)
            pixdata[coords[e_Replace][0], height - 1 - coords[e_Replace][1]] = (0, 0, 0, 0)
            pixdata[width - 1 - coords[e_Replace][0], height - 1 - coords[e_Replace][1]] = (0, 0, 0, 0)

        if width == 752:
            DFCOffset = 375
            for e_Replace in range(0, len(coords)):
                pixdata[coords[e_Replace][0] + DFCOffset, coords[e_Replace][1]] = (0, 0, 0, 0)
                pixdata[width - 1 - coords[e_Replace][0] - DFCOffset, coords[e_Replace][1]] = (0, 0, 0, 0)
                pixdata[coords[e_Replace][0] + DFCOffset, height - 1 - coords[e_Replace][1]] = (0, 0, 0, 0)
                pixdata[width - 1 - coords[e_Replace][0] - DFCOffset, height - 1 - coords[e_Replace][1]] = (0, 0, 0, 0)

            for e_MiddleX in range(375, 377):
                for e_middleY in range(0, height - 1):
                    pixdata[e_MiddleX, e_middleY] = (0, 0, 0, 0)
        # Outputs the converted image file.
        if overwrite_cards == False:
            img.save(str(Path(e_FilteredFilename).stem) + ".Cleaned.png", "PNG")
        else:
            img.save(Path(e_FilteredFilename), "PNG")
    except Exception as e:
        print(e)
