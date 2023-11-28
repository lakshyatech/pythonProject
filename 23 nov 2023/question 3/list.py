# lis=[10,34,20,30.43,100]
# print(lis)
# # index value print
# print(lis[0])

            #1. sorted Method
# sort list
# lis=[1,3,2,0.43,1]
# print("sort elements",sorted(lis))
# l=sorted(lis)
# print(l)
# lis.sort()
# print(lis)


                    #2. sum Method

# list all elements sum
# l=[12,34,5,46]
# print(sum(l))               # sum Method used

# i=l[0]+l[1]+l[2]+l[3]      # index value used
# print(i)

# l=[12,34,5,46]                 # list all elements sum used loops
# for i in l:
#     print(i)
# print("all elements sum=",sum(l))


                    # Append Method
# addend is function
#  it this takes a single argument,
# it insert the value end of a list
# Append function take any data input number,string,decimael number list another object

# mylist=['lakshya','shreya','mohit']       # append method used
# mylist.append("mohit")
# print(mylist)
#
# number_list=[1,2,3,4]
# mylist.append(number_list)
# print(mylist)


                        # Count Method


# list_count=['agarwal','aggarwal','agrawal','aagarwal']
# l=list_count.count('agarwal')
# print(l)



# lis=['A','B','A','C','B','A','AA','C']
# print(lis.count('A'))


                    # Extend Method


# f=['apple','banana','cherry',]
# add_f=['orange','grape']
# f.extend(add_f)
# print(f)


# abc=['mon','tus','wed',8,7,9]
# abc.extend('jan')
# print(abc)


        # Remove Method

# l=['a',78,98,98.6]
# print(l)
# l.remove('a')
# print(l)


# loop used this remove elements

l=[1,22,3,4,5,64,3,4,2,3]
while 2 in l:
    l.remove(2)
print(l)

