from ContentGeneration import prefix
from StaticContent import pelican_static_content
import subprocess 
from datetime import datetime

"""
Given a date and time, 
create a git commit with that particular 
date and time. 

Do not push (publish), by default.

"""

def git_add_static_content_yesterday(when=datetime.now(),publish=False,superclean=False):
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
    asmodeus = 'https://github.com/charlesreid1/asmodeus'
    pelican_dir = prefix + "/pelican/"
    output_dir  = prefix + "/pelican/output/"

    ### if superclean:

    ###     print "Clear output"
    ###     subprocess.call(['rm','-rf','output/'], cwd=pelican_dir)

    ###     print "Check output"
    ###     subprocess.call(['git','clone','-b','gh-pages',asmodeus,'output/'], cwd=pelican_dir)



    ### print "Use Github pelican configuration"
    ### subprocess.call(['cp','publish.pelicanconf.py','pelicanconf.py'], cwd=pelican_dir)

    ### print "Make stuff in output" 
    ### subprocess.call(['pelican','-D','content/'], cwd=pelican_dir)



    print "Add/commit stale stuff yesterday"

    dtstamp = datetime.strftime( when, "%Y-%m-%d %H:%M:%S")

    print "--> This git commit will use the following date and time: %s"%(dtstamp)

    ### # ------------------
    ### # tests:

    ### # first, compile the 'what time is it' program
    ### print "gcc faketime/what_time_is_it.cc -o whattime"
    ### subprocess.call(['gcc','./faketime/what_time_is_it.cc','-o','./whattime'],cwd=prefix)

    ### # use faketime to run the 'what time is it' program
    ### print "faketime '%s' ./whattime"%(dtstamp)
    ### subprocess.call(['faketime',dtstamp,'./whattime'],cwd=prefix)

    # ------------------
    # real time:

    # use faketime to run git add and git commit
    print "use faketime to run git add -A . and git commit -a -m 'i am a robot. beep boop.'"
    subprocess.call(['faketime',dtstamp,'git','add','-A','.'],cwd=output_dir)
    subprocess.call(['faketime',dtstamp,'git','commit','-a','-m','"this is an automated commit. beep boop."'],cwd=output_dir)

    print "Now publish"
    if publish is True:
        subprocess.call(['faketime','\''+dtstamp+'\'','git','push','origin','gh-pages'],cwd=output_dir)

    return 0

