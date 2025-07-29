import pypose as pp

link1_to_d1 = pp.SE3([0, 0, 0, 0.527, -0.525, 0.473, -0.473])
link2_to_d2 = pp.SE3([0, 0, 0, 0.528, -0.525, 0.473, -0.472])
link3_to_d3 = pp.SE3([0, 0, 0, 0.527, -0.525, 0.474, -0.472])

d1_to_d2 = pp.SE3([-0.816414, -0.865774, 0.515056, -0.057232, 0.384691, 0.602994, 0.692261])
d1_to_d3 = pp.SE3([-0.183869, -0.587545, 0.344056, -0.319156, 0.114013, 0.399843, 0.851625])

base_to_link1 = pp.SE3([0, 0, 0, 0, 0, 0, 1])

d2_to_link2 = link2_to_d2.Inv()  # link2_to_d2的逆变换
d3_to_link3 = link3_to_d3.Inv()  # link3_to_d3的逆变换

# 计算base_to_link2
# 变换链: base → link1 → d1 → d2 → link2
base_to_link2 = base_to_link1 @ link1_to_d1 @ d1_to_d2 @ d2_to_link2

# 计算base_to_link3  
# 变换链: base → link1 → d1 → d3 → link3
base_to_link3 = base_to_link1 @ link1_to_d1 @ d1_to_d3 @ d3_to_link3

print("base_to_link2:")
print(base_to_link2)
print("\nbase_to_link3:")
print(base_to_link3)