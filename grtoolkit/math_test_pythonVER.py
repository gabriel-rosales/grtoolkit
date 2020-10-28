from grtoolkit.Math import *
import re

def gen_sorted_bracket_pairs(expr): #ordered bracket pairs
    open_brackets = [m.start() for m in re.finditer('\(', expr)]
    close_brackets = [m.start() for m in re.finditer('\)', expr)]
    # copyOpen = open_brackets
    taken = list()
    bracket_pairs = list()
    
    all_open_brackets = [[open,'o'] for open in open_brackets]
    all_close_brackets = [[close,'c'] for close in close_brackets]
    all_brackets = sorted(all_open_brackets + all_close_brackets)

    if len(all_open_brackets) != len(all_close_brackets):
        raise "Error: Non-even brackets."

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

def gen_func_bps(func_name, expr, sorted_bracket_pairs): #bracket pair after function namefunction opening and closing bracket pairs in str
    funcs = [m.start() for m in re.finditer(func_name, expr)]
    master_func_bracket_pairs = list()

    for i in range(len(sorted_bracket_pairs)):
    # print(bracket_pairs[i])
        for func in funcs:
            if func > sorted_bracket_pairs[i][0] and func < sorted_bracket_pairs[i+1][0]:
                master_func_bracket_pairs.append(sorted_bracket_pairs[i+1])
    return master_func_bracket_pairs

def gen_func_sub_bps(func_bps,sorted_bracket_pairs): 
    """function sub bracket pairs"""
    #Find bracket pairs inside func_bps:
    func_sub_bps = list()
    for fbp in func_bps:
        temp_sub_bps = list()
        for bp in sorted_bracket_pairs:
            if bp[0]>fbp[0] and bp[1]<fbp[1]:
                temp_sub_bps.append(bp)
        func_sub_bps.append(temp_sub_bps)
    return func_sub_bps

def gen_func_commas(expr, func_bps, func_sub_bps):
    #Find commas inside function bracket pairs that are not inside function sub bracket pairs
    commas = [m.start() for m in re.finditer(',', expr)]
    func_commas = list()
    ## for each comma:
    i=0
    for fbp in func_bps:
        temp_comma = list()
        for comma in commas:
        ## if comma within function bracket pair:
            if comma > fbp[0] and comma < fbp[1]: #if comma within function brackets
                AND_counter = list()
                for sfbp in func_sub_bps[i]: # if comma not within any bracket pair within function
                    if comma < sfbp[0] or comma > sfbp[1]:  # is comma outside of this sub-bracket?
                        AND_counter.append(1)
                    else:
                        AND_counter.append(0)
                if sum(AND_counter) == len(AND_counter): # append comma only when outside all sub-brackets
                    temp_comma.append(comma)
        if comma:
            func_commas.append(temp_comma)
        i+=1
    return func_commas

def gen_ranges2protect(func_bps, func_comma):
    #generating list of ranges to protect
    zipped_list = list(zip(func_bps,func_comma))
    ranges2protect = list()
    i=0
    for func, fcommas in zipped_list:
        i=0
        mini_r2p=list()
        for fcomma in fcommas:
            if (len(fcommas)-i)>1:
                # print(expr[fcommas[i]+1:fcommas[i+1]])
                mini_r2p.append([fcommas[i]+1, fcommas[i+1]])
            else:
                # print(expr[fcomma+1:func[1]])
                mini_r2p.append([fcomma+1,func[1]])
            i+=1
        ranges2protect.append(mini_r2p)
    return ranges2protect

def gen_protect_zones_copy(expr, ranges2protect):
    protect_zones_copy = list()
    for a in ranges2protect:
        for b in a:
            # print(expr[b[0]:b[1]])
            protect_zones_copy.append(expr[b[0]:b[1]])
    return protect_zones_copy

def gen_protect_zones(expr, func_list):
    protect_zones = list()
    for func in func_list:
        sorted_bracket_pairs = gen_sorted_bracket_pairs(expr)
        func_bps = gen_func_bps(func, expr, sorted_bracket_pairs)
        func_sub_bps = gen_func_sub_bps(func_bps,sorted_bracket_pairs)
        func_commas = gen_func_commas(expr, func_bps, func_sub_bps)
        ranges2protect = gen_ranges2protect(func_bps, func_commas)
        func_protect_zones = gen_protect_zones_copy(expr, ranges2protect)
        protect_zones = protect_zones + func_protect_zones
    return protect_zones

def gen_replace_zones(expr, func_list):
    replace_zones = list()
    for func in func_list:
        sorted_bracket_pairs = gen_sorted_bracket_pairs(expr)
        func_bps = gen_func_bps(func, expr, sorted_bracket_pairs)
        func_sub_bps = gen_func_sub_bps(func_bps,sorted_bracket_pairs)
        func_commas = gen_func_commas(expr, func_bps, func_sub_bps)
        ranges2replace = gen_ranges2protect(func_bps, func_commas)
        replace_zones = replace_zones + ranges2replace

    replace_zones_copy = list()
    for a in replace_zones:
        for b in a:
            # print(expr[b[0]:b[1]])
            replace_zones_copy.append([b[0],b[1]])
    return replace_zones_copy

def stringMutation(old, new, replacement_range):
    #slice into 3 parts
    pre = old[:replacement_range[0]]
    cen = old[replacement_range[0]:replacement_range[1]]
    suf = old[replacement_range[1]:]
    return pre + new + suf

def preSympifySub(expr,**kwargs):
    """
    Designed this as a reponse to the fact that sympify evaluates expressions when performed and therefore would integrate and/or differentiate before I would have a chance to perform substitution.
    Usage:
        preSympifySub(r'Eq(v, L*diff(i,t))',i="10*t*exp(-5*t)")
    """

    for k,v in kwargs.items():
        v=str(v)

    protect_zones = gen_protect_zones(expr, ["integrate", "diff"])
    protect_zones.reverse()

    for k,v in kwargs.items():
        regex = rf'(?<!\w|\d){k}(?!\w|\d)'
        expr = sub(regex,rf"({str(v)})",str(expr))

    undue_replaced_zones = gen_replace_zones(expr, ["integrate", "diff"])
    undue_replaced_zones.reverse()

    for protect, replaced in list(zip(protect_zones, undue_replaced_zones)):
        # expr = expr.replace(replaced,protect)
        expr = stringMutation(expr,protect,replaced)

    return expr

expr = 'eq.append("Eq(w,integrate(C*v,(v,v0,v1))-integrate(C*v,(v,v0,v1))+integrate(8*diff(v**2,v),(v,v0,vt), (v4,f3)))")'
# expr = 'eq.append("Eq(w,integrate(C*v,(v,v0,v1)'
protect_zones = gen_protect_zones(expr, ["integrate", "diff"])
print(protect_zones)

from re import sub
print(expr)
expr_new = preSympifySub(expr,v="99*red_ballons")
print(expr_new)

# gen_replace_zones(expr, ["integrate", "diff"])