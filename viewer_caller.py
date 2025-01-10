# ----------------------------------------------------------------------------------------------------------
# viewer_caller v1.0
# Author: David Francois
# Copyright (c) 2024, David Francois
# ----------------------------------------------------------------------------------------------------------

import nuke

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
    viewer_height = 100  # Approximate height of a Viewer node (adjust if necessary)

    # Calculate the coordinates to align the Viewers
    center_x, center_y = current_center[0], current_center[1]
    spacing = 100  # Horizontal spacing between Viewers

    # Calculate the starting point to position the Viewers at the bottom of the screen
    # The zoom level affects the "visible" position, so adjust accordingly
    start_x = center_x - (len(viewer_nodes) - 1) * spacing // 2
    adjusted_y = center_y + (300 / zoom_level)  # Place the Viewers lower (adjust "500" based on the desired height)

    # Position each Viewer
    for i, viewer in enumerate(viewer_nodes):
        viewer.setXpos(int(start_x + i * spacing))
        viewer.setYpos(int(adjusted_y))  # Align vertically at the bottom of the screen
