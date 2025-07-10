from setuptools import setup, find_packages

setup(
    name='userhunt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyfiglet'
    ],
    entry_points={
        'console_scripts': [
            'userhunt = userhunt.__main__:main'
        ],
    },
    author='Your Name',
    author_email='you@example.com',
    description='🕵️ A fast username OSINT tool to hunt usernames across 30+ websites.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourname/userhunt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
    ],
    python_requires='>=3.6',
)
