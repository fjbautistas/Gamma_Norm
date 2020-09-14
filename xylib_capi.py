#!/usr/bin/env python

"""
ctypes-based Python interface to C API of xylib
"""

from ctypes import cdll, c_char_p, c_double

xylib = cdll.LoadLibrary("libxy.so")

get_version = xylib.xylib_get_version
get_version.restype = c_char_p

load_file = xylib.xylib_load_file

get_block = xylib.xylib_get_block

count_columns = xylib.xylib_count_columns

count_rows = xylib.xylib_count_rows

get_data = xylib.xylib_get_data
get_data.restype = c_double

dataset_metadata = xylib.xylib_dataset_metadata
dataset_metadata.restype = c_char_p

block_metadata = xylib.xylib_block_metadata
block_metadata.restype = c_char_p

free_dataset = xylib.xylib_free_dataset

channal,energy,counts=[],[],[]

if __name__ == '__main__':
    import sys

    print("xylib version:", get_version())

    filename = (len(sys.argv) > 1 and sys.argv[1] or 'SMP00011.CNF')
    dataset = load_file(filename.encode(), None, None)
    if not dataset:
        
        print("File not found:", filename)
        sys.exit(1)
    block = get_block(dataset, 0)

    ncol = count_columns(block)
    print("number of columns:", ncol,end=' ')
    print("number of rows (-1 means it's a generator):",end=' ')
    for i in range(ncol):
        print(count_rows(block, i),end=' ')
    print("\n")

    print("data: ")
    #n = min(count_rows(block, 2),2048)
    n =count_rows(block, 1)
    for i in range(n):
        #b=(get_data(block, 0, i), get_data(block, 1, i),get_data(block, 2, i))
        #print("(%i, %g, %g) " % (get_data(block, 0, i), get_data(block, 1, i), get_data(block, 2, i)))
        print("(%i, %g) " % (get_data(block, 0, i), get_data(block, 1, i)))
        channal.append([get_data(block, 0, i)])
        #energy.append([get_data(block, 1, i)])
        counts.append([get_data(block, 1, i)])

    #spectra=[(channal),(energy),(counts)]
    print("...")
    print("Dataset metadata:", )
    print("measured at:", dataset_metadata(dataset, "MEASURE_DATE"))
    print("Block metadata:", )
    print("Description: ", block_metadata(block,b'description'))
    print("measured at: ", block_metadata(block,b'date and time'))
    print("real time: ", block_metadata(block,b'real time (s)'))
    print("live time", block_metadata(block,b'live time (s)'))
    print("energy cal: ",
          block_metadata(block,b'energy calib 0'),
          block_metadata(block,b'energy calib 1'),
          block_metadata(block,b'energy calib 2'))
    free_dataset(dataset)

