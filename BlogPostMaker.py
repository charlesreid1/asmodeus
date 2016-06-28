from ContentGeneration import generate_content 
from datetime import datetime

def make_a_blog_post():

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
    with open('blogpost.md','w') as f:
        f.write(blog_title + "\n")
        f.write(blog_date + "\n")
        f.write(blog_cat + "\n\n")
        f.write(blog_body + "\n")

if __name__=="__main__":
    make_a_blog_post()

