# pdf-tools
Tools to quickly modify PDF files  
![Screenshot of scripts in send to folder](https://i.imgur.com/8jI0F7X.png)

## How to Use
### Installing to the SendTo Menu

1. Download & open the .zip from the latest release

2. Open a file explorer window and type `Shell:SendTo` in the address bar (this will open the folder `C:\Users\[USERNAME]\AppData\Roaming\Microsoft\Windows\SendTo`)

3. Copy the scripts into the SendTo folder

4. Rename the shortcuts to what you would like them to show as in the SentTo Menu. I like to prefix the shortcut names with an underscore so they appear at the top (For example `_MergePDF`)

5. Bingo. Try it out on some PDFs by right clicking and choosing Send To > MergePDF/SplitPDF

## Usage Notes
When using these MergePDF, bear in mind that no matter how you select the PDFs, **the PDF you right click will be FIRST PDF in the new merged PDF!**  
This just means you need to right click whichever PDF you would like to be ordered first.

## Compiling from Source
The Windows binaries are complied using the *auto-py-to-exe python library*. Install this first with `pip install auto-py-to-exe`, then run `auto-py-to-exe` and point to one of the scripts. Make sure the 'One File' option is selected, then hit convert.
