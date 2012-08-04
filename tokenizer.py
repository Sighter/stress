#!/usr/bin/python3

# tokenizer.py -- the tokenizer
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2012-07-29.
# @Revision:    0.1

TIME_UNITS = ["min", "minutes", "minute", "h", "hours", "hour"]
SEPERATORS = [" ", ","]


class tokenizer:
    def __init__(self, string):
        self.string = string
        self.cur_idx = 0

    def reset(self):
        self.cur_idx = 0

    def _get_next_char(self):
        if self.cur_idx < len(self.string):
            n = self.string[self.cur_idx]
            self.cur_idx += 1
            return n
        else:
            return None

    def _reveal_next_char(self):
        if self.cur_idx < len(self.string):
            n = self.string[self.cur_idx]
            return n
        else:
            return None

    def _read_number(self):
        value = ""
        while self._reveal_next_char() != None \
              and self._reveal_next_char().isdigit():
            value += self._get_next_char()
        return int(value)

    def _get_next_word(self):
        word = ""
        while True:
            c = self._reveal_next_char()
            if c == None:
                break
            if c in SEPERATORS:
                break
            if c == ":":
                break
            
            word += self._get_next_char()

        return word


    def next_token(self):
        # check for seperators
        while self._reveal_next_char() in SEPERATORS:
           self._get_next_char()

        character = self._reveal_next_char()

        # end of stream
        if character == None:
            self.reset()
            return None

        if character.isdigit():
            return ("INTEGER", self._read_number())
        
        if character == ":":
            return ("TAG_MARKER", self._get_next_char())

        # handle all other
        word = self._get_next_word()
        
        if word in TIME_UNITS:
            return ("TIME_UNIT", word)

        return ("WORD", word)

    def get_token_list(self):
        self.reset()
        tlist = []
        t = self.next_token()
        while t != None:
            tlist.append(t)
            t = self.next_token()

        return tlist
            

