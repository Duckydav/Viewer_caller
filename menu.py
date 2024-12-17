import nuke
import viewer_caller

# Add a custom menu in Nuke
dd_tools_menu = nuke.menu('Nuke').addMenu('DD Tools')
dd_tools_menu.addCommand('Viewer Caller', 'viewer_caller.run()', 'Alt+W')
