from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# Filter out empty lines and comments
install_requires = [req.strip() for req in install_requires if req.strip() and not req.strip().startswith("#")]

# get version from __version__ variable in apex_item/__init__.py
from apex_item import __version__ as version

setup(
	name="apex_item",
	version=version,
	description="Item pricing tools",
	author="Gaber",
	author_email="gaber@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)


