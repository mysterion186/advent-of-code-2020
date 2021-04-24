f = open("day6.txt",'r')
a = f.readlines()

# create a list where each element is the response of all groups
def load_input(L):
	answer =[]
	answer_temp=[]
	i_prev = 0
	for i in range(len(L)):
		
		if L[i]=='\n':
			
			for k in range(i_prev,i):
				answer_temp.append(L[k].split('\n')[0])
				i_prev = i+1
			answer.append(answer_temp)
			answer_temp = []	
	return answer

def affiche(L):
	for k in range (len(L)):
		print(L[k])



# get the numbers of answered questions in one groupe
def get_numbers(L):
	temp = ""
	for k in range(len(L)):
		temp=temp+L[k]
	return len(set(temp))


def day_6(L):
	sum = 0
	for k in range(len(L)):
		sum = sum+ get_numbers(L[k])
	return sum



def day_6_v2(L):
	summ = 0
	temp = 0
	for k in range(len(L)):
		if len(L[k])==1 :
			summ = summ +len(L[k][0])
		else :
			#
			L[k].sort()
			
			for char in L[k][0]:
				temp = 0
				for i in range(1,len(L[k])):
					if char in L[k][i]:
						#print(char)
						temp +=1
						#print(temp)
					if temp == len(L[k])-1:
						summ+=1

			"""
			for i in range(len(L[k])):
				temp = 0
				for j in range(i,len(L[k])):
					for char in L[k][0]:
						if char in L[k][j]:
							temp+=1
						if temp == len(L[k]):
							summ +=1
							"""
	return summ


print("*"*10+"réponse"+"*"*10)
print("réponse pour v1 = ",day_6(load_input(a)))
print("réponse pour v2 = ",day_6_v2(load_input(a)))

#print("réponse pour v2 = ",day_6_v2([["abytu","ayu","ayu","uhodlay","uay"]]))

#['lqhksfnerg', 'negsc', 'snage', 'engs', 'sneg'],
#["abytu","ayu","ayu","uhodlay","uay"]
