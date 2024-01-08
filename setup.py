from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='project-scanner',
    version='0.1.1',
    description='A Python package to scan project directories and files batch by batch.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    url='https://github.com/chigwell/project-scanner',
    packages=find_packages(),
    install_requires=[
        # Specify any dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
