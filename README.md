This is a collection of small python functions that I have used to automatically

- download Genbank files based on a list with Genbank IDs
- subsequently extract information from the Genbank files based on the fields such as "source location"

The functions are derived from a number of posts at http://stackexchange.com/  that I have been looking through to solve this task.
I have tested the functionality in the Anaconda environment on a Windows PC (http://continuum.io/downloads)

(Python 2.7.6 |Anaconda 1.9.2 (64-bit)| (default, Nov 11 2013, 10:49:15) [MSC v.1500 64 bit (AMD64)] on win32)

I have attached:
- A demo for running the workflow "script.py"
- A module with functions for downloading and parsing genbank files "Genbank_module.py"
- an example file with genbank IDs "ACCESIOND_IDs.txt"


Running the "script.py" with these files in the working directory should result in:
- an output file "source_list.txt"
- a number of genbank files
