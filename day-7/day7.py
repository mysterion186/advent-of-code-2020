"""
firt step : find in all the rules 'day7.txt' all the colors that can 
directly contain a shiny gold bag
second step : find all the colors that contain a colored bag found in 
the first step
"""

with open("day7.txt","r") as f :
    raw_rules = f.readlines()

rules = []
for rule in raw_rules : 
    rules.append(rule.replace("\n",""))

exemple = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
'bright white bags contain 1 shiny gold bag.',
'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
'faded blue bags contain no other bags.',
'dotted black bags contain no other bags.']

#step 1 find color that can contain shiny gold bag
def find_color(rules):
    color = {}
    main_color_dict = {}
    for rule in rules :
        main_color = rule[0:rule.index("bags")]
        if main_color in color :
            if not color[main_color]  :
                color[main_color] = 'shiny gold' in rule[rule.index("bags"):]
        else :
            color[main_color] = 'shiny gold' in rule[rule.index("bags"):]
    
    for key in color :
        if color[key]:
            main_color_dict[key] = True
            print("raw color ",key)
    return main_color_dict

#find all colors that can contain directly or contain a bag that can 
#contain a shiny gold bag
def find_all_color(rules):
    count = 0
    #put all the 'main' colors into a list thant will enventually contain
    #all colors
    color_list = []
    color = find_color(rules)
    for key in color :
        if color[key] :
            color_list.append(key)
    #check to find any bags that contain color from color_list
    for rule in rules:
        for main_color in color_list:
            if main_color in rule[rule.index("bags"):] :
                color_list.append(rule[0:rule.index("bags")])
                #to be sure that we don't have duplicates
                color_list = list(set(color_list))
                color[main_color] = True
    
    print(color)
    print(color_list)
    for key in color :
        if color[key] :
            count +=1 
    print("count ",count)
    return len(color_list)


"""a = (find_color(rules))
print((a))"""



