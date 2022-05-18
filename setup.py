from setuptools import setup
import os
VERSION_TEMPLATE = """
# Note that we need to fall back to the hard-coded version if either
# setuptools_scm can't be imported or setuptools_scm can't determine the
# version, so we catch the generic 'Exception'.
version = 1.0
""".lstrip()

setup(use_scm_version={'write_to': os.path.join('src', 'version.py'),
                       'write_to_template': VERSION_TEMPLATE})
