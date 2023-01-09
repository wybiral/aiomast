import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='aiomast',
    version='0.0.1',
    author='davy wybiral',
    author_email="davy.wybiral@gmail.com",
    description='Asynchronous Mastodon library for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wybiral/aiomast",
    packages=['aiomast'],
    install_requires=['aiohttp'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
