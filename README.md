# Viewer Caller - Python Script for Nuke

**Viewer Caller** is a Python script designed to automate the positioning of Viewer nodes in Nuke's Node Graph. It simplifies the organization of Viewers by sorting them, aligning them horizontally, and positioning them slightly below the visible center of the current view.

## ***Features***

- **Sorting Viewers**: Organizes Viewer nodes by name in ascending order (e.g., `Viewer1`, `Viewer2`, etc.).
- **Horizontal Alignment**: Viewers are aligned side by side with configurable uniform spacing.
- **Vertical Positioning**: Viewers are placed at the bottom of the visible view, slightly below the current center.
- **Zoom Adaptation**: Viewer positions are dynamically adjusted based on the active zoom level in the Node Graph.

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
