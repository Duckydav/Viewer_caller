# ----------------------------------------------------------------------------------------------------------
# viewer_caller v1.1
# Author: David Francois
# Copyright (c) 2024, David Francois
# ----------------------------------------------------------------------------------------------------------

import nuke

X_OFFSET = 0  # Additional offset to adjust horizontal position
Y_OFFSET = 0  # Additional offset to adjust vertical position

def run():
    # Find all Viewer nodes
    viewer_nodes = [node for node in nuke.allNodes() if node.Class() == "Viewer"]

    if not viewer_nodes:
        nuke.message("No Viewer found in the script!")
        return

    # Sort Viewers by name (alphanumeric order)
    viewer_nodes.sort(key=lambda v: v['name'].value())

    # Get the current center position and the size of the Node Graph view
    current_center = nuke.center()  # Center of the current view
    zoom_level = nuke.zoom()  # Current zoom level
    print(f"zoom_level:{zoom_level:.2f}")
    viewer_height = 100  # Approximate height of a Viewer node

    # Calculate the coordinates to align the Viewers
    center_x, center_y = current_center[0], current_center[1]
    spacing = 100  # Horizontal spacing between Viewers

    # Starting point for positioning the Viewers at the bottom of the screen
    start_x = center_x - (len(viewer_nodes) - 1) * spacing // 2 + X_OFFSET
    adjusted_y = center_y + (100 / zoom_level) + Y_OFFSET

    # Position each Viewer
    for i, viewer in enumerate(viewer_nodes):
        viewer.setXpos(int(start_x + i * spacing))
        viewer.setYpos(int(adjusted_y))  # Align vertically at the bottom of the screen
