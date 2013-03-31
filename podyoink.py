#!/usr/bin/python
#
# podyoink.py
#
# Copyright (C) 2013 George Goldberg <george@grundleborg.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#

import feedparser
import urllib
import sys

# Set up some paths
PODCAST_URL = 'http://downloads.bbc.co.uk/podcasts/radio4/fricomedy/rss.xml'
DOWNLOADS_DIR = '/home/gberg/podcasts/'
DOWNLOADED_LIST_FILE = '/home/gberg/.podyoink/downloaded.list'

# Parse the Atom Feed
feed = feedparser.parse(PODCAST_URL)

# Read the downloaded files list
downloadedListFile = open(DOWNLOADED_LIST_FILE)
downloadedList = downloadedListFile.read().splitlines()
downloadedListFile.close()

# Loop over all the entries in the feed
for item in feed.entries:
    
    # Print out the entry found.
    print "Entry Found:", item.link

    # Get the file name of the podcast
    fileName = item.link.split('/')[-1]

    # Check if the file is already downloaded
    if fileName in downloadedList:
        # Go to next file.
        print "Not a new file. Skipping..."
        continue

    # File is not already downloaded
    print "New File. Downloading..."

    # Actually download the file
    urllib.urlretrieve(item.link, DOWNLOADS_DIR + fileName)

    # Add the file to the list of done ones
    listFile = open(DOWNLOADED_LIST_FILE, 'a')
    listFile.write(fileName)
    listFile.write("\n")
    listFile.close()

print "Done"


