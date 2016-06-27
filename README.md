# Asmodeus

**Table of Contents:**

[Pelican](#pelican)

[Content](#content)

[Commit](#commit)

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

Pelican:

```
pip install Markdown
pip install pelican
```

### Directories

`pelican/` - Files and Pelican configuration used to generate static content 

### Branches

`gh-pages` branch - contains the static content, which is served up by Github Pages.

[http://charlesreid1.github.io/asmodeus](http://charlesreid1.github.io/asmodeus) - webpage where the static content is served up.



<a name="content"></a>
## The Content Generation Toolchain

This tool will automatically generate text using Olipy, a procedural and artistic text generation library.

It will then generate blog posts using the automatically generated text.

Finally, it will re-generate the static content for the Pelican blog.

### Tools Required

Olipy:

```
git clone http://github.com/leonardr/olipy
```

### Directories

`content/` - directory containing the tools for content generation

### Branches

`master` branch - nothing special here.



<a name="commit"></a>
## The Commit Toolchain

Add new blog posts

Add new static site contents.



<a name="scheduling"></a>
## The Scheduling Toolchain

Using libfaketime and other trickery to make the commit graph look just so.

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

