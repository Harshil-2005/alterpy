from setuptools import setup, find_packages

setup(
    name='alterpy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'numpy'
    ],
    description='A Python library for analyzing and visualizing student attendance data.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/Harshil-2005/alterpy',
)
