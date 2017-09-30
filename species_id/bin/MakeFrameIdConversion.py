#!/usr/bin/python
'''The frame ids were originally just sequential based on how the frames were spit out of the extraction process, which is 1Hz. This is a problem when we want to execute on time based analysis, it is hard to match up the frames. To fix this, we changed the frame ids to refer to the frame number in the video. This script creates a file that does the conversion of the form:

<oldFrameId>,<newFrameId>

It is generated by looking at the symlinks of the old frame ids and see where they point.'''
usage='MakeFrameIdConversion <oldFrameDir> <outputFile>'

import os
import os.path
from optparse import OptionParser
import re

if __name__ == '__main__':
  parser = OptionParser(usage=usage)

  parser.add_option('--frame_regex',
                    default='(([0-9][0-9]-){3}[0-9]+)\.',
                    help='Regex to extract the frame id from filenames')

  (options, args) = parser.parse_args()

  frameRe = re.compile(options.frame_regex)

  oldFrameDir = args[0]

  # Open the file for output
  outStream = open(args[1], 'w')

  # Step through all the files in the directory
  for f in sorted(os.listdir(oldFrameDir)):
    frameSearch = frameRe.search(f)
    if frameSearch:
      oldFrameId = frameSearch.groups()[0]

      newFrameFile = os.path.realpath(os.path.join(oldFrameDir, f))
      newFrameId = frameRe.search(newFrameFile).groups()[0]

      outStream.write('%s,%s\n' % (oldFrameId, newFrameId))
  