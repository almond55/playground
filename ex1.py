def validate(rules, data):
    retdata = { 'ok': [],
                'not_ok': []}
    for x in data:
        if x in rules and type(data[x]) is rules[x]:
            retdata['ok'].append('%s: %s' % (x, data[x]))
        else:
            retdata['not_ok'].append('%s: %s' % (x, data[x]))

    return retdata

data = {'name': 'Aman',
        'year': 1982,
        'hobbies': ['painting','reading',],
        'cash_balance': 0.45,
        'resolution': {'this_year': 'Be RICH!',}
       }
        
rules = {'year': int, 'hobbies': list, 'name': str}
test = validate(rules, data)
print('Ok data = %s' % test['ok'])
print('Bad data = %s' % test['not_ok'])
