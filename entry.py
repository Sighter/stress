#!/usr/bin/python2

# entry.py -- entry class
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2012-07-24.
# @Revision:    0.1

from tokenizer import tokenizer

def parse_str(self, entry_str):
    """parse entry string"""
    pass


class entry:
    def __init__(self):
        """constructor"""
        self.msg = ""
        self.starttime = ""
        self.duration = ""


        
class entry_parser:
    def __init__(self):
        """init the parser."""
        self.reset()

    def reset(self):
        """from outside callable reset method"""
        self.msg = ""
        self.tags = []
        self.durations = []
        tm_count = 0


    def parse_str(self, raw_string):
        """parse the given string and return a new entry instance"""
        self.tok = tokenizer(raw_string)

        # parse string and write the results in temp vars
        # read methods append the results to the coresponding vars
        t = self.tok.reveal_next_token()
        while (t != None):
            
            if t[0] == "TIME_UNIT":
                self._read_time_duration()

            if t[0] == "TAG_MARKER" and self.tok.tag_marker_count == tm_count:
                self._read_tags()
                pass


            


        # build new entry
        
    def get_new_entry(self):
        """returns the constructed entry
