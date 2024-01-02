import setuptools


# first reading README.md, there is no need to read this readme.md 
# only whenever publishing this project as pypi package.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# version is 0.0.0 only, this is the first time we are implimenting this project.
__version__ = "0.0.0"

REPO_NAME = "Blur-and-Non-Blur-image-classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "pravalli029"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "pravalli029@gmail.com"

# this code will look for constructor file and install as local package.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)