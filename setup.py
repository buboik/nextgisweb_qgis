from setuptools import setup, find_packages

version = '0.0'

requires = (
    'nextgisweb',
)

entry_points = {
    'nextgisweb.packages': [
        'nextgisweb_qgis = nextgisweb_qgis:pkginfo',
    ],
    'nextgisweb.amd_packages': [
        'nextgisweb_qgis = nextgisweb_qgis:amd_packages',
    ],
}

setup(
    name='nextgisweb_qgis',
    version=version,
    description="",
    long_description="",
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points=entry_points,
)
