from setuptools import setup, find_packages

setup(
    name="alterpy",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn"
    ],
    author="Harshil Gajjarvati",
    description="A Python library for analyzing and visualizing attendance data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
