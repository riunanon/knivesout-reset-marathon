import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knivesout",
    version="0.1.0",
    author="riunanon",
    description="reset marathon tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riunanon/knivesout-reset-marathon-shortcut-keyboard-pythonista3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
