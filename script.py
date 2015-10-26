# -*- coding: utf-8 -*-
"""
@author: RasmusHKirkegaard
Downloads all the genbank files based on a file listing genbank IDs
Parses all the files and extracts the source locations
Creates a list with the unique source locations
"""

import Genbank_module as gb

filewgenbankids = "ACCESSION_IDs.txt"
outputfilelocation = ""

gb.fetch_genbankfile(filewgenbankids,
                     outputfilelocation)

gb.parse_genbank_function(filelist=filewgenbankids,
                          field="isolation_source",
                          outputfile='source_list.txt')
