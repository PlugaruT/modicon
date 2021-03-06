import setuptools

setuptools.setup(
    name="modicon",
    version="0.0.1",
    # url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Tudor Plugaru",
    author_email="plugaru.tudor@gmail.com",

    description="Python API for reading from Modicon TM251 logic controller",
    long_description=open('readme.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['pymodbus'],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)