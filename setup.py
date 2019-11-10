from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="text-validator",
    version="0.1",
    description="pluggable command-line tool for validating the formatting and orthography of text files",
    url="http://github.com/jtauber/text-validator",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["text_validator", "text_validator.plugins"],
    entry_points={"console_scripts": ["validate-text = text_validator.main:main",],},
    install_requires=["toml",],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Text Processing",
    ],
)
