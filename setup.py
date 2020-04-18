import setuptools
import requirements

install_requires = []

with open('requirements.txt') as fd:
    for req in requirements.parse(fd):
        if req.name:
            name = req.name.replace("-", "_")
            full_line = name + "".join(["".join(list(spec)) for spec in req.specs])
            install_requires.append(full_line)

setuptools.setup(
    name="DBBridge",
    version="0.1.dev0",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=install_requires,
    author="Vadim VZ Zhdanov",
    author_email="vz.vadia@gmail.com",
    description="Package for database access",
    url="https://github.com/alexkovyev/-PB.DataBaseBridge",
    license='MIT',
    long_description=open('README.md').read(),
    include_package_data=True,
    package_data={'': ['cfg/config.ini']},
)
