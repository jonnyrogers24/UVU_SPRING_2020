import maya.cmds as cmds

sels = cmds.ls(sl=True)

for sel in sels:
    if (cmds.nodeType(sel) == 'joint'):
        if cmds.getAttr('%s.displayLocalAxis' % sel) == False:
            cmds.setAttr('%s.displayLocalAxis' % sel, k=True)
            cmds.setAttr('%s.jointOrientX' % sel, k=True)
            cmds.setAttr('%s.jointOrientY' % sel, k=True)
            cmds.setAttr('%s.jointOrientZ' % sel, k=True)
            cmds.setAttr('%s.displayLocalAxis' % sel, True)
        else:
            cmds.setAttr('%s.displayLocalAxis' % sel, k=False, cb=False)
            cmds.setAttr('%s.jointOrientX' % sel, k=False, cb=False)
            cmds.setAttr('%s.jointOrientY' % sel, k=False, cb=False)
            cmds.setAttr('%s.jointOrientZ' % sel, k=False, cb=False)
            cmds.setAttr('%s.displayLocalAxis' % sel, False)