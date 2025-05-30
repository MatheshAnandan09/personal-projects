#

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('pokemon',['abc', 'efg', 'ghi'], align= 'c')
table.add_column('power', ['electric', 'water', 'fire'])
print(table)