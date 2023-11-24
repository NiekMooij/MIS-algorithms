from setuptools import setup, find_packages

setup(
    name='MIS',
    version='0.0.1',
    author='Niek Mooij',
    author_email='mooij.niek@gmail.com',
    description='All algorithms used in the paper',
    url='https://github.com/NiekMooij/MIS',
    classifiers=['Programming Language :: Python :: 3',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent'],
    packages=find_packages(),
    install_requires=[
        'networkx',
        'numpy',
        'scipy',
        'pulp',
    ],
    entry_points={
        'console_scripts': [
            'continuation=MIS.continuation:main',
            'exact=MIS.exact:main',
            'greedy=MIS.greedy:main',
            'lotka_volterra=MIS.lotka_volterra:main',
        ],
    },
)

