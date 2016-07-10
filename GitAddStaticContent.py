import git

"""
This script adds the newly-generated static content to the gh-pages branch
of the asmodeus repository.

NOTE:
Various other scripts will do the hard work of creating new content for the blog
(both creating new markdown files, and turning those markdown files into HTML content.)

NOTE:
It may be possible/desirable to modify the StaticContent.py static content
generation script so that instead of just creating the static content 
in the output/ directory, it actually checks out the latest gh-pages branch
into output/, and then regenerates the static content to be put into output/ 
and into the gh-pages branch.

"""



# Figure out where the new static content lives 
pelican_dir = '/Volumes/noospace/Users/charles/codes/asmodeus/pelican/'
static_dir = pelican_dir + 'output/'

# Need to verify that output/ is also the gh-pages branch
# 

# Now we are going to commit whatever changes are in the output/ directory
# NOTE:
# This should also check out a copy of gh-pages into output/ directory 
# (if we are running the real thing, for real)


