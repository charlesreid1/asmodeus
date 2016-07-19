from ContentGeneration import prefix
import subprocess 

"""
This script will update the master branch with any newly-created markdown files corresponding to new blog posts. 
which are the raw material out of which the full Pelican site is generated. 

NOTE:
Various other scripts will do the hard work of creating new content for the blog
(both creating new markdown files, and turning those markdown files into HTML content.)

"""

def git_add_static_content():
    """
    Add fresh static content
    to the gh-pages branch
    """

    # Asmodeus on github
    gh = 'https://github.com/charlesreid1/asmodeus'
    
    # Path to asmodeus pelican directory:
    pelican_dir = '/Volumes/noospace/Users/charles/codes/asmodeus/pelican/'

    # Path to Pelican static countent output directory:
    static_dir = pelican_dir + 'output/'

    # cd output 
    # git add *
    # git commit -a -m 'new static content, update XYZ'
    # git push origin gh-pages

    ### # Use as template:
    ### print prefix
    ### my_dir = prefix+'/pelican/'
    ### subprocess.call(['pelican','-D','content/'], cwd=my_dir)

