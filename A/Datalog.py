from tabulate import tabulate


assembly = [
    ("trike", "wheel", "contains", 3),
    ("trike", "seat", "contains", 1),
    ("trike", "pedal", "contains", 2),
    ("wheel", "rim", "component", 1),
    ("wheel", "tube", "component", 1),
    ("pedal", "spoke", "component", 10),
    ("seat", "cushion", "component", 1)
]

def components():
    components_dict = {}

    for part, subpart, rule_type, qty in assembly:
        if (part, subpart) not in components_dict:
            components_dict[(part, subpart)] = {'quantity': qty}
        else:
            if rule_type == 'contains':
                components_dict[(part, subpart)]['quantity'] += qty

    return components_dict

components_relation = components()

components_data = []
for component, info in components_relation.items():
    part, subpart = component
    quantity = info['quantity']
    components_data.append([part, subpart, quantity])

print("Components Relation:")
print(tabulate(components_data, headers=['Part', 'Subpart', 'Quantity'], tablefmt='grid'))

target_part = 'trike'
target_components_data = []
for component, info in components_relation.items():
    part, subpart = component
    if part == target_part:
        quantity = info['quantity']
        target_components_data.append([part, subpart, quantity])

print(f"\nComponents of '{target_part}':")
print(tabulate(target_components_data, headers=['Part', 'Subpart', 'Quantity'], tablefmt='grid'))
