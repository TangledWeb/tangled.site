from setuptools import setup, find_packages


setup(
    name='tangled.site',
    version='0.1.dev0',
    description='Simple site/blog/cms',
    packages=find_packages(),
    install_requires=(
        'tangled.mako>=0.1.dev0',
        'tangled.sqlalchemy>=0.1.dev0',
        'tangled.web>=0.1.dev0',
        'alembic>=0.6.2',
        'bcrypt>=1.0.2',
        'SQLAlchemy>=0.9.1',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    entry_points="""
    [tangled.scripts]
    site = tangled.site.command

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
