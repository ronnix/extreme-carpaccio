import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
]

setup(
    name='extreme_carpaccio',
    version='0.1.0',
    description='extreme_carpaccio',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Ronan Amicel',
    author_email='ronan.amicel@gmail.com',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="extreme_carpaccio",
    entry_points="""\
    [paste.app_factory]
    main = extreme_carpaccio:main
    """,
)
