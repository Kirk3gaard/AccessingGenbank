# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 10:31:39 2014

@author: RasmusHKirkegaard
Parses genbank files and retrieves the unique values of a given field if available
"""

def parse_genbank_function(filelist='ACCESSIONids.txt',field="isolation_source",outputfile='output.txt'):
    """
    Given a file with a list of genbank IDs, a set of mathcing genbank files, a genbank field, and an output filename
    Parses the genbank files and returns a list of unique entries in the field
    """
    from Bio import SeqIO
    f1 = open(filelist, 'r')
    lines = f1.read().splitlines()
    field_list = []
    fail=0
    success=0
    for x in lines:
        gb_file = x+".gb"     
        for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank") :
            # Add to list
            try:
                field_list.append(gb_record.features[0].qualifiers[field][0])
                success=success+1
            except Exception:
                fail=fail+1
                pass
    # Make a list with unique field entries and print to file
    print("Number of files not having a \""+field+"\": "+str(fail)+"/"+str(success+fail))
    unique_field_list = list(set(field_list))
    print("Number of unique \""+field+"\": "+str(len(unique_field_list)))
    f = open(outputfile, 'w')
    for item in unique_field_list:
      f.write("%s\n" % item)
    f.close()
    f1.close()