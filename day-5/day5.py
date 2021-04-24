f= open("day5.txt",'r')
a= f.readlines()


def load_list(L):
	seat_infos=[]
	for k in range (len(L)):
		seat_infos.append(L[k].split('\n')[0])
	return seat_infos

seat_list = load_list(a)


#order two numbers [lowest, highest]
def range_row(a,b):
	if a<b:
		return [a,b] 
	else :
		return [b,a]
	

#get the row on the boarding pass
def get_row(char):
	top_row = 127
	low_row = 0
	for k in range (len(char)):
		#donne l'inrevalle des rows pour front
		if char[k]=='F':
			#print("F")
			top_row = (low_row+(top_row - low_row)//2)
			top_row = range_row(top_row,low_row)[1]
			low_row = range_row(top_row,low_row)[0]
			#print("low = {} top {}".format(low_row,top_row))

		#donne l'inrevalle des rows pour back
		if char[k]=='B':
			#print("B")
			low_row = (top_row-((top_row - low_row )//2))

			top_row = range_row(top_row,low_row)[1]
			low_row = range_row(top_row,low_row)[0]
			#print("low = {} top {}".format(low_row,top_row))

	if low_row == top_row:
		return top_row # choix arbitraire car les 2 ont la même valeur
	return "Erreur dans le programme"




#get the columns on the boarding pass
def get_columns(char):
	top_columns = 7
	low_columns = 0
	for k in range (len(char)):
		#calcul l'intervalle des columns pour lower
		if char[k]=="L":
			#print("L")
			top_columns =low_columns+( (top_columns - low_columns)//2)
			top_columns = range_row(top_columns,low_columns)[1]
			low_columns = range_row(top_columns,low_columns)[0]
			#print("low {} and top {} ".format(low_columns,top_columns))
		#calcul l'intervalle des columns pour upper
		if char[k]=="R":
			#print("R")
			low_columns = (top_columns -((top_columns - low_columns)//2))
			top_columns = range_row(top_columns,low_columns)[1]
			low_columns = range_row(top_columns,low_columns)[0]
			#print("low {} and top {} ".format(low_columns,top_columns))
		if low_columns==top_columns:
			return top_columns

	return "Erreur dans le programme"


def day_5(L):
	id_max= 0
	for k in range (len(L)):
		temp = (get_row(L[k])*8)+get_columns(L[k])
		if temp > id_max:
			id_max = temp
	return id_max


print("Solution part 1  {}".format(day_5(load_list(a)))) #913

def day_5_v2(L):
	id_list = []
	temp = -1
	for k in range(len(L)):
		#add id of seat that aren't in the front or the back of the place (127 or 0)
		if get_row(L[k]) != 0 and get_row(L[k]) != 127 :
			id_seat = (get_row(L[k])*8)+get_columns(L[k]) 
			id_list.append(id_seat)
	id_list.sort()
	for i in range(1,len(id_list)-1):
		if id_list[i] != id_list[i-1]+1 or id_list[i] != id_list[i+1]-1:
			#temp store the id+1 value
			temp = id_list[i]
	return temp-1



print("Solution part 2  {}".format(day_5_v2(seat_list))) #717







