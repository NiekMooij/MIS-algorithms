from setuptools import setup, find_packages

setup(
    name='MIS',
    version='0.1',
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
