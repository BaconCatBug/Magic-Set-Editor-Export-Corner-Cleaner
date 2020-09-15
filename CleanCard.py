from PIL import Image
import glob
from pymsgbox import confirm

decision = \
    confirm(
        text='This will now clean up the corners of all png images in the folder this script was run from.\n\n'
             'This will create new copies and not alter the original images.\n\n'
             'Do you wish to proceed?',
        title='BaconCatBug\'s Card Image Corner Cleaner',
        buttons=['Yes, make my cards sexy!', 'No, I am scared of transparent pixels!']
    )

if decision is 'Yes, make my cards sexy!':
    rawFileList = glob.glob('*.png')
    filteredFileList = []
    for e_RawFileList in rawFileList:
        if 'Cleaned' not in e_RawFileList:
            filteredFileList.append(e_RawFileList)

    for e_FilteredFilename in filteredFileList:
        img = Image.open(e_FilteredFilename)
        img = img.convert("RGBA")
        pixdata = img.load()
        coords = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],
                  [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
                  [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
                  [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                  [4, 0], [4, 1], [4, 2], [4, 3],
                  [5, 0], [5, 1], [5, 2],
                  [6, 0], [6, 1],
                  [7, 0], [7, 1],
                  [8, 0],
                  [9, 0]]

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

        filename = e_FilteredFilename.split('.')
        img.save(filename[0] + "_Cleaned." + filename[1], "PNG")
else:
    exit(1)
