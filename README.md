# Asmodeus

**Table of Contents:**

[Pelican](#pelican)

[Content](#content)

[Commit](#commit)



## About 

Attempting demonic possession of my Github account. What could possibly go wrong?

Oops, shouldn't have run that script. Let me just...

Wait... what's... oh no! No no no noooooo...

Fm'latgh hrii nnnep uaaah kn'a vulgtm y'hahor ph'orr'e lloig, 
'fhalma ph'bug lw'nafh fm'latghoth Yoggoth uln ah syha'hoth 
ebunma nilgh'ri vulgtlagln throd, ph'mnahn' Cthulhu hafh'drnyar 
nnnchtenff nog mnahn' kn'a naooboshu syha'h Yoggothor! 



<a name="pelican"></a>
## The Pelican Site

This tool will manage a website with Pelican, a static page generator for Python.

### Tools Required

To install Pelican, use pip:

```
pip install Markdown
pip install pelican
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



<a name="content"></a>
## The Content Generation Toolchain

This tool will automatically generate text using Olipy, a procedural and artistic text generation library.

It will then generate blog posts using the automatically generated text.

Finally, it will re-generate the static content for the Pelican blog.

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



<a name="commit"></a>
## The Commit Toolchain

When automatically generated content has been turned into a new blog post, and the static content for the site has been updated, 
it is time to actually commit changes. This portion of the code enables adding colorful dots to your commit graph. 

### Tools Required

This requires a Python library to interface with git.

### Directories and Files

`GitAddBlogPosts.py` - adds the new blog post in the `pelican/` directory to the `master` branch.

`GitAddSiteContent.py` - adds the updated Pelican blog static content to the `gh-pages` branch.




<a name="scheduling"></a>
## The Scheduling Toolchain

Using libfaketime and other trickery to make the commit graph look just so.

This will take some thinking through...

### Tools Required

Libfaketime:

On Mac OS X,

````
brew install libfaketime
```

On Linux,

```
git clone https://github.com/wolfcw/libfaketime
cd libfaketime
make
```

