import bpy
import sys, os
import json

# Save json data coordinates to vertexList array
# Opening walls JSON file
jsonPath = os.path.join(os.path.dirname(bpy.data.filepath), 'lightsOn.json')
f = open(jsonPath)

# returns JSON object as 
# a dictionary
data = json.load(f)

wallNames = []
x0s = []
y0s = []
z0s = []
x1s = []
y1s = []
z1s = []
pt1s = []
pt2s = []
vertexList = []

# Iterating through the json
# Save points in vertexList array

for i in data["RoomPlan_Objects"]:
    # print(i["x1"])
    # x0s.append(i["x1"])
    # x1s.append(i["x2"])
    # y0s.append(i["y1"])
    # y1s.append(i["y2"])
    # z0s.append(0.0)
    # z1s.append(0.0)
    vertexA = [i["x1"], i["y1"], 0.0]
    vertexB = [i["x2"], i["y2"], 0.0]
    vertexList.append(vertexA)
    vertexList.append(vertexB)

# print(vertexList)


sphere = bpy.data.objects['sphere']

for vertex in vertexList:
    name = f'sphere {vertex}'
    new_sphere = bpy.data.objects.new(name=name, object_data=sphere.data)
    new_sphere.location = (vertex[0], vertex[1], vertex[2])
    new_sphere.scale = (0.1, 0.1, 0.1)
    bpy.data.collections["spheres"].objects.link(new_sphere)