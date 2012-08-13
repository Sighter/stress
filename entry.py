#!/usr/bin/python2

# entry.py -- entry class
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2012-07-24.
# @Revision:    0.1

import datetime

from tokenizer import tokenizer
from tokenizer import HOUR_UNITS
from tokenizer import MIN_UNITS

def parse_str(self, entry_str):
    """parse entry string"""
    pass


class entry:
    def __init__(self):
        """constructor"""
        self.msg = ""
        self.starttime = ""
        self.duration = ""

    def __str__(self):
        """debug print"""
        s =  "entry [\n"
        s += "  msg = " + str(self.msg) + "\n"
        s += "  tags = " + str(self.tags) + "\n"
        s += "  durations = " + str(self.duration) + "\n"
        s += "]"
        return s

        
class entry_parser:
    def __init__(self):
        """init the parser."""
        self.reset()

    def __str__(self):
        """debug print"""
        s =  "entry_parser [\n"
        s += "  msg = " + str(self.msg) + "\n"
        s += "  tags = " + str(self.tags) + "\n"
        s += "  durations = " + str(self.durations) + "\n"
        s += "]"
        return s

    def reset(self):
        """from outside callable reset method"""
        self.msg = []
        self.tags = []
        self.durations = []
        self.tm_count = 0

    def get_new_entry(self):
        """returns the constructed entry"""

    def parse_str(self, raw_string):
        """parse the given string and return a new entry instance"""
        self.tok = tokenizer(raw_string)

        # parse string and write the results in temp vars
        # read methods append the results n(to the coresponding vars
        while (True):
            
            t = self.tok.reveal_next_token()
            if t == None:
                break
            
            if t[0] == "INTEGER":
                con = self._read_time_duration()
                if con == True:
                    continue

            if t[0] != "INTEGER" and t[1].upper() in ["TAGS", "TAG", "T"]:
                con = self._read_tags()
                if con == True:
                    continue
                else:
                    self.tm_count += 1;

            # read msg
            self.msg.append(t[1])
            self.tok.consume_next_token()

            
        # build msg
        new_entry = entry()

        for word in self.msg:
            new_entry.msg += str(word) + " "

        new_entry.msg = new_entry.msg.strip()
            
        # build timedelta objects and sum them
        complete_duration = datetime.timedelta()

        for d in self.durations:
            if d[1] in HOUR_UNITS:
                cur_dur = datetime.timedelta(hours = d[0])
            elif d[1] in MIN_UNITS:
                cur_dur = datetime.timedelta(minutes = d[0])

            complete_duration += cur_dur

        new_entry.duration = complete_duration

        # build entry
        new_entry.tags = self.tags

        # reset the parser and return the new entry
        self.reset()

        return new_entry
        
    def _read_time_duration(self):
        """this method reads a time duration"""
        t1 = self.tok.reveal_next_token(1)

        if t1 != None and t1[0] == "TIME_UNIT":
            digit = self.tok.consume_next_token()[1]
            unit = self.tok.consume_next_token()[1]
            self.durations.append((digit, unit))

            return True
        else:
            return False

    def _read_tags(self):
        """this methods reads the tags till the end of the string"""
        t1 = self.tok.reveal_next_token(1)
        
        if t1 != None and t1[0] == "TAG_MARKER":
            self.tok.consume_next_token()
            self.tok.consume_next_token()
            token = self.tok.consume_next_token()
            
            while (token != None):
                self.tags.append(token[1])
                token = self.tok.consume_next_token()

            return True
        else:
            return False

