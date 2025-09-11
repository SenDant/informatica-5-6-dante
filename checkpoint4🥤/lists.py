independence_stages = ["Inicio", "Organización", "Resistencia", "Consumación"]
print(independence_stages[0])
print(len(independence_stages))

#List Methods
leaders = []
leaders.append("Miguel Hidalgo y Costilla")
#leaders.append("José María Morelos y Pavón")
leaders.append("Vicente Guerrero")
#leaders.extend(independence_stages) //mixing lists together (～￣▽￣)～
leaders.insert(1, "José María Morelos") #Inserting an elements inside the list between other elements
#leaders.remove("Vicente Guerrero") #remove especific info
leaders.append("Agustín de Iturbide")

#leaders.append(input("Type a leader: ")) #user can insert stuff in the list

#same as remove BUT with index numbers(positions)
#leaders.clear() # Will erase everything in the list
print(leaders.index("Miguel Hidalgo y Costilla")) #finds the position of an element
print(leaders.count("Vicente Guerrero"))
leaders.sort() #sort the elements by alphabetical order or ascendent order
leaders.reverse() #sort the list in reverse
new_leaders = leaders.copy()
print(new_leaders)
print(leaders)