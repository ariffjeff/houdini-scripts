# houdini-scripts
Useful Houdini scripts such as those that enable autosave by default.

# Installation
1. Save the scripts anywhere, for this example in a folder named `houdini-scripts`.
2. Find the `houdini.env` file for your current install of Houdini. Usually located in `C:\Users\USER\Documents\houdiniXX.X\houdini.env`
3. Append the following environment variable to the end of `houdini.env`: `HOUDINI_SCRIPT_PATH = "C:/path/to/houdini-scripts;&"`
4. The scripts will be recognized the next time you start up a new Houdini instance.

# Note
Scripts `123.py` and `456.py` must be named like so in order for houdini to recognize them.
