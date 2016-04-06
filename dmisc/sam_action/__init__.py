import re
import numpy as np

def cigarToSeq(cigar):
    """
    Input a cigar string (eg. 1S16M5I10M4S)
    output a line: SMMMMMMMMMMMMMMMMIIIIIMMMMMMMMMMSSSS
    """
    cigarNum = np.array(re.findall('[0-9]+',cigar),dtype='int64')
    cigarStr = np.array(re.findall('[A-Z]',cigar),dtype='string')
    usable = np.in1d(cigarStr,np.array(['S','M','I'],dtype='string'))
    cigarStr = cigarStr[usable]
    cigarNum = cigarNum[usable]
    cigarSeq = ''
    for s, n in zip(cigarStr, cigarNum):
        cigarSeq += int(n)*str(s)
    return cigarSeq

def MDToSeq(mdtag):
    """
    input mdTag: 31^CA31
    output: -------------------------------DDD-------------------------------

    input mdTag: 8G11^TG14T0T28T3
    output: --------G-----------DD--------------TT----------------------------T---
    """
    mdNum = np.array(re.findall('[0-9]+',mdtag),dtype='int64')
    mdStr = np.array(re.split('[0-9]+',mdtag),dtype='string')[1:]
    mdSeq = ''
    for s, n in zip(mdStr,mdNum):
        string = n * '-' + (len(s)-1) * 'D' if '^' in s else n * '-' + s
        mdSeq += string
    return mdSeq
