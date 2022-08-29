# https://www.sidefx.com/docs/houdini/hom/locations.html#startup

# Houdini runs this script when it is started without a scene (.hip) file. 
# Houdini will only run the first 123.py script it finds in the path. 
# This is useful for customizing the empty scene, for example if you want to start every scene with a default lighting rig.
# This is the Python equivalent of the 123.cmd Hscript file. If 123.cmd and 123.py both exist, Houdini will only run 123.py.

# Only Houdini FX runs 123.py. Houdini Core runs houdinicore.py instead of 123.py on startup. 
# Both 123.py and houdinicore.py serve the same purpose but for different products.

# This script enables autosave on Houdini startup (new scene).
# Be aware that the Save As window will eventually appear as Houdini will try to autosave if you are still in the new unsaved scene.

import hou
hou.appendSessionModuleSource('''hou.hscript("autosave on")''')
