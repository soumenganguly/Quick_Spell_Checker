from setuptools import setup,find_packages
setup(
    name="Quick_Spell_Checker",
    version="0.1",
    packages=find_packages,
    install_requires=["pyenchant","pyyaml","nltk"],
    dependency_links=["http://www.abisource.com/projects/enchant/","http://www.aspell.net","http://nltk.github.com/nltk_data"],
    #personal info
    author="Soumen Ganguly",
    author_email="soumendotganguly@gmail.com",
    description="A quick spell checking utility",
    license="GNU GPLv3",
    )
