#pip install setuptools
#pip install wheel
#pip install twine

from setuptools import setup, find_packages
#python setup.py sdist bdist_wheel
#makes dist, build, name.egg-info
#twine upload dist/* --verbose
setup(
    name = 'pycraters',
    version = '0.1.0', #even if you delete the dist folder, you have to change the version number
    packages = find_packages(),
    description='',
    author='Scott Norris',
    author_email='<snorris@mail.smu.edu>',
    keywords=['craters', 'education'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=['numpy', 'matplotlib', 'scipy', 'pandas', 'lmfit', 'uncertainties', 'math', 'fittools', 'os', 'shelve', 'pylab', 'sys', 'subprocess'],
)