from bz2 import BZ2File
import contextlib
from detect_compression import file_type
import sys

@contextlib.contextmanager
def zopen(filename=None):
    ftype = file_type(filename)
    if ftype == 'bz2':
        fh = BZ2File(filename)
    elif ftype == None:
        fh = open(filename)
    else:
        raise TypeError('File type "%s" not supported' %ftype)
    try:
        yield fh
    finally:
        if fh:
            fh.close()


@contextlib.contextmanager
def selective_output(filename=None):
    if filename and filename != '-':
        fh = open(filename, 'w')
    else:
        fh = sys.stdout
    try:
        yield fh
    finally:
        if fh:
            fh.close()
