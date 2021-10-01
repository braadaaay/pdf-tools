from PyPDF2 import PdfFileWriter, PdfFileReader
from time import sleep
import sys
import os
import datetime

# Take a dropped file as an input and set variables
args = sys.argv
files = args[1::]
workingDir = os.path.dirname(files[0])

# First check that there was a file dropped
if(len(files) < 1):
	input("NO PDFs to Merge!")
	exit()
# Then print them
print(str(len(files)) + " files to merge:")

try:
	# Add all pages to a buffer
	output = PdfFileWriter()
	for file in files:
		#open(file, "rb")
		pdfReader = PdfFileReader(file)
		for page in range(pdfReader.numPages):
			output.addPage(pdfReader.getPage(page))

	# Check next available file name following below format
	n = 1
	while True:
		if (os.path.exists(os.path.join(workingDir,str(datetime.date.today())+"_"+str(n)+".pdf"))):
			n += 1
		else:
			break
	
	# Set output name and write page buffer to pdf file
	outputFile = os.path.join(workingDir,str(datetime.date.today())+"_"+str(n)+".pdf")
	with open(outputFile, "wb") as outputStream:
		output.write(outputStream)

	# Finished
	print("DONE")
except Exception as e:
	print(e)
	input("Press ENTER to continue")

# Remove the original file
try:
	for file in files:
		os.remove(os.path.abspath(file))
		sleep(1)
except Exception as e:
	print(e)
	input("Press ENTER to continue")