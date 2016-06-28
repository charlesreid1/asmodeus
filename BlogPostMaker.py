from ContentGeneration import generate_content, prefix
from datetime import datetime

def make_a_blog_post():
    """
    This method is simple, but it could use some more options.
    - Title
    - Date
    - Categories
    - Location of blog file
    """
    # Blog file
    blog_file = prefix+"/pelican/content/blogpost.md"

    # Header
    my_title = "Dino Ipsum"
    my_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    my_cat = "Dinosaurs"

    # Blog
    blog_title = "Title: %s"%(my_title)
    blog_date  = "Date: %s"%(my_date)
    blog_cat   = "Category: %s"%(my_cat)
    blog_body = generate_content()

    # Make the blog post file
    with open(blog_file,'w') as f:
        f.write(blog_title + "\n")
        f.write(blog_date + "\n")
        f.write(blog_cat + "\n\n")
        f.write(blog_body + "\n")

    return blog_file

if __name__=="__main__":
    print make_a_blog_post()
