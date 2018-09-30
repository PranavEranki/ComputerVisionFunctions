import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ComputerVisionFunctions",
    version="0.0.1",
    author="Pranav Eranki",
    author_email="pranav.eranki@gmail.com",
    description="An easy to use, high-level computer vision library containing assorted functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PranavEranki/ComputerVisionFunctions",
    packages=['ComputerVisionFunctions'],
    include_packade_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
