
For more comprehensive documentation, please see the [documentation here](./docs/index.md).

# An Affix Stripping Iterative Stemming Algorithm for Tamil

This is an attempt to create a rule based affix stripping stemmer for
Tamil language. The stemmer is implemented using Snowball language
(http://snowball.tartarus.org/)

Note that this is a stemmer and not a lemmatizer. The output need not be a
dictionary word. 

---

# Building snowball with Tamil support in GNU/Linux

## From SVN

Snowball library can be built with tamil support using the patch in this
repository. The patch was taken against snowball svn @ revision 577.

```bash
# Create a build directory
$ mkdir tamil-stemmer-build
$ cd tamil-stemmer-build

# Clone the tamil-stemmer git repo
$ git clone https://github.com/rdamodharan/tamil-stemmer.git

# Clone the snowball code
$ svn co -r 577 svn://snowball.tartarus.org/snowball/trunk/snowball snowball

# apply the patch and build snowball
$ cd snowball
$ svn patch ../tamil-stemmer/snowball-tamil.patch
$ make

# Test the stemmer
# this will wait for input in the console. input
# the words and get the stemmed form. Ctrl-C to quit
$ ./stemwords -l ta
கண்கள்
கண்
^C

# stemmer UI
# this script assumes that stemwords executable is in current directory
# if no arguments is passed. If stemwords executable is in different
# location it needs to be passed as first argument
# eg. ../tamil-stemmer/stemmer-ui.py /path/to/stemwords
# NOTE: stemmer UI requires python 2.x and pygtk-2.0
$ python ../tamil-stemmer/stemmer-ui.py
```

## From the tar file

The repository includes a snowball source tarball already patched with
tamil support.

```bash
$ mkdir tamil-stemmer-build
$ cd tamil-stemmer-build

$ git clone https://github.com/rdamodharan/tamil-stemmer.git

$ tar -zxf tamil-stemmer/snowball-with-tamil.tgz
$ cd snowball-with-tamil
$ make

$ ./stemwords -l ta
கண்கள்
கண்

# stemmer UI
# this script assumes that stemwords executable is in current directory
# if no arguments is passed. If stemwords executable is in different
# location it needs to be passed as first argument
# eg. ../tamil-stemmer/stemmer-ui.py /path/to/stemwords
# NOTE: stemmer UI requires python 2.x and pygtk-2.0
$ python ../tamil-stemmer/stemmer-ui.py
```

---

# License

This software is distributed under BSD-2-Clause license. Please refer to
LICENSE.txt

