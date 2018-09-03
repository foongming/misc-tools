#!/usr/bin/python
import csv
import hashlib
import argparse
the_args = argparse.ArgumentParser()
the_args.add_argument("-i", "--input_file",
  help="input file",
  type=str,
)
the_args.add_argument("-o", "--output_file",
  help="output file",
  type=str,
)
args = the_args.parse_args()
with open(args.input_file, "rb") as csvfile:
    with open(args.output_file, "w+") as out:
        data_in = csv.reader(csvfile)
        data_out = csv.writer(out, delimiter=',',
                quotechar='|',
                quoting=csv.QUOTE_MINIMAL,
                lineterminator='\n')
        for row in data_in:
            row[0] = hashlib.sha224(row[0]).hexdigest()
            data_out.writerow(row)
