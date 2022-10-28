from distutils.core import setup

setup(
    name='pyloggor',
    version='1.0.0',
    description='An incredibly versatile yet simple logging system.',
    author='Parth Mittal',
    author_email='parth@thekoalaco.in',
    url='https://www.github.com/PrivatePandaCO/pyloggor',
    license='MIT',
    packages=['pyloggor'],
    install_requires=['rich', 'typing-extensions'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Documentation": "https://github.com/PrivatePandaCO/pyloggor/blob/master/README.md",
        "Github": "https://github.com/PrivatePandaCO/pyloggor",
        "Changelog": "https://github.com/PrivatePandaCO/pyloggor/blob/master/Changelog.md"
    }
)
