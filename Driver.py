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

def git_add():
    from GitAddBlogPosts import git_add_static_content
    git_add_static_content(publish=False)

def program1():
    print make_another_blog_post()
    print make_another_blog_post()
    print make_another_blog_post()
    print make_static_content()

if __name__=="__main__":
    git_add()

