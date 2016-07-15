import subprocess

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

# Asmodeus on github
gh = 'https://github.com/charlesreid1/asmodeus'

# Path to asmodeus pelican directory:
pelican_dir = '/Volumes/noospace/Users/charles/codes/asmodeus/pelican/'

# Path to Pelican static countent output directory:
static_dir = pelican_dir + 'output/'

# rm -rf static_dir
# git clone -b gh-pages https://github.com/charlesreid1/asmodeus output
# # local testing
# cp pelicanconf.local.py pelicanconf.py 
# # big time
# cp pelicanconf.ghpages.py pelicanconf.py 
# pelican content
# cd output 
# git add *
# git commit -a -m 'automated update XYZ'
# git push origin gh-pages

