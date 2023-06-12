"""
Print each persons name and twitter handle, using groups, should look like:
==============
Full Name / Twitter
==============
Derek Hawkins / @derekhawkins

Erik Sven-Osterberg / @sverik

Ryan Butz / @ryanbutz

Example Exampleson / @example

Ripal Pael / @ripalp

Darth Vader / @darthvader
"""
import re

def name_handles():
    with open("names.txt") as f:
        data = f.readlines()
        name_pattern = re.compile("([A-Z][A-z]+), ([A-Z][A-z]+)")
        twitter_pattern = re.compile(r"\B([@][A-z]+)")

        for name in data:
            match_name = name_pattern.search(name)   
            match_twitter = twitter_pattern.search(name)

            if match_name and match_twitter:
                print(f"{match_name.group(2)} {match_name.group(1)} / {match_twitter.group(1)}")  

name_handles()