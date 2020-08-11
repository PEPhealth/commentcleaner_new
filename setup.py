from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["nltk"]

setup(
    name="commentcleaner_new",
    version="0.0.1",
    author="Bobby Lowe",
    author_email="bobby.lowe@pephealth.ai",
    description="Cleans comments for scraping scrpts",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/PEPhealth/commentcleaner_new",
    download_url = 'https://github.com/PEPhealth/commentcleaner_new/archive/v_01.tar.gz',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
