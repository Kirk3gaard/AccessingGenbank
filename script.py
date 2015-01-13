# -*- coding: utf-8 -*-
"""
Created on Tue Jan 06 11:43:12 2015

@author: RasmusHKirkegaard
Downloads all the genbank files based on a file listing genbank IDs
Parses all the files and extracts the source locations
Creates a list with the unique source locations
"""

filewgenbankids = "ACCESSION_IDs.txt"
outputfilelocation=""


from fetch_genbank_function import fetch_genbankfile
fetch_genbankfile(filewgenbankids, outputfilelocation)

from parse_genbank_function import parse_genbank_function
parse_genbank_function(filelist=filewgenbankids,field="isolation_source",outputfile='source_list.txt')
