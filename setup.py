from setuptools import setup

setup(
    name = "npgamma",
    version = "0.4.0",
    author = "Simon Biggs",
    author_email = "mail@simonbiggs.net",
    description = "Perform a gamma evaluation comparing two dose grids",
    long_description = "Using numpy to find the gamma index / gamma evaluation. This gamma index is often used in Medical Physics. Example of the code in action can be found [here (3d)](http://nbviewer.ipython.org/github/SimonBiggs/npgamma/blob/master/example_3d.ipynb), and [here (2d)](http://nbviewer.ipython.org/github/SimonBiggs/npgamma/blob/master/example_2d_equal_grid.ipynb). USE AT YOUR OWN RISK",
    keywords = ["radiotherapy", "gamma evaluation", "gamma index", "distance to agreement", "medical physics"],
    url = "https://github.com/SimonBiggs/npgamma/",
    packages = ["npgamma"],
    license='AGPL3+',
    classifiers = [],
)
