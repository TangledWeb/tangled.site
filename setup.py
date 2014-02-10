from setuptools import setup


setup(
    name='tangled.site',
    version='0.1a2.dev0',
    description='Simple site/blog/cms',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=[
        'tangled',
        'tangled.site',
        'tangled.site.model',
        'tangled.site.resources',
        'tangled.site.tests',
    ],
    include_package_data=True,
    install_requires=[
        'tangled.mako>=0.1.dev0',
        'tangled.sqlalchemy>=0.1.dev0',
        'tangled.web>=0.1.dev0',
        'alembic>=0.6.2',
        'bcrypt>=1.0.2',
        'Markdown>=2.3.1',
        'SQLAlchemy>=0.9.1',
    ],
    extras_require={
        'dev': [
            'tangled[dev]',
        ],
    },
    entry_points="""
    [tangled.scripts]
    site = tangled.site.command

    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
