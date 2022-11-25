from bacagrammar import cekTerminal, cekVariables

def CFGtoCNF(CFG):
    l_head = list(CFG.keys())
    l_body = list(CFG.values())
    ss = l_head[0]
    addRule = False

    for rules in l_body:
        for rule in rules:
            if ss in rule:
                addRule = True
                break
        if addRule:
            break

    if addRule:
        newRule = {"START" : [[ss]]}
        newRule.update(CFG)
        CFG = newRule
        
    contain = True

    while contain:
        unit_product = {}
        contain = False
        
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and cekVariables(rule[0]):
                    contain = True
                    if head not in unit_product.keys():
                        unit_product[head] = [[rule[0]]]
                    else:
                        unit_product[head].append([rule[0]])

        for head_units, body_units in unit_product.items():
            for rule_units in body_units:
                for head, body in CFG.items():
                    if len(rule_units) == 1 and head == rule_units[0]:
                        newRule = {head_units : body}
                        if head_units not in CFG.keys():
                            CFG[head_units] = body
                        else:
                            for rule in body:
                                if rule not in CFG[head_units]:
                                    CFG[head_units].append(rule)
    
        for head_units, body_units in unit_product.items():
            for rule_units in body_units:
                if len(rule_units) == 1:
                    CFG[head_units].remove(rule_units)

    new_productions = {}
    del_productions = {}
    i = 0
    for head, body in CFG.items():
        for rule in body:
            head_symbol = head
            temp_rule = [r for r in rule]
            if len(temp_rule) > 2:
                while len(temp_rule) > 2:
                    new_symbol = f"X{i}"
                    if head_symbol not in new_productions.keys():
                        new_productions[head_symbol] = [[temp_rule[0], new_symbol]]
                    else:
                        new_productions[head_symbol].append([temp_rule[0], new_symbol])
                    head_symbol = new_symbol
                    temp_rule.remove(temp_rule[0])
                    i += 1
                else:
                    if head_symbol not in new_productions.keys():
                        new_productions[head_symbol] = [temp_rule]
                    else:
                        new_productions[head_symbol].append(temp_rule)
                    
                    if head not in del_productions.keys():
                        del_productions[head] = [rule]
                    else:
                        del_productions[head].append(rule)

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    new_productions = {}
    del_productions = {}

    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and cekTerminal(rule[0]) and cekTerminal(rule[1]):
                new_symbol_Y = f"Y{j}"
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, new_symbol_Z]]
                else:
                    new_productions[head].append([new_symbol_Y, new_symbol_Z])
                    
                new_productions[new_symbol_Y] = [[rule[0]]]
                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and cekTerminal(rule[0]):
                new_symbol_Y = f"Y{j}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, rule[1]]]
                else:
                    new_productions[head].append([new_symbol_Y, rule[1]])

                new_productions[new_symbol_Y] = [[rule[0]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1

            elif len(rule) == 2 and cekTerminal(rule[1]):
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[rule[0], new_symbol_Z]]
                else:
                    new_productions[head].append([rule[0], new_symbol_Z])

                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                k += 1

            else:
                pass

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    return CFG