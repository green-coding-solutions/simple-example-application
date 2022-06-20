#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "mode",
    help="Select the operation mode. Select `run` to run a load test and `cleanup` to perform a cleanup of all created helper- and meta-data",
    choices=['run', 'cleanup']
)

opt_group = parser.add_mutually_exclusive_group()
opt_group.add_argument("-n", type=int, help="Specify an amout of dummy data to be populated into the dataframe for the load test")

args = parser.parse_args()

if args.mode == 'run':
    print("Doing run")
    if args.n is not None and args.n != '':
        print("Amount detected: %d" % args.n)
        import hashlib
        dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', args.n)
    else:
        print("Please supply -n argument")
elif args.mode == 'cleanup':
    print("Doing cleanup")
    print("TODO")
else:
    print(f"Error: Unknown mode {args.mode}\n")
    parser.print_help()
