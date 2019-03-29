from setuptools import setup


def read_md(f):
    return open(f, 'r').read()


setup(
    name='py-helloworld',
    version='0.0.2',
    description='Test python package',
    long_description=read_md('README.md'),
    license='MIT',
    packages=['helloworld'],
    author='Tony LE',
    author_email='lpthong90@gmail.com',
    keywords=['helloworld'],
    url='https://github.com/ThongLe/pyhelloworld',
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ]
)