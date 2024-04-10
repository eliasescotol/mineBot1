from openpyxl import load_workbook
from openpyxl.styles import Font
from parameters import parameters
from is_number import is_number
from imageToPDF import add_image_to_pdf
from heicTojpg import convert_heic_to_jpg
from deleteFiles import delete
from PDF_merge import PDFMerge
from compressImage import compress_jpeg
from datechange import convert_date_format


# string to search in file
delete('PDF')
delete('JPEG')
delete('JPG')
valueTracker = []
descriptionLine = 0
pictures = []

input('Please Input Your Notes And Pictures')

workbook = load_workbook(filename="Excel/Reports/2023.12.15_Swing.xlsx")
daily = workbook["DAILY"]

for word in parameters:
    with open(r'note/note1.txt', 'r', encoding='windows-1252') as fp:
        # read all lines in a list
        lines = fp.readlines()
        lineNumber = 0
        description_add = ""
        for line in lines:
            lineNumber = 1 + lineNumber
            if line.find("Description") != -1:
                descriptionLine = lineNumber
            if descriptionLine == lineNumber:
                descriptionLine = lineNumber + 1
                if line.find('@') != -1:
                    descriptionLine = 0
                    parameters[40]['value'] = description_add
                else:
                    if line.find("Description") != -1:
                        continue
                    else:
                        description_add = description_add + str(line)
            if line.find('Image') != -1:
                value = line.replace("\n", "")
                pictures.append(str(value))


            # check if string present on a current line
            elif line.find(word['type']) != -1:
                value = line.split(':', 1)[1]
                value = value.replace(" ", "").replace("\n", "")
                if is_number(value):
                    conv = int(value)
                    word['value'] = conv
                else:
                    word['value'] = value
                break

for items in parameters:
    insertValue = daily[items['location']]
    insertValue.value = items['value']


workbook.save('PDF/1.xlsx')

thisIsaBreak = input("Fix Your Excel File Before Continuing. Input Any Word To CONTINUE: ")

convert_heic_to_jpg()
compress_jpeg(40)
print(pictures)
add_image_to_pdf(pictures)
finalFileName = parameters[1]["value"]
finalFileName = finalFileName.replace("/", ".")
finalFileName= str(convert_date_format(finalFileName))
PDFMerge(finalFileName+'_Swing')




print(parameters)
print(lineNumber)
