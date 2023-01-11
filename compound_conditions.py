result = not False and not True or True
print(result)

x = 0
y = 0
z = 0

test_1 = x or y and z

# T T T = T 
# F T T = T
# T F T = T
# F F T = T
# T T F = T
# F T F = F
# T F F = F
# F F F = F