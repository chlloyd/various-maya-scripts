import maya.cmds as cmds

selection = cmds.ls(selection=True)
for mesh in selection:
	cmds.xform(mesh, centerPivots=1)
