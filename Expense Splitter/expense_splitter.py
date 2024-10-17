def grp_split():
    chk1 = input("Add Group members? Y/N :")
    if chk1 == 'Y':
        num = int(input("\nTotal number of members in group : "))
        names = []
        amt = []
        for i in range(num):
            n = input("\nName : ")
            a = int(input("Amount Contributed : "))
            names.append(n)
            amt.append(a)
        contribute = sum(amt)/len(amt)
        for j in range(num):
            if amt[j] < contribute:
                give = (contribute - amt[j])/(num-1)
                print(f"\n{names[j]} owes Rs. {give} to all other members of the group.")
            elif amt[j] > contribute:
                take = (amt[j] - contribute)/(num-1)
                print(f"\nAll other members of group owe Rs. {take} to {names[j]}.")
            else:
                pass
    else:
        pass

def main():
    grp_split()

if __name__=='__main__':
    main()
