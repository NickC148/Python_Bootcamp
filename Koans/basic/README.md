#Python Koans

Python Koans is a port of Edgecase's "Ruby Koans" which can be found
at (http://rubykoans.com/).

(https://user-images.githubusercontent.com/2614930/28401740-ec6214b2-6cd0-11e7-8afd-30ed3102bfd6.png)

Python Koans is an interactive tutorial for learning the Python programming
language by making tests pass.

Most tests are *fixed* by filling the missing parts of assert functions. Eg:

    self.assertEqual(__, 1+2)

which can be fixed by replacing the __ part with the appropriate code:

    self.assertEqual(3, 1+2)

Occasionally you will encounter some failing tests that are already filled out.
In these cases you will need to finish implementing some code to progress. For
example, there is an exercise for writing some code that will tell you if a
triangle is equilateral, isosceles or scalene.

As well as being a great way to learn some Python, it is also a good way to get
a taste of Test Driven Development (TDD).


### Downloading Python Koans

Python Koans is available through git on Github:

(http://github.com/gregmalcolm/python_koans)

It is also mirrored on bitbucket for Mercurial users:

(http://bitbucket.org/gregmalcolm/python_koans)

Either site will allow you to download the source as a zip/gz/bz2.

###Sniffer Support

Sniffer allows you to run the tests continuously. If you modify any files files
in the koans directory, it will rerun the tests.

To set this up, you need to install sniffer::

    pip install sniffer

You should also run one of these libraries depending on your system. This will
automatically trigger sniffer when a file changes, otherwise sniffer will have
to poll to see if the files have changed.

On Windows::

    pip install pywin32

(If that failed, try::
    
    pip install pypiwin32
)

Once it is set up, you just run::

```bash
sniffer
```

