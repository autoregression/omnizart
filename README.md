# omnizart

![build](https://github.com/Music-and-Culture-Technology-Lab/omnizart/workflows/general-check/badge.svg)

Omniscient Mozart, being able to transcribe everything in the music, including vocal, drum, chord, beat, instruments, and more.
Combines all the hard works developed by everyone in MCTLab into a single command line tool, and plan to distribute as a python package in the future.

# About
[Music and Culture Technology Lab (MCTLab)](https://sites.google.com/view/mctl/home) aims to develop technology for music and relevant applications by levering cutting-edge AI techiniques.

# Plan to support
| Commands | transcribe         | train | evaluate | Description                       |
|----------|--------------------|-------|----------|-----------------------------------|
| music    | :heavy_check_mark: |       |          | Transcribes notes of instruments. |
| drum     |                    |       |          | Transcribes drum tracks.          |
| vocal    |                    |       |          | Transcribes pitch of vocal.       |
| chord    |                    |       |          | Transcribes chord progression.    |
| beat     |                    |       |          | Transcribes beat position.        |

Example usage
<pre>
omnizart music transcribe --audio-path <i>path/to/audio</i> --model-path <i>path/to/model</i>
</pre>


# Development
Describes the neccessary background of how to develop this project.

## Package management
Uses [poetry](https://python-poetry.org/) for package management, instead of writing `requirements.txt` and `setup.py` manually.

## Documentation
Automatically generate documents from inline docstrings of module, class, and function. 
[Hosted document page](http://140.109.21.96:8000/build/html/index.html)

Documentation style: Follows `numpy` document flavor. Learn more from [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html).

Document builder: [sphinx](https://www.sphinx-doc.org/en/master/)

To generate documents, `cd docs/` and execute `make html`. To see the rendered results, run `make serve` and view from the browser.
All documents and docstrings use **reStructured Text** format. More informations about this format can be found from 
[Sphinx's Document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

## Linters
flake8, pylint, black

To check with linters, execute `make check`. To format the code with black, enter `make format`.

## Unittest
Uses `pytest` for unittesting. Under construction...

## CI/CD
Uses github actions for automatic linting, unittesting, document building, and package release. Under construction...

## Command Test
To actually install and test the `omnizart` command, execute `make install`. This will automatically create a virtual environment and install everything needed inside it. After installation, just follow the instruction showing on the screen to activate the environment, then type `omnizart --help` to check if it works. After testing the command, type `deactivate` to leave the virtual environment. 
