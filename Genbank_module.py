# -*- coding: utf-8 -*-
"""
@author: RasmusHKirkegaard
Module for automated interaction with genbank files
"""


def fetch_genbankfile(filewgenbankids='ACCESSIONids.txt',
                      output_location=""):
    """
    Downloads genbank files
    Given a file with a list of genbank ids and an outputlocation,
    downloads all the genbank files and saves them
    """
    import urllib2
    import os
    import sys
    import time
    import datetime as dt
    url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=gb&retmode=text"

    for id in open(filewgenbankids):
        id = id.strip()
        if id == "":
            continue

        sys.stdout.write("Fetching %s..." % id)
        sys.stdout.flush()
        gbk_out_file = os.path.join(output_location, id + ".gb")
        if os.path.exists(gbk_out_file):
            print "already fetched"
            sleeptime = 0
        else:
            timeatrequest = dt.datetime.now()
            try:
                open(gbk_out_file, "w").write(urllib2.urlopen(url_template % id).read())
                timeafterrequest = dt.datetime.now()
                timeused = (timeafterrequest-timeatrequest).total_seconds()
                sleeptime = max(0,1.0/3-timeused)  # Max 3 times pr second!!!
            except Exception:
                pass
        print "Done"
        time.sleep(sleeptime)


def parse_genbank_function(filelist='ACCESSIONids.txt',
                           field="isolation_source",
                           outputfile='output.txt'):
    """
    Parses genbank files
    Given
    a file with a list of genbank IDs,
    a set of mathcing genbank files,
    a genbank field, and
    an output filename
    Parses the genbank files and returns a list of unique entries in the field
    """
    from Bio import SeqIO
    f1 = open(filelist, 'r')
    lines = f1.read().splitlines()
    field_list = []
    fail = 0
    success = 0
    for x in lines:
        gb_file = x+".gb"
        for gb_record in SeqIO.parse(open(gb_file, "r"), "genbank"):
            # Add to list
            try:
                field_list.append(gb_record.features[0].qualifiers[field][0])
                success = success+1
            except Exception:
                fail = fail+1
                pass
    # Make a list with unique field entries and print to file
    print("Number of files not having a \"" +
          field+"\": "+str(fail) + "/" + str(success+fail))
    unique_field_list = list(set(field_list))
    print("Number of unique \"" + field + "\": " + str(len(unique_field_list)))
    f = open(outputfile, 'w')
    for item in unique_field_list:
        f.write("%s\n" % item)
    f.close()
    f1.close()


def fetch_extractgenbankIDfromfastafile(input_fasta='my.fasta',
                                        output_file="GBIDs.txt"):
    """
    Function for extracting genbank IDs from a fasta file
    assuming that the first 8 characters following the ">" sign is the
    Genbank ID
    """
    file1 = open(input_fasta, 'r')
    file2 = open(output_file, "w")
    for line in file1:
        if (line[0] == ">"):
            file2.write(line[1:9]+"\n")
    file1.close()
    file2.close()
