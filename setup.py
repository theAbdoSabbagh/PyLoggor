from distutils.core import setup

setup(
    name='PyLoggor',
    version='1.1.3',
    description='An incredibly versatile yet simple logging system.',
    author='Parth Mittal',
    author_email='parth@thekoalaco.in',
    url='https://www.github.com/PrivatePandaCO/PyLoggor',
    license='MIT',
    packages=['PyLoggor'],
    install_requires=['rich'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Documentation": "https://github.com/PrivatePandaCO/PyLoggor/blob/master/README.md",
        "Github": "https://github.com/PrivatePandaCO/PyLoggor",
        "Changelog": "https://github.com/PrivatePandaCO/PyLoggor/blob/master/Changelog.md"
    }
)
