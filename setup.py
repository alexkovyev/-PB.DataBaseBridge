import setuptools
import pkg_resources

setuptools.setup(
    name="DBBridge",
    version="0.1dev",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=pkg_resources.parse_requirements('requirements.txt'),
    author="Vadim VZ Zhdanov",
    author_email="vz.vadia@gmail.com",
    description="Package for database access",
    url="https://github.com/alexkovyev/-PB.DataBaseBridge",
    license='MIT',
    long_description=open('README.md').read(),
    include_package_data=True,
    package_data={'': ['cfg/config.ini']},
)
