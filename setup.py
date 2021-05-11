from setuptools import setup

setup(
    name="creache",
    version="0.1",
    description="A tool that looks to convert structs to class entities in swift",
    author="Markim Shaw",
    author_email="ms79723@gmail.com",
    license="MIT",
    packages=["creache"],
    zip_safe=False,
    scripts=["bin/creache"],
    install_requires=["re", "asyncio", "click"],
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
