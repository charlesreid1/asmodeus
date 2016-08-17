# Asmodeus

**Table of Contents:**

[about](#about)

[TLDR: Up and Running](#tldr) 

[The Pelican Blog Site](#pelican) (DONE)

[The Static Content Generator Toolchain](#content) (DONE)

[The Commit Toolchain](#commit) (DONE)

[The Scheduling Toolchain](#scheduling) (IN PROGRESS)

[The Big McNasty](#bigmcnasty)





<hr />
<a name="about"></a>
## About 

This repository contians code for creating procedurally-generated content
(i.e., a Lorem Ipsum-like robot gibberish) and using it to populate information
on a page.






<hr />
<a name="tldr"></a>
## TLDR: Up and Running

Install Pelican. Install the atom-hammer-theme for Pelican. 

```
pip install Markdown
pip install pelican
git clone https://github.com/charlesreid1/atom-hammer-theme
pelican-themes -i atom-hammer-theme
```

Clone a copy of this repository (asmodeus).

```
git clone https://github.com/charlesreid1/asmodeus
cd asmodeus
```

Install NLTK and TextBlob. Install Olipy.

```
pip install TextBlob
pip install nltk
git clone http://github.com/leonardr/olipy
```

This project works by running a cascade of scripts that each do one thing and feed the result to the next. 
To make posts and regenerate Pelican static content, just run the driver:

```
python Driver.py
```






<hr />
<a name="pelican"></a>
## The Pelican Site (Done)

This bot will manage a website with Pelican, a static page generator for Python.

The pelican site uses the [Atom Hammer Pelican Theme](http://github.com/charlesreid1/atom-hammer-theme), 
a custom Pelican theme I created for this purpose.

### Tools Required

To install Pelican, use pip:

```
pip install Markdown
pip install pelican
```

To install the atom-hammer-theme for Pelican, get a copy:

```
git clone https://github.com/charlesreid1/atom-hammer-theme
pelican-themes -i atom-hammer-theme
```

### Directories and Files

`pelican/` - Files and Pelican configuration used to generate static content 

### Branches

`gh-pages` branch - contains the static content, which is served up by Github Pages.

[http://charlesreid1.github.io/asmodeus](http://charlesreid1.github.io/asmodeus) - webpage where the static content is served up.

### Instructions

To configure the Pelican page:
* Edit the file `pelican/pelicanconf.py`

To add content to the Pelican page:
* Put the content into a new markdown file with the proper headings.
* Put the markdown file into the `pelican/content/` directory.

To generate the static content for the site in order to test it locally:
* Go to the Pelican directory, `cd pelican/`
* Modify `pelican/pelicanconf.py` and set the `SITEURL` variable to be blank
* Generate static content with `pelican content`
* Start a local web server on port 8080 in the output directory, `cd output && python -m SimpleHTTPServer 8080`
* Test the static content by opening your browser and going to `localhost:8080`

To generate the static content for Github Pages:
* Go to the Pelican directory, `cd pelican/` 
* Modify `pelican/pelicanconf.py` and set the `SITEURL` variable to `asmodeus`
* Clone a copy of the `gh-pages` branch into an `output/` directory so that the static content will be generated directly into the `gh-pages` branch, `git clone -b gh-pages https://github.com/charlesreid1/asmodeus output/`
* Generate static content, `pelican content` (this will dump it into the `output/` directory)
* Update the static content in the `gh-pages` branch, `cd gh-pages && git add && git commit -m 'updating website' && git push origin gh-pages`






<hr />
<a name="content"></a>
## The Content Generation Toolchain (DONE)

The content generation toolchain covers the part of the process
where we procedurally generate text using Olipy.
That text is used to create new blog posts.
The new blog posts are used to generate new static content with pelican.

### Tools Required

This portion of the toolchain uses Olipy. 
Olipy is a set of Python scripts that depends on 
TextBlob and NLTK (Natural Language Toolkit), 
which are also Python packages.

To install dependencies:

```
pip install TextBlob
pip install nltk
```

To use Olipy, clone a copy of Olipy into the directory that you 
want to use it from: 

```
git clone http://github.com/leonardr/olipy
```

Example directory layout:

```
asmodeus
    ├── README.md
    ├── pelican/
    ├── olipy/
    ├── script_that_uses_olipy.py
```

The script that uses Olipy will import the Olipy module 
that it wants to use as follows: 

```
from olipy.queneau import WordAssembler
from olipy.data import load_json

assembler = WordAssembler(load_json("dinosaurs.json"))
```

See the `example.dinosaurs.py` file for an example of how this can be set up.

### Directories and Files

`ContentGeneration.py` - Procedurally generates content and feeds it to the blog post maker. 

`BlogPostMaker.py` - Takes the procedurally generated content and makes a blog post in the `pelican/` directory.

`StaticContent.py` - Regenerates static content for the Pelican blog site.

### Branches

`master` branch - nothing special here.






<hr />
<a name="commit"></a>
## The Commit Toolchain (DONE)

There are two scripts that show you how to take care of the commit toolchain:
* `GitAddBlogPosts.py` - demonstrates the use of Pelican and GitHub to 
    re-make static content using Pelican, then check the statically generated
    content into a GitHub repository.
* `GitAddBlogPostsYesterday.py` - demonstrates the linking of libfaketime with git
    to check content into a repository using a fake date and time. I used this
    to successfully create several commits at 2 in the morning on June 30 of 2013.

### Tools Required

Most of the tools used in this section are stock Python libraries, meaning no extra
software is required. (No git-python API, no language bindings, system-level calls only.)

The exception is the libfaketime library.

On Mac OS X, install libfaketime like this:

````
brew install libfaketime
```

On Linux, install libfaketime like this:

```
git clone https://github.com/wolfcw/libfaketime
cd libfaketime
make
```

### Directories and Files

* `GitAddBlogPosts.py` - adds content to gh-pages branch
* `GitAddBlogPostsYesterday.py` - adds content to gh-pages branch yesterday

Both scripts accomplish two basic tasks: 
* (Optionally,) check out a fresh copy of the gh-pages branch of the Asmodeus repository
* Make static content using the current version of the master branch
* Add the newly-generated static content to the gh-pages brnach

The `GitAddBlogPosts.py` file does both of these.

The `GitAddBlogPostsYesterday.py` file does both of these, but it does the second
(checking content into the GitHub repository) in a special way that obscures the
true date of the commit.



<hr />
<a name="scheduling"></a>
## The Scheduling Toolchain

Code for creating a commit schedule for libfaketime.

The commit schedule turns a 7-grid-high pixel drawing
into a sequence of commits that will draw it on the Github
commit graph.

Each repository will have its own set of commits, 
so if you screw up the drawing, or otherwise aren't happy with it,
just delete the repository.

### Tools

* Graph paper: 7 days of week = 7 pixels high. 52 weeks = 52 columns.
* Fancy date math - counting days starting from a known point, e.g., "last Saturday"

### Running

See [faketime/README.md](https://github.com/charlesreid1/asmodeus/blob/master/faketime/README.md) 
for more details on running a simple C program through libfaketime.

Basically, what we're doing is this:
* Turning a pixel drawing into a bunch of boxes
* Turning those boxes into a set of dates
* Feeding those dates to libfaketime 
* Generating a bunch of fake commits for each date 
* Committing them to a new Github repository via libfaketime

### Directories and Files

* `faketime/` - directory with a basic C program that prints the "current" date and time. 
    This is useful for testing libfaketime.

* `DRAWING.txt` - input file to CreateDatesList.py, the drawing/diagram/figure you want plastered on your github timeline.

* `CreateDatesList.py` - for a given drawing, generate a list of dates to fill in that drawing.

* `DATES.txt` - output file from CreateDatesList, list of dates required to draw your space invader or whatever.



<hr />
<a name="bigmcnasty"></a>
## The Big McNasty

Tis section covers the final, nasty, ugly, uncomfortable, despicable, unholy, 
Texas-sized hairball of a script that will make this whole Rube Goldberg machine go.

The end result will be procedurally generated blog posts, automatically processed
into static content, pushed to Github Pages, and back-dated, with all of this being done 
so that the Github commit graph will make a funny drawing of a space invader.

```
         %%       %%
        %%%%%%%%%%%%% 
     %%%%   %%%%%   %%%%
   %%%%%%%%%%%%%%%%%%%%%%%
   %%   %           %   %%
   %%   %%%%%   %%%%%   %%
```

### Directories and Files

A note on directory structure and all of that: 
* You will create a new space invader repository to put your drawing on your commit graph. You'll copy all the files you need into that repository.
* Check out a local copy of the new space invader repository.
* Pelican files should be already prepared and in the space invader repository.
* `gh-pages` branch should already be created and checked out in `pelican/source/`.
* Copy the scripts that are needed over to the space invaders repository directory and check them in there.
* Check out a copy of Olipy in the space invaders repository directory. You'll run the script from there, and it will look for Olipy there.

Now, the list of files:

* `ScriptGenerator.py` - given a list of dates, this generates a script
    that will fully populate the github repo with the necessary garbage
    to make a funny commit graph. 

* `BigMcNasty.py` - the final Big McNasty script

