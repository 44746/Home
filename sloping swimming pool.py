#George West
#14-09-2014
# sloping swimming pool

length = float(input("Please input the length of the pool in metres: "))
width = float(input("Please input the width of the pool in metres:: "))
s_depth = float(input("Please input the shallowest depth of the pool in metres:: "))
d_depth = float(input("Please input the deepest depth of the pool in metres:: "))

rectangle = length*width*d_depth
depth_dif = d_depth-s_depth
triangle = depth_dif*length*width/2
volume = rectangle - triangle
litres = volume*1000

print("You will need {0} litres to fill your pool".format(litres))
