from ContentGeneration import prefix
import subprocess 

"""
Given a date and time, 
create a git commit with that particular 
date and time. 

Do not push (publish), by default.
"""

def git_add_static_content_yesterday(when=datetime.now(),publish=False):
    """
    Add stale static content to the gh-pages branch

    Given a datetime object (when),
    create some git commits at that time
    using libfaketime.
    If you're confident it worked great,
    you can publish it (push it to Github).
    
    Be careful! 
    We haven't worked out how to undo commits.
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


