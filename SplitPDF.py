from PyPDF2 import PdfFileWriter, PdfFileReader
from time import sleep
import sys
import os
import datetime

# Take a dropped file as an input


def checkInput():
	if len(sys.argv) < 2:
		print("NO PAGES")
		inputfile = input("Drag PDF into this window and press ENTER >")
		inputfile = os.path(inputfile)
		print(inputfile)


checkInput()

# Take a dropped file as an input and set variables
inputfile = sys.argv[1]
workingDir = os.path.dirname(inputfile)
fileName = os.path.basename(str(os.path.splitext(inputfile)[0]))

try:
	# Load and initialize
	inputpdf = open(inputfile, "rb")
	pdfReader = PdfFileReader(inputpdf)

	# Show the pdf path and amount of pages in pdf
	print("Input File:", inputfile)
	print("Has", pdfReader.numPages, "pages\n")

	#Split at every page
	n = 1
	for i in range(pdfReader.numPages):

		# Clear & initate PDF writer, then add a page to the buffer
		output = PdfFileWriter()
		output.addPage(pdfReader.getPage(i))

		# Check and set output name to next available following below format
		while True:
			if (os.path.exists(os.path.join(workingDir,fileName + "_p%s.pdf" % (n)))):
				n += 1
			else:
				break

		# Set output name and write the page to it's own pdf
		outputFile = os.path.join(workingDir, fileName + "_p%s.pdf" % (n))
		with open(outputFile, "wb") as outputStream:
			output.write(outputStream)
		
		# Increase page count
		n += 1

	inputpdf.close()
	print("DONE")
	sleep(1)
except Exception as e:
	print(e)
	input("Press ENTER to continue")

# Remove the original file
try:
	os.remove(os.path.abspath(inputfile))
except Exception as e:
	print(e)
	input("Press ENTER to continue")
