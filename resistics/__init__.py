"""
A package for the processing of magnetotelluric data
Resistics is a package for the robust processing of magnetotelluric data. It includes several features focussed on traceability and data investigation. For more information, visit the package website at:
www.resistics.io
"""
__name__ = "resistics"
# short X.Y version
xyversion = "0.0.7"
# release
release = ".dev1"
# combined version
__version__ = "{}{}".format(xyversion, release)


from resistics.log import log_info, log_warning, log_debug
from resistics.project import new, load, reload