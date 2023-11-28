
# dic={
#     "name": "mahendra",
#     "age":   21,
#     "city": "Jaipur"
# }
# print(dic)


        # Copy Method

# dic={
#     "Student Name": "Mahendra",
#     "Studnet branch": "MCA",
#     "year": 2022
# }
# print(dic)
# a_copy=dic.copy()
# print(a_copy)


            # Get Method
# Returns the value of the specified key


# d = {
#   "name": "mahendra",
#     "age": 21,
#     "city":"jaipur"
# }
#
# x = d.get("age")
#
# print(x)


            # Items Method

#
# d = {
#   "name": "mahendra",
#     "age": 21,
#     "city":"jaipur"
# }
# x=d.items()
# print(x)

      # Items values change


# d = {
#   "name": "mahendra",
#     "age": 21,
#     "city":"jaipur"
# }
# x=d.items()
# d['age']=20
# print(x)


        # key Method


# d = {
#   "name": "mahendra",
#     "age": 21,
#     "city":"jaipur"
# }
# x=d.items()
# d["Number"]=123456789
# print(x)

  # Dictionary ki all keys print

# d = {
#   "name": "mahendra",
#     "age": 21,
#     "city":"jaipur"
# }
# x=d.keys()
# d["Number"]=123456789
# print(x)


            # values Method

  #  dictionary all values print ke liye Values Method ka Used
  # and dictionary single values ko print ke liye get method ka Used
#
# d = {
#   "name": "mahendra",
#     "age": 21,
#     "city":"jaipur"
# }
# x=d.values()
# d["Number"]=123456789
# print(x)



            # fromkeys Method

    # fromkeys Method ka used multiple keys hai un sb me some type ki value ko print kra na to used is fromkeys method

x=("key1","key2","key3")
y="Mahendra"
dic=dict.fromkeys(x,y)
print(dic)