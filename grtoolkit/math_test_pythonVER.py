from grtoolkit.Math import *
import re

expr = 'eq.append("Eq(w,integrate(C*v,(v,v0,v1))-integrate(C*v,(v,v0,v1))+integrate(8*diff(v**2,v),(v,v0,vt), (v4,f3)))")'
# print(preSympifySub(expr,v="99*red_ballons"))
# expr.find("integrate")
print(expr)

def obp(expr): #ordered bracket pairs
    open_brackets = [m.start() for m in re.finditer('\(', expr)]
    close_brackets = [m.start() for m in re.finditer('\)', expr)]
    copyOpen = open_brackets
    taken = list()
    bracket_pairs = list()
    
    all_open_brackets = [[open,'o'] for open in open_brackets]
    all_close_brackets = [[close,'c'] for close in close_brackets]
    all_brackets = sorted(all_open_brackets + all_close_brackets)

    for b in range(len(all_brackets)):
        if all_brackets[b][1] == "c":
            i = 1
            while True:
                if all_brackets[b-i][1] == "o" and b-i not in taken:
                    bracket_pairs.append([all_brackets[b-i][0],all_brackets[b][0]])
                    taken.append(b-i)
                    break
                i+=1
    sorted_bracket_pairs = sorted(bracket_pairs)
    # print(sorted(sorted_bracket_pairs)) ### BRACKET PAIRS
    return sorted_bracket_pairs

# test = "(tomato{ went } down the ) (street)"
#note: bug in working with incomplete pairs of brackets
# print(obp(test))
sorted_bracket_pairs = obp(expr)
# print(sorted_bracket_pairs)

def bp_after_func(func_name, expr, sorter_bracket_pairs): #bracket pair after function namefunction opening and closing bracket pairs in str
    funcs = [m.start() for m in re.finditer(func_name, expr)]
    master_func_bracket_pairs = list()

    for i in range(len(sorted_bracket_pairs)):
    # print(bracket_pairs[i])
        for func in funcs:
            if func > sorted_bracket_pairs[i][0] and func < sorted_bracket_pairs[i+1][0]:
                master_func_bracket_pairs.append(sorted_bracket_pairs[i+1])
    return master_func_bracket_pairs

func_bps = bp_after_func("integrate",expr,sorted_bracket_pairs)
# print(func_bps)

# print(expr)
# for bp in func_bps:
#     print(expr[bp[0]:bp[1]])

# # Needs to be comma sensitive
# commas = [m.start() for m in re.finditer(',', expr)]
# print(commas)
# print(sorted_bracket_pairs)

#find bracket pairs inside func_bps:
func_sub_bps = list()
for fbp in func_bps:
    temp_sub_bps = list()
    for bp in sorted_bracket_pairs:
        if bp[0]>fbp[0] and bp[1]<fbp[1]:
            temp_sub_bps.append(bp)
    func_sub_bps.append(temp_sub_bps)

# # func_comma
# func_sub_bps
# print(expr)
# for a in func_sub_bps:
#     for b in a:
#         print(expr[b[0]:b[1]+1])

commas = [m.start() for m in re.finditer(',', expr)]

func_comma = list()
## for each comma:
i=0
for fbp in func_bps:
    temp_comma = list()
    for comma in commas:
    ## if comma within function bracket pair:
        if comma > fbp[0] and comma < fbp[1]: #if comma within function brackets
            # for func in func_sub_bps[i]: # if comma not within any bracket pair within function
            #     for sfbp in func:
            #         if comma < sfbp[0] or comma > sfbp[1]:
            #             temp_comma.append(comma)
            AND_counter = list()
            for sfbp in func_sub_bps[i]: # if comma not within any bracket pair within function
                if comma < sfbp[0] or comma > sfbp[1]:  # is comma outside of this sub-bracket?
                    AND_counter.append(1)
                else:
                    AND_counter.append(0)
            if sum(AND_counter) == len(AND_counter): # append comma only when outside all sub-brackets
                temp_comma.append(comma)
    if comma:
        func_comma.append(temp_comma)
    i+=1

# print(func_comma)
            # append comma to list
        # append comma list to master comma list
    # zipped_list = list(zip(func bracket pair,master comma list))

# func_sections_to_protect = [1]
# strs2protect = list()
# for section in zipped_list:

print(expr)
i=0
# # for a in func_sub_bps:
# for b in func_sub_bps[0:2]:
#     print(expr[b[0]:b[1]+1])
#     i+=1

zipped_list = list(zip(func_bps,func_comma))
print(zipped_list)

i=0
for func, fcommas in zipped_list:
    i=0
    for fcomma in fcommas:
        if (len(fcommas)-i)>1:
            print(expr[fcommas[i]+1:fcommas[i+1]])
        else:
            print(expr[fcomma+1:func[1]])
        i+=1