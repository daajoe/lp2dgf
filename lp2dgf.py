#!/usr/bin/env python
#
# Copyright 2015
# Johannes K. Fichte, Vienna University of Technology, Austria
#
# lp2htd.py is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.  lp2htd.py is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.  You
# should have received a copy of the GNU General Public License along
# with lp2htd.py.  If not, see <http://www.gnu.org/licenses/>.
#
from os import path as os_path
import logging
import logging.config
logging.config.fileConfig('%s/logging.conf'%os_path.dirname(os_path.realpath(__file__)))

from graph import Graph
from ioutils import *
import optparse
from os import path as os_path
import select
import sys

def options():
    usage  = "usage: %prog [options] [files]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-o", "--output", dest="out", type="string", help="Output file", default=None)
    opts, files = parser.parse_args(sys.argv[1:])
    if len(files)>1:
        logging.critical('Supports at most one input file.')
        exit(1)
    return opts, files[0]

def write_dimacs(G,filename,output):    
    output.write('c original_input_file:%s\n' %filename)
    output.write('p edges %i %i\n' %(G.num_edges(),G.num_vertices()))
    for x,y in G:
        output.write('e %s %s\n' %(x,y))
    output.flush()


def parse_and_run(filename,output):
    G=Graph()
    with zopen(filename) as f:
        for line in f:
            if line.startswith('edge'):
                s=line[5:-3].split(',')
                if len(s)>2:
                    continue
                G.add_edge(s[0],s[1])
    write_dimacs(G,filename,output)

if __name__ == '__main__':
    opts,filename=options()
    with selective_output(opts.out) as s:
        parse_and_run(filename=filename,output=s)
    exit(0)
