# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 09:44:04 2014

@author: RasmusHKirkegaard
20150106 Working fine now
"""

def fetch_genbankfile(filewgenbankids='ACCESSIONids.txt', output_location=""):
    """
    Given a file with a list of genbank ids and an outputlocation, downloads all the genbank files and saves them
    """
    import urllib2
    import os
    import sys
    import time
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
    
        open(gbk_out_file, "w").write(urllib2.urlopen(url_template % id).read())
        print "Done"
        time.sleep(1.0/3) # It is not allowed to request more than 3 times pr second!!!