'''
Driver.py

Function to make more static content
    +--> calls StaticContent.py
        +--> calls BlogPostMaker.py
            +--> calls ContentGeneration.py
'''

def make_another_blog_post():
    from BlogPostMaker import make_a_blog_post
    return make_a_blog_post()

def make_static_content():
    from StaticContent import pelican_static_content
    return pelican_static_content()




if __name__=="__main__":
    print make_another_blog_post()
    print make_another_blog_post()
    print make_another_blog_post()
    print make_static_content()

