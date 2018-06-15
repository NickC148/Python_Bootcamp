# Packages are a way of structuring modules using sub directories. For the example below Python
# searches through the directories on sys.path looking for the package subdirectory. There has to
# be an __init__.py in each directory that forms part of the package.

sound/                          # Top-level package
    __init__.py                 # Initialize the sound package
    formats/                    # Subpackage for file format conversions
        __init__.py
        wavread.py
        wavwrite.py
        aiffread.py
        aiffwrite.py
        auread.py
        auwrite.py
        ...
    effects/                    # Subpackage for sound effects
        __init__.py
        echo.py
        surround.py
        reverse.py
        ...
    filters/                    # Subpackage for filters
        __init__.py
        equalizer.py
        vocoder.py
        karaoke.py
        ...

# Adding the following line into the __init__.py for the effects subdirectory would allow for
# an import sound.effects.*, but bear in mind that import * is generally frowned upon.

__all__ = ["echo", "surround", "reverse"]

# From Python 2.5 zip files can be treated like directories. Adding a zip file to sys.path means
# that all files with extension of [‘.py’, ‘.pyc’, ‘.pyo’] are treated like source or compiled
# python. Packages stored in the zip file with their sub directories would work as described above.
