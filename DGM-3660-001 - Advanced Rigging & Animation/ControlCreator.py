import maya.cmds as cmds

def group():
    sels = cmds.ls(sl=True)
    
    for sel in sels:
        #get transformation of sel
        #create group
        #paste xform values into group
        #rename the group
        #parent sel into the group
        
        pos = cmds.xform(sel, q=True, ws=True, translation=True)
        orient = cmds.xform(sel, q=True, ws=True, rotation=True)
        
        grp = cmds.group(empty=True, world=True)
        cmds.xform(grp, ws=True, Translation=pos)
        cmds.xform(grp, ws=True, rotation=orient)
        
        cmds.rename(grp, sel + '_Grp')