
# maya python. modeling, animation, shader

import maya.cmds as cmds
import random


flowerShader_list = [];
m=1;

# 잎 & 줄기 Shader
myShader = cmds.shadingNode('aiStandard', asShader=True)
cmds.setAttr ( (myShader + '.color'), 0.169,0.337,0, type = 'double3' )   

# 꽃 Shader
for m in range (6) :
    flowerShader_list.append(cmds.shadingNode('aiStandard', asShader=True, n='flowerShader'))
    cmds.setAttr ( (flowerShader_list[m] + '.color'), 0.673,0.115 + (0.05 * m),0.315, type = 'double3' )   
    
# 잎 modeling & animation
def leaves(rotXnum) : 

    rotPX = 0.3
    rotMX = -0.5
    ext_list = []
    box_list = []
    box_list.extend(cmds.polyCube(n='myC'))
    cmds.hyperShade( assign=myShader )
    
    cmds.scale(.3,0.1,1.5)
    cmds.move(0, -0.5, 0, box_list[0] + '.scalePivot', box_list[0] + '.rotatePivot', localSpace=True)
    cmds.rotate((45*rotXnum),0,0)

   
    for i in range (28):
    
        if i <= 5:
            rotPX = rotPX - 0.07
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.5, ls=(0.9, 1.15, 0) ))
        elif 5< i <= 10:
            rotPX = rotPX - 0.07
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.5, ls=(0.9, 1.12, 0) ))
        elif 10< i <= 15:
            rotMX = rotMX + 0.07
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.5, ls=(0.98, 0.98, 0) ))
        else:
            rotMX = rotMX + 0.07
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.5, ls=(.92, .92, 0) ))
            
            
    for b in range (28):
        cmds.setKeyframe(ext_list[b]+'.localTranslateZ', t=b)
        cmds.setKeyframe(ext_list[b]+'.localTranslateX', t=b)
        cmds.setKeyframe(ext_list[b]+'.localTranslateZ', t=0, v=0)
        cmds.setKeyframe(ext_list[b]+'.localTranslateX', t=0, v=0)
     
            
# 꽃 modeling & animation
def flower(rotXnum) : 

    rotPX = 0.2
    rotMX = -0.5
    ext_list = []
    box_list = []
    key_frameValue = rotXnum + 30
  
    box_list.extend(cmds.polyCube(n='myF'))
    cmds.scale(1,1,1);
    cmds.move(0, -0.5, 0, box_list[0] + '.scalePivot', box_list[0] + '.rotatePivot')
    cmds.move(-0.5, x=True)
    
    def extrudeKeyFrame(i) : 
        cmds.setKeyframe(ext_list[i]+'.localTranslateZ', t=key_frameValue)
        cmds.setKeyframe(ext_list[i]+'.localTranslateX', t=key_frameValue)
        cmds.setKeyframe(ext_list[i]+'.localTranslateZ', t=0, v=0)
        cmds.setKeyframe(ext_list[i]+'.localTranslateX', t=0, v=0)


    if 0 <= rotXnum < 8:
        cmds.rotate((45*rotXnum)+20,0,0)
        cmds.hyperShade( assign=flowerShader_list[0] )       
        for i in range (20):
            if i <= 5:
                rotPX = rotPX - 0.09
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
            elif 5< i <= 10:
                rotPX = rotPX - 0.09
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.12, 0) ))
            elif 10< i <= 13:
                rotPX = rotPX - 0.07
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.98, 0.98, 0) ))
            else:
                rotMX = rotMX - 0.03
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.4, ls=(0.88, 0.88, 0) ))
                
            extrudeKeyFrame(i)
                
       
           
                
    elif 8 < rotXnum <= 16:
        cmds.rotate((45*rotXnum)+50,0,0)
        cmds.hyperShade( assign=flowerShader_list[1] )
        for i in range (18):
            if i <= 5:
                rotPX = rotPX - 0.16
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
            elif 5< i <= 7:
                rotPX = rotPX - 0.16
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.12, 0) ))
            elif 7< i <= 13:
                rotPX = rotPX + 0.07
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.98, 0.98, 0) ))
            else:
                rotPX = rotPX + 0.13
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.88, 0.88, 0) ))
                

            extrudeKeyFrame(i)
                
                
    elif 16 < rotXnum <= 24:
        cmds.rotate((45*rotXnum)-20,0,0)
        cmds.hyperShade( assign=flowerShader_list[2] )
        for i in range (13):
            if i <= 5:
                rotPX = rotPX - 0.2
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
            elif 5< i <= 7:
                rotPX = rotPX - 0.2
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.12, 0) ))
            elif 7< i <= 10:
                rotPX = rotPX + 0.07
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.98, 0.98, 0) ))
            else:
                rotPX = rotPX + 0.13
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.88, 0.88, 0) ))
                
       
            extrudeKeyFrame(i)
                
    elif 24 < rotXnum <= 30:
        cmds.rotate(45*rotXnum,0,0)
        cmds.hyperShade( assign=flowerShader_list[3] )
        for i in range (10):
            if i <= 3:
                rotPX = rotPX - 0.25
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
            elif 3< i <= 6:
                rotPX = rotPX - 0.25
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.12, 0) ))
            elif 6< i <= 8:
                rotPX = rotPX + 0.07
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.98, 0.98, 0) ))
            else:
                rotPX = rotPX + 0.13
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.88, 0.88, 0) ))
                
            extrudeKeyFrame(i)
                
    elif 30 < rotXnum <= 33:
        cmds.rotate((45*rotXnum),0,0)
        cmds.hyperShade( assign=flowerShader_list[4] )
        for i in range (11):
            if i <= 5:
                rotPX = rotPX - 0.3
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
            elif 5< i <= 7:
                rotPX = rotPX - 0.3
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.12, 0) ))
            else:
                rotMX = rotMX - 0.03
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.4, ls=(0.88, 0.88, 0) ))
                
       
            extrudeKeyFrame(i)
              
    else:
        cmds.rotate(60*rotXnum + random.uniform(-10,30),0,0)
        cmds.hyperShade( assign=flowerShader_list[5] )
        
        if 34 <= rotXnum < 37:
            cmds.move(random.uniform(0,2), z= True)
        else:
            cmds.move(random.uniform(-2,0), z= True)
            
            
        for i in range (8):
            if i <= 3:
                rotPX = rotPX - 0.5
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
            elif 3< i <= 5:
                rotPX = rotPX - 0.5
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotPX), ltz=.4, ls=(0.9, 1.15, 0) ))
  
            else:
                rotPX = rotPX + 0.5
                ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[1]', ltx=(rotMX), ltz=.4, ls=(0.88, 0.88, 0) ))
            
     
            extrudeKeyFrame(i)
            

# 줄기 modeling & animation
def stem() :

    rotPX = 0.3
    rotMX = -0.5
    ext_list = []
    box_list = []
    box_list.extend(cmds.polyCube(n='myS'))
    
    cmds.scale(.5,.5,.5)
    cmds.move(0, 0, 0, box_list[0] + '.scalePivot',box_list[0] + '.rotatePivot', localSpace=True)
    cmds.rotate(0,0,0)
    
    cmds.hyperShade( assign=myShader )
    
    for i in range (10):
    
        if i <= 3:
            rotMX = rotMX + 1;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[4]', lty=(rotMX), ltz=2, ))
        elif 3< i <= 5:
            rotMX = rotMX + 0.09;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[4]', lty=(rotMX), ltz=2, ))
        else:
            rotMX = rotMX + 1.2;
            ext_list.extend(cmds.polyExtrudeFacet( box_list[0]+'.f[4]', lty=(rotMX), ltz=2,))


     
for a in range (8):        
    leaves(a)
    cmds.displaySmoothness( du=2, dv=2, pw=8, ps=2, po=3)
    
    
    
for k in range (44): 
    flower(k)
    cmds.displaySmoothness( du=2, dv=2, pw=8, ps=2, po=3)
    
        
stem()
cmds.displaySmoothness( du=2, dv=2, pw=8, ps=2, po=3)


