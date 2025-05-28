from setuptools import setup, find_packages

# Load dependencies from requirements.txt
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="climate-opinions-and-elections",  # Name of your package
    version="0.1.0",  # Initial version
    author="Paraskevas Leivadaros",
    author_email="paraskevasleivadaros@gmail.com",
    description="Exploring how attitudes toward climate change shift before and after elections, influenced by policies implemented during election cycles. Includes data analysis, visualizations, and models to uncover trends in public perception and the impact of political events on climate opinions",
    long_description=open("README.md").read(),  # Use README.md as the long description
    long_description_content_type="text/markdown",
    url="https://github.com/paraskevasleivadaros/climate-opinions-and-elections",  # Link to your repository
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=required,  # Use requirements.txt for dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Minimum Python version
)