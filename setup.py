from setuptools import setup, find_packages

setup(
    name="encryption-lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ],
    author="Nikhil Jain",
    author_email="nikhil.jain@techrbm.com",
    description="A library for encrypting and verifying user data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/njnikhiljain/encryption-lib",  # Optional GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
