# import array
my_list = [10,20,30]
print(my_list)

my_tupple = (10,20,30) # tupple is ddefined by bracket
# is once added the vaules cannot be changed 
# my_tupple[1] = 40     # this line will give error
print(my_tupple)

my_tuyple_2 = ([1],[2],[3],10)     #this is tuiple of a lists
my_tuyple_2  [1] [0] = 4        # not actually changing tupple we are changing list's element
my_tuyple_2[1].append(5)
print(my_tuyple_2)

my_dict = {1:"arpit",2:"adarsh",3:"amisha",1:"Sapna"}
my_dict[4] = "Ayush"
print(my_dict)
print(my_dict.get(1))
del my_dict[2]
