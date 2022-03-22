#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Just definitions here. Code starts in bottom block with argparse

def run(n):
    if n < 10:
        n = 10
    print("Running with n = %d" % n)
    import pandas as pd

    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    # generate dataset
    X, y = make_classification(n_samples=n, n_features=2, n_redundant=0,
        n_clusters_per_class=1, weights=[0.31], flip_y=0, random_state=2)

    ## correlation
    df = (pd.DataFrame(X))
    df = df.join(pd.Series(y, name="y"))
    print(df.corr())

    ## Unmodified CatboostClassifier as ML stress-test
    lm = LogisticRegression()
    result = lm.fit(X,y)
    print("LM Score: ", result.score(X,y))

def cleanup():
    print("TODO")

## Actual starting point of the code

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="Select the operation mode. Select `run` to run a load test and `cleanup` to perform a cleanup of all created helper- and meta-data", choices=['run', 'cleanup'])

opt_group = parser.add_mutually_exclusive_group()
opt_group.add_argument("-n", type=int, help="Specify an amout of dummy data to be populated into the dataframe for the load test")
opt_group.add_argument("-u", type=str, help="Specify a url to load dataframe from for the load test")

args = parser.parse_args()

if args.mode == 'run':
    print(f"Doing run")
    if args.n != None and args.n != '':
        print("Amount detected: %d" % args.n)
        run(args.n)
    elif args.u != None and args.u != '':
        print("Fetching url: %s" % args.u)
        print("TODO")
        # fetch ur
    else:
        print("Please supply -n or -u argument")
elif args.mode == 'cleanup':
    print(f"Doing cleanup")
    cleanup()
else:
    print(f"Error: Unknown mode {args.mode}\n")
    parser.print_help()



