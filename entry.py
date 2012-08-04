#!/usr/bin/python2

# entry.py -- entry class
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2012-07-24.
# @Revision:    0.1

def parse_str(self, entry_str):
    """parse entry string"""
    pass


class entry:
    def __init__(self, entry_str):
        """constructor"""
        self.msg = ""
        self.starttime = ""
        self.duration = ""

        msg, starttime, duration = self.parse_str(entry_str)

        
    
        
        
        
