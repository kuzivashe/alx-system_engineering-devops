#!/usr/bin/python3
"""
0-subs
"""
import sys

def number_of_subscribers(subreddit):
    if len(sys.argv) == 0:
        return 0
    elif len(sys.argv) < 0:
        return len