This is a collection of small python functions that I have used to automatically

- download Genbank files based on a list with Genbank IDs
- subsequently extract information from the Genbank files based on the fields such as "source location"

The functions are dervied from a number of Stackexchange posts that I have been looking through to solve this task.
I have tested the functionality in the Anaconda environment on a Windows PC (http://continuum.io/downloads)

I have attached:
- a file for running the workflow "script.py"
- A function for downloading genbank files "fetch\_genbank\_function.py"
- A function for parsing genbank files "parse\_genbank\_function.py"
- an example file with genbank IDs "ACCESIOND_IDs.txt"


And running the script with these files in the working directory should result in the:
- an example of the output file "source_list.txt"
- a number of genbank files
