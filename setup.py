from distutils.core import setup

setup(
    name='OSINT_box',
    version='1.0',
    description='OSINT module',
    author='Shy0for0u',
    author_email='secret@samedomain.com',
    packages=['full_scripts'],
    package_dir={'full_scripts': 'full_scripts'},
    package_data={'full_scripts': ['*.dat']},
)
