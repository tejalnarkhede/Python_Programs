list=[1,"Tejal","GPP",96]
print(type(list))
print(list)
print(list[3:])
print(list[0:2])
print(list+list)
print(list*2)
#modifying value in list
list[2]="Narkhede"
print(list)

#Output

#<class 'list'>
#[1, 'Tejal', 'GPP', 96]
#[96]
#[1, 'Tejal']
#[1, 'Tejal', 'GPP', 96, 1, 'Tejal', 'GPP', 96]
#[1, 'Tejal', 'GPP', 96, 1, 'Tejal', 'GPP', 96]
#[1, 'Tejal', 'Narkhede', 96]

