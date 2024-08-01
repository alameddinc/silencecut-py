from setuptools import setup, find_packages

setup(
    name="SilenceCutter",
    version="1.0",
    author="Alameddin ÇELİK",
    author_email="alameddinc@gmail.com",
    packages=find_packages(),
    install_requires=[
        "moviepy",
        "pydub",
    ],
    entry_points={
        "console_scripts": [
            "silence_cutter=silence_cutter:main",
        ],
    },
)
