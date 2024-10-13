words = ['courtyard', 'alley', 'landlady', 'landlord', 'tenant', 'stairs', 'fire escape', 'trash bin', 'hallway', 'balcony', 'doorknob',  'peephole', 'elevator', 'lobby', 'door chain', 'realtor']
Ddict = {}
for x in words:
    if not (len(x) in Ddict):
        Ddict[len(x)] = [x]
    else:
        Ddict[len(x)].append(x)

for item in Ddict.items():
    print("[{}] words of length {} -> {}".format(len(item[1]), item[0], item[1]))
