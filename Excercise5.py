#Data types in python (Numbers, Strings, Lists, Tuples & Dictionaries)

#Data type list
	juices_list = ['Banana', 'Carot', 'Strawberry', 'Avocado']
	
	print(juices_list[0]) #Index value & it will show up first value as "Banana"
	
	print(juices_list[2]) #Guess what, it will show the value "Strawberry"
	
	#We can also play with the list 
	
	print(juices_list) #It will display all the values
	
	print(juices_list[:2]) #It will display first two values from the list as "Banana", "Carot"
	
	print(juices_list[1:2]) #t will display only second value and first value would be ignore. 
	
	print(juices_list[2:4]) #It will display last two values of the list as "Strawberry", "Avocado"
	
	#We can also replace value of the list item, suppose you want to change second value from carot to watermelon
	
	juices_list[1] = "Watermelon"
	
	print(juices_list[1]) #Result would be Watermelon
	
	icecream_list = ['Mango', 'Cassata', 'Nuts', 'Chocolate'] #Second list
	
	combine_list = [juices_list, icecream_list]
	
	print(combine_list[0][2]) #Result would be 'Strawberry'
	
	print(combine_list[1][2]) #Result would be 'Nuts'
	
	juices_list.append('Orange') #This will add another item to list
	
	print(juices_list) #['Banana', 'Carot', 'Strawberry', 'Avocado', 'Orange']

	juices_list.insert(1, "Pomogranate") #This will insert Pomogranate on 1 index
	
	juices_list.remove("Orange") ##This will remove orange from the list
	
	juices_list.sort() #This will sort the list
	
	juices_list.reverse() #This will reverse the list
	
	del juices_list[4] #This will del the value of index 4
	
	print(len(juices_list)) #We can find the length of the strings
	
	print(max(juices_list)) #We can see the maximum value
	
	print(min(juices_list)) #We can see the minimum value
	
	#Tuples
	
	#Tuples are similar to list and we can interchange them easily. The difference between tuples and list are once tuple is created it can't be change unlike list.
	
	tuples = (10, 20, 30, 40, 50)
	
	tuples_to_list = list(tuples)
	list_to_tuples = tuple(tuples)
	
	#Dictionaries #They are also same like list but the difference is we can't concatenate like list using +

	movie = { 'Avengers' : 'Action movies with super heroes', 'Inception' : 'Dream inside dream', 'lucy': 'Science Fiction', 'Panda' : 'Comedy Movie'}
	
	print(movie['Avengers']) #Result would be "Action movies with super heroes"
	
	del movie['Panda'] #This will delete the key and value of panda
	
	movie['lucy'] = 'When someone can use 100%' #This will change the value of lucy
	
	print(len(movie)) #Length of the dictionary
	
	print(movie.get("inception"))
	
	print(movie.key())
	
	print(movie.values())
