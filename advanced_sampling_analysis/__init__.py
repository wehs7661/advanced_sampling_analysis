"""
advanced_sampling_analysis
This is a repository providing useful tools for analyzing simulations results obtained from advanced sampling. 
"""

# Add imports here
from .advanced_sampling_analysis import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
