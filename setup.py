from setuptools import setup, find_packages

setup(
    name="smbus_ssd1306",
    version="0.0.1",
    description="Yet another smbus implementation of the SSD1306 OLED driver",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Tom Wallis",
    url="https://github.com/TWALL9/smbus_ssd1306",
    packages=find_packages(),
    requires=[
        "smbus2",
        "pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
