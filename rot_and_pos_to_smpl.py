import maya.standalone
import maya.cmds as cmds

import csv


maya.standalone.initialize(name='python')
cmds.loadPlugin( allPlugins=True )



cmds.file('data/smpl.fbx', i=True, type='FBX')
cmds.rotate(0, 0, 180 , 'm_avg_root')

cmds.currentTime(0, edit=True)

jointlist = [
'm_avg_Pelvis',
'm_avg_L_Hip',
'm_avg_R_Hip',
'm_avg_Spine1',
'm_avg_L_Knee',
'm_avg_R_Knee',
'm_avg_Spine2',
'm_avg_L_Ankle',
'm_avg_R_Ankle',
'm_avg_Spine3',
'm_avg_L_Foot',
'm_avg_R_Foot',
'm_avg_Neck',
'm_avg_L_Collar',
'm_avg_R_Collar',
'm_avg_Head',
'm_avg_L_Shoulder',
'm_avg_R_Shoulder',
'm_avg_L_Elbow',
'm_avg_R_Elbow',
'm_avg_L_Wrist',
'm_avg_R_Wrist',
'm_avg_R_Hand',
'm_avg_R_Hand'
]

fullpath = 'data/mr_output/rot_out.csv'
fullpath2 = 'data/mr_output/pos_out.csv'



lines2 = csv.reader(open(fullpath2, 'r'), delimiter=',')


with open(fullpath, 'r') as csvfile:
    lines = list(csv.reader(csvfile, delimiter=','))



    num_frames = len(lines)
    print(num_frames)


    cmds.playbackOptions(minTime=0)
    cmds.playbackOptions(maxTime=num_frames)
    cmds.playbackOptions(animationStartTime=0)
    cmds.playbackOptions(animationEndTime=num_frames)
    cmds.playbackOptions(minTime=0)
    cmds.playbackOptions(maxTime=num_frames)

    for line, line2 in zip(lines, lines2):
        fline = [float(p) for p in line]
        coordinates = [[fline[0], fline[1], fline[2]], fline[3:6], fline[6:9], fline[9:12],
                       fline[12:15], fline[15:18], fline[18:21], fline[21:24],
                       fline[24:27], fline[27:30], fline[30:33], fline[33:36],
                       fline[36:39], fline[39:42],fline[42:45], fline[45:48],
                       fline[48:51], fline[51:54], fline[54:57], fline[57:60],
                       fline[60:63], fline[63:66], fline[66:69], fline[69:72]]



        current_frame = cmds.currentTime(q=True)

        for jointt, angle in zip(jointlist, coordinates):
            cmds.rotate(angle[0], angle[1], angle[2], jointt)
            cmds.setKeyframe(jointt)

        cmds.move(-float(line2[0]), line2[1], line2[2], jointlist[0])
        cmds.setKeyframe(jointlist[0])

        cmds.currentTime(current_frame + 1, edit=True)

    cmds.select( jointlist, add=True)
    cmds.select( 'm_avg', add=True)
    cmds.file('data/fbx/aco.fbx', force = True, options = "v = 0", type = "FBX export", exportSelected = True)
