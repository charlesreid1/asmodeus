# Asmodeus - Pelican Static Site Content 

This folder contains the source code for the Asmodeus web page generator. 

This page uses Pelican to generate static content. 

To install Pelican:

```
pip install Markdown
pip install pelican
```

## Action Scripts

We want to create action scripts that will allow us to automatically generate content, blog posts, etc. It's coming.

## Instructions: Modifying Site Contents

To create or modify site content, check out the `pelican/` directory of the `master` branch of the asmodeus Github repository.

This folder contains the content (homepage, author page, blog posts) used to generate the static site. 

To create a new blog post, you will add a file here.

## Instructions: Commit Toolchain

The commit toolchain is where you take any and all changes posted and you commit them to the repository, which turns them from "good idea" to "revolutionary"

(don't ask.)

Git automation - we are automating commits here. Don't lose sight of that fact: we are automating commits.

## Instructions: Automation and Trickery

The trickery is where we put scripts for Github trickery, committing particular things at particular times.

Time modification library. Patterns on the repo graph. Etc.





`-----------------------------8<--------------------------`


## Instructions: Updating Site

Once you have finished adding or modifying site contents, you will use Pelican to rebuild the site.

You will need to install the `coffin-spore-theme`, a custom pelican theme I wrote for these bots.

```
git clone https://github.com/charlesreid1/coffin-spore-theme
pelican-themes -i coffin-spore-theme
```

Now go to the `pelican/` directory in the Apollo Space Junk repository. 

When you run Pelican to generate site contents, it will put the static site into a directory called `output/`. 

If you check out a copy of the `gh-pages` brnach of Apollo Space Junk, and call it `output/`, it will check out 
a copy of the site's static content. If you then run Pelican to update the site's static content, it will 
update the content in-place, and you can update the static contents in Github directly from there.

In the pelicanconf.py file, you can use the SITEURL variable to set the site prefix. 

If you are building the site to test locally, use SITEURL = ''

Then go to the `output/` directory and run a simple HTTP server: `python -m SimpleHTTPServer 8080`

If you are building the site to deploy to Github Pages, use SITEURL = '/apollospacejunk'

Then go to the `output/` directory and update the gh-pages branch of the Apollo Space Junk repository.

