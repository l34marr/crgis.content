from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='crgis.content',
    version=version,
    description="CRGIS Content Types",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.7",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Python Plone',
    author='TsungWei Hu',
    author_email='marr.tw@gmail.com',
    url='http://pypi.python.org/pypi/crgis.content',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['crgis'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'plone.app.dexterity < 2.1.0',
        'plone.dexterity >= 2.2.1',
        'plone.namedfile [blobs]',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework [debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
