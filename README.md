# pdf-tools
Tools to quickly modify PDF files

## Dependencies
To use these tools, you must have Python installed as well as the PyPDF2 package (which can be installed by running `pip install PyPDF2`)

## How to Use

There are two ways to use these scripts; the second being the easiest to use once set up, but harder to set up to begin with:

### Drag and Drop
Drag and drop PDFs straight onto Script to run

### Adding to the SendTo Menu

1. Extract the scripts to a permanant folder (that is one where they won't be moved etc.)

2. Create Merge.bat with following contents:

        ::MergePDF.py
        @echo off
        cls
        python "..\MergePDF.py" %*

3. Repeat for Split.bat:

        ::SplitPDF.py
        @echo off
        cls
        python "..\SplitPDF.py" %*

4. Select both .bat files, Right click one of them and choose 'Create Shortcut'

5. Rename the shortcuts to what you would like them to show as in the SentTo Menu.  
I normally prefix the name with an underscore so they appear at the top (For example `_MergePDF`)

6. Move the shortcuts to `C:\Users\[USERNAME]\AppData\Roaming\Microsoft\Windows\SendTo`.  
You can also open the start menu or run and type `Shell:SendTo`

7. Bingo. Try it out on some PDFs.

## Usage Notes
When using these MergePDF, bear in mind that no matter how you select the PDFs, **the PDF you right click will be FIRST PDF in the new merged PDF!**  
This just means you need to right click whichever PDF you would like to be ordered first.