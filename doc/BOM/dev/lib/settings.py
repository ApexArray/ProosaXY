import os
from pathlib import Path


BASE_PATH = Path(os.path.dirname(__file__))
MAIN_PROJECT_PATH = BASE_PATH.parent.parent.parent.parent
CAD_FILE = MAIN_PROJECT_PATH / 'src/freecad/component-assembly/MAIN.FCStd'
# Use EXTRA_CAD_FILES to find colors of parts not in the main assembly
# EXTRA_CAD_FILES = [
#     SNAKEOIL_PROJECT_PATH / 'WIP/component-assembly/toolhead-carrier-sherpa-1515-assembly.FCStd',
#     SNAKEOIL_PROJECT_PATH / 'WIP/component-assembly/top-lid-assembly.FCStd',
#     SNAKEOIL_PROJECT_PATH / 'WIP/component-assembly/sherpa-mini-assembly.FCStd',
#     SNAKEOIL_PROJECT_PATH / 'WIP/component-assembly/bottom-panel-250-assembly.FCStd',
#     SNAKEOIL_PROJECT_PATH / 'WIP/component-assembly/4PR-assembly.FCStd',
#     SNAKEOIL_PROJECT_PATH / 'WIP/E-axis/sherpa-mini.FCStd',
# ]
# STL_PATHS = [
#     SNAKEOIL_PROJECT_PATH / 'BETA3_Standard_Release_STL' / 'STLs',
#     SNAKEOIL_PROJECT_PATH / 'BETA3_4PR_Release_STL' / 'STLs',
#     # SNAKEOIL_PROJECT_PATH / 'BETA3_Standard_Release_STL' / 'STLs',
# ]
# Convert to relative paths
# STL_PATHS = [x.relative_to(MAIN_PROJECT_PATH) for x in STL_PATHS]
# # Ignore STL files in these directories
# STL_EXCLUDE_DIRS = [
#     (MAIN_PROJECT_PATH / "BETA3_Standard_Release_STL/STLs/Add-on"),
#     (MAIN_PROJECT_PATH / "BETA3_Standard_Release_STL/STLs/Tools"),
#     (MAIN_PROJECT_PATH / "BETA3_Standard_Release_STL/STLs/Panels/Bottom-panel/alt"),
#     (MAIN_PROJECT_PATH / "BETA3_Standard_Release_STL/STLs/Z-axis/alt"),
# ]
# Convert to relative paths
# STL_EXCLUDE_DIRS = [x.relative_to(MAIN_PROJECT_PATH) for x in STL_EXCLUDE_DIRS]
# STL_EXCLUDE_STRINGS = [
#     "OPTIONAL"
# ]

USE_CACHE = False