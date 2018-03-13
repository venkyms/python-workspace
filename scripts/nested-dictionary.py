elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}


# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
def update_noble_gas(element_dic, gas_name, is_noble_gas):
    element_detail = element_dic.get(gas_name)
    element_detail['is_noble_gas'] = is_noble_gas

    return element_detail


update_noble_gas(elements, 'hydrogen', False)
update_noble_gas(elements, 'helium', True)

print(elements)
