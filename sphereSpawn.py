import bpy

sphere = bpy.data.objects['sphere']

vertexList = [1,1,1]

for vertex in vertexList:
    name = f'sphere {vertex}'
    new_sphere = bpy.data.objects.new(name=name, object_data=sphere.data)
    new_sphere.location = (vertex[0], vertex[1], vertex[2])

    bpy.data.collections["spheres"].objects.link(new_sphere)