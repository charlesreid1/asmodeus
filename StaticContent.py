from BlogPostMaker import make_a_blog_post
from ContentGeneration import prefix
import subprocess 

def pelican_static_content():
    """
    This method runs the "pelican content" command
    to generate the new static site content

    NOTE:
    This script should also, if it is updated to work nicely,
    clone a copy of the gh-pages branch into the output/ directory 
    (if we are running the real thing, for real)
    """

    print prefix

    my_dir = prefix+'/pelican/'
    subprocess.call(['pelican','-D','content/'], cwd=my_dir)

    return 0

if __name__=="__main__":
    pelican_static_content()
    print "Done"

