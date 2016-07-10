'''
Driver.py
    +--> calls StaticContent.py
        +--> calls BlogPostMaker.py
            +--> calls ContentGeneration.py
'''

from StaticContent import pelican_static_content 

pelican_static_content()
print "Done"

