# https://www.sidefx.com/docs/houdini/hom/locations.html#startup

# Houdini runs this script whenever a scene file is loaded (including when Houdini starts up with a scene file).
# This is the Python equivalent of the 456.cmd Hscript file.

# This script enables autosave on scene file load

import hou
hou.appendSessionModuleSource('''hou.hscript("autosave on")''')
