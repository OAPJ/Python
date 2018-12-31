my_list = ["string", 15, 14.6, True]

my_list.append(6)
my_list.insert(1, "insert") #pide la posicion donde se va a guardar y lo que se va a guardaar

my_list.remove(15) #elimina un elemento
#print(my_list)
last_value = my_list.pop() #extrae el utlimo elemento de la Lista
#print(my_list)
#print(last_value)
my_list2 = [1, 9, 22, 6, 8, 65, 14, 99]
my_list3 = [22, 23]
my_list2.sort() #ordena la lista de manera ascedente
my_list3.sort(reverse = True) #ordena la lista de manera descedentes

my_list2.extend(my_list3) #Junta dos listas
print(my_list2)
