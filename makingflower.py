```python
import maya.cmds as cmds;
import random;

// leaf
def leave(rotXnum) : 

    rotPX = 0.3;
    rotMX = -0.5;
    ext_list = [];
    box_list = [];
    box_list.extend(cmds.polyCube(n='myC'));
    print  box_list[0];
    cmds.scale(.3,0.1,1);
    cmds.move(0, -0.5, 0, box_list[0] + '.scalePivot', box_list[0] + '.rotatePivot', localSpace=True);
    cmds.rotate((45*rotXnum),0,0)
    
    for i in range (25):
        if i <= 5:
            rotPX = rotPX - 0.07;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.5, ls=(0.9, 1.15, 0) ));
        elif 5< i <= 10:
            rotPX = rotPX - 0.07;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.5, ls=(0.9, 1.12, 0) ));
        elif 10< i <= 15:
            rotMX = rotMX + 0.07;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.5, ls=(0.98, 0.98, 0) ));
        else:
            rotMX = rotMX + 0.07;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.5, ls=(.92, .92, 0) ));
            
    for b in range (25):
        cmds.setKeyframe(ext_list[b]+'.localTranslateZ', t=b);
        cmds.setKeyframe(ext_list[b]+'.localTranslateX', t=b);
        cmds.setKeyframe(ext_list[b]+'.localTranslateZ', t=0, v=0);
        cmds.setKeyframe(ext_list[b]+'.localTranslateX', t=0, v=0);
        
    
for a in range (8):        
    leave(a)
    
```