import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

    #if i want to publish as pypi package

__version__ = '0.0.0'
REPO_NAME = "Text-summarizer"
AUTHOR_USER_NAME = "shivanshu-th"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shivanshuthakurwork@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python nlp app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)