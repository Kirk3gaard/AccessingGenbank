This is a collection of small python functions that I have used to automatically

- download Genbank files based on a list with Genbank IDs
- subsequently extract information from the files based on the fields such as "source location"

The functions are dervied from a number of Stackexchange posts that I have been looking through to solve this task.
I have tested the functionality in the Anaconda environment on a Windows PC (http://continuum.io/downloads)



The script:
filewgenbankids = "ACCESSION_IDs.txt"
outputfilelocation=""

# Import function
from fetch_genbank_function import fetch_genbankfile
fetch_genbankfile(filewgenbankids, outputfilelocation)

# Import function
from parse_genbank_function import parse_genbank_function
parse_genbank_function(filelist=filewgenbankids,field=field_to_extract,outputfile='source_list.txt')