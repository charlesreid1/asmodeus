from BlogPostMaker import make_a_blog_post, prefix
import subprocess 

def pelican_static_content():
    """
    This method runs the pelican content ocmmand
    to generate the new static site content
    """

    make_a_blog_post()

    print prefix

    my_dir = prefix+'/pelican/'
    subprocess.call(['pelican','-D','content/'], cwd=my_dir)

if __name__=="__main__":
    pelican_static_content()
    print "Done"

