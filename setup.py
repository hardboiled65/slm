from distutils.core import setup

setup(
    name='slm',
    packages=[],
    scripts=['slm'],
    version='0.0.2',
    license='MIT',
    description='Seshat library manager.',
    author='hardboiled65',
    author_email='hardboiled65@gmail.com',
    url='https://github.com/hardboiled65/slm',
    download_url='https://github.com/hardboiled65/slm/archive/v0.0.2.tar.gz',
    keywords=['c', 'c++'],
    install_requires=[
        'pyyaml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
