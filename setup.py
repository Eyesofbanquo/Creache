from setuptools import setup

with open("./.version", "r") as f:
    variables = f.readlines()

setup(
    name="creache",
    version=variables[0],
    description="A tool that looks to convert structs to class entities in swift",
    author="Markim Shaw",
    author_email="ms79723@gmail.com",
    license="MIT",
    packages=["src.creache", "src.cli", "src.incrementer"],
    url="https://github.com/Eyesofbanquo/Creache",
    zip_safe=False,
    scripts=["src/creache/run"],
    install_requires=["click"],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
