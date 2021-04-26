with open("day8.txt","r") as f :
    raw_program = f.readlines()

program = [line.replace("\n","") for line in raw_program]

#return a list with the instruction and the value
def get_info(line):
    return [line[0:3],line[4:]]


def day8(program,version = 1):
    i,acc = 0,0
    program_list = [0 for k in range(len(program))]
    while i != len(program):
        if program_list[i] == 0 :
            program_list[i] = 1
            instruction = get_info(program[i])[0]
            value = int(get_info(program[i])[1])
            if instruction =="acc":
                acc+= value
                i+=1
            elif instruction=="jmp":
                temp = i
                i+=value
                if program_list[i] == 1 :
                    print("instruction {} value {}".format(instruction,value))
            else :
                i+=1
        else :
            if version == 1:
                return acc
                


test =["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6 "]


print("Solution part one ",day8(program))

def find_instructions(program):
    count = 0
    for instrunction in program:
        if instrunction[0:3]=="nop" or instrunction[0:3]=="jmp":
            count +=1
    return count 

print(find_instructions(program))
for k in range(0,1):
    print(k)
