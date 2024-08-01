from setuptools import setup, find_packages

setup(
    name="silence_cutpy",
    version="1.0",
    author="Alameddin Çelik",
    author_email="alameddinc@gmail.com",
    description="A tool to remove silent parts from video files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alameddinc/silencecut-py",
    packages=find_packages(),
    install_requires=[
        "moviepy",
        "pydub",
    ],
    entry_points={
        "console_scripts": [
            "silence_cutter=silence_cutter.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
