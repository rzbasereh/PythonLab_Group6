# 3-2

##### Part 1

# Notice: Once a tuple is created, you cannot add items to it. 

tuple1 = ('95105968', 'reza')
print(tuple1)

# update tuple values
tuple1 = ()

arr1 = list(tuple1)
arr1.append('95105968')
arr1.append('reza')

tuple1 = tuple(arr1)
print(tuple1)

##### Part 2

tuple2 = ('95105965', 'ali')
tuple3 = ('95105960', 'ahmad')


wrapper = []
wrapper.append(tuple1)
wrapper.append(tuple2)
wrapper.append(tuple3)

print(tuple(wrapper))

##### Part 3

print(wrapper[0])
print(wrapper[0][0])