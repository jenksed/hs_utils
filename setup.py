from setuptools import setup, find_packages

setup(
    name="hs_utils",
    version="0.1.0",
    description="A simple HubSpot API client",
    long_description="""
        This package provides utility functions to interact with HubSpot's APIs, 
        including creating, updating, retrieving, and deleting resources. 
        It is designed to simplify the integration of HubSpot services into Python applications.
    """,
    author="Joshua Jenks",
    author_email="joshuadavidjenks@gmail.com",
    url="https://github.com/jenksed/hs_utils",  # Update this to your GitHub repository URL
    packages=find_packages(),
    install_requires=[
        "requests",  # Ensure you add any other necessary packages
        "beautifulsoup4",  # Assuming HTML parsing is needed, add if used
        # Add other dependencies as needed
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",  # Update if you use a different license
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Adjust based on the versions you intend to support
)
