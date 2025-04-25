electrons = int(input())
filed_shells = []
counter_of_shells = 0
while electrons > 0:
    counter_of_shells += 1
    current_filing_of_shells = 2 * counter_of_shells ** 2
    if electrons >= current_filing_of_shells:
        filed_shells.append(current_filing_of_shells)
        electrons -= current_filing_of_shells
    else:
        filed_shells.append(electrons)
        electrons -= electrons
print(filed_shells)

