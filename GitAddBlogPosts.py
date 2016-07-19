from ContentGeneration import prefix
from StaticContent import pelican_static_content
import subprocess 
from datetime import datetime

"""
This script will update the master branch with any newly-created markdown files corresponding to new blog posts. 
which are the raw material out of which the full Pelican site is generated. 

NOTE:
Various other scripts will do the hard work of creating new content for the blog
(both creating new markdown files, and turning those markdown files into HTML content.)

"""

def git_add_static_content(publish=False,superclean=False):
    """
    Add fresh static content
    to the gh-pages branch

    Don't bother with the date and time yet.
    """
    asmodeus = 'https://github.com/charlesreid1/asmodeus'
    pelican_dir = prefix + "/pelican/"
    output_dir  = prefix + "/pelican/output/"

    if superclean:

        print "Clear output"
        subprocess.call(['rm','-rf','output/'], cwd=pelican_dir)

        print "Check output"
        subprocess.call(['git','clone','-b','gh-pages',asmodeus,'output/'], cwd=pelican_dir)

    print "Use Github pelican configuration"
    subprocess.call(['cp','publish.pelicanconf.py','pelicanconf.py'], cwd=pelican_dir)

    print "Make stuff in output" 
    subprocess.call(['pelican','-D','content/'], cwd=pelican_dir)

    print "Add/commit new stuff"
    subprocess.call(['git','add','-A','.'],cwd=output_dir)
    subprocess.call(['git','commit','-a','-m','"this is an automated commit."'],cwd=output_dir)

    print "Now publish"
    if publish is True:
        subprocess.call(['git','push','origin','gh-pages'],cwd=output_dir)

    # cd pelican
    # rm -rf output
    # git clone -b gh-pages //asmodeus
    # pelican content
    # cd output
    # git add -a 
    # git commit 
    # git push

    return 0

