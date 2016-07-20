'''
Driver.py

'''

def make_another_blog_post():
    """
    Function to make another blog post and stop there
        +--> calls BlogPostMaker.py
            +--> calls ContentGeneration.py
    """
    from BlogPostMaker import make_a_blog_post
    return make_a_blog_post()

def make_static_content():
    """
    Function to make more static content
        +--> calls StaticContent.py
            +--> calls BlogPostMaker.py
                +--> calls ContentGeneration.py
    """
    from StaticContent import pelican_static_content
    return pelican_static_content()

def program1():
    print make_another_blog_post()
    print make_another_blog_post()
    print make_another_blog_post()
    print make_static_content()





def git_add():
    """
    Function to add new content to git 
    """
    from GitAddBlogPosts import git_add_static_content
    git_add_static_content(publish=False,superclean=False)


def git_add_yesterday():
    """
    Function to add content to git using a time machine
    """
    from GitAddBlogPostsYesterday import git_add_static_content_yesterday
    from datetime import datetime


    # ~~~~~~~~********~~~~~~~~~@@@@@@@~~~~~~~~~~~
    # @@@@@@@@@@@@ ~~~~~~~~~~~ ######### ********
    # ################ ~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~ Step into the time machine @@@@@ ~~~~~
    #
    yrsago = datetime.strptime("2013-06-30 02:22:31","%Y-%m-%d %H:%M:%S")
    #
    # @@@@@@@@@@@@ ~~~~~~~~~~~ ######### ********
    # ~~~~~~~~~~~~~~ ****************** ~~~~~~~~~
    # ~~~~~~~~ ****************** ~~~~~~~~~~~~~~~

    make_another_blog_post()
    make_static_content()
    git_add_static_content_yesterday(when=yrsago, publish=True, superclean=False)


if __name__=="__main__":
    git_add_yesterday()

