# Viewer Caller

**Viewer Caller** is a Python script designed to locate and organize Viewer nodes in Nuke's Node Graph.

## Problem

When working on complex setups in Nuke, it can be difficult to find Viewer nodes or quickly check their inputs. This script solves the issue by automatically bringing all Viewers to your current position in the Node Graph.

## Demo

To use the **Viewer Caller** script, simply trigger the function with the shortcut **Alt + W**.

![viewer_caller_demo](https://github.com/user-attachments/assets/2a79e727-504e-4abc-87af-05405972a5ff)

## Features

- **Viewer Sorting**: Sorts Viewers by name in ascending order for clear organization.
- **Horizontal Alignment**: Arranges Viewers side by side with uniform spacing.
- **Vertical Positioning**: Places Viewers slightly below the visible center of the current view for easier accessibility.
- **Zoom Adaptation**: Dynamically adjusts Viewer positions based on the current zoom level in the Node Graph.

## ***Installation***

1. Place the `viewer_caller.py` file in the **`.nuke`** directory:
   - **Windows**: `%HOME%/.nuke/`
   - **macOS/Linux**: `~/.nuke/`

2. Add the following command to your `menu.py` file located in the same `.nuke` directory:

   ```python
   import nuke
   import viewer_caller

   # Add a custom menu in Nuke
   dd_tools_menu = nuke.menu('Nuke').addMenu('DD Tools')
   dd_tools_menu.addCommand('Viewer Caller', 'viewer_caller.run()', 'Alt+W')
