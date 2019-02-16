import maya.cmds as cmds

items = cmds.ls(sl=True)

for item in items:
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.constructionHistory( q=True, tgl=True )