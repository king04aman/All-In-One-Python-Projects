def grp_split():

    """
    This function takes in the number of members in the group, and their contribution amount 
    along with their names.
    It gives the total amount contributed by the group, the amount of equal 
    contribution for each group member and whether any group memebr(s) owes/owe any amount to other group member(s).

    """

    chk1 = input("Add Group members? Y/N :").lower()
    if chk1.lower() == 'y':
        curr = input("Enter Currency : ")
        num = int(input("\nTotal number of members in group : "))
        assert num>1, "\033[91mNumber of group members should be greater than 1\033[0m"
        names = []
        amt = []
        for i in range(num):
            print(f"\nMember {i+1} :-")
            n = input("Name : ")
            assert n!='', "\033[91mName cannot be blank\033[0m"
            names.append(n)
            a = float(input(f"Amount Contributed : {curr}"))
            assert a!='', "\033[91mAmount cannot be blank\033[0m"
            assert a>=0.0, f"\033[91mAmount should be {curr} 0 or more\033[0m"
            amt.append(a)
        contribute = sum(amt)/len(amt)
        print(f"\nTotal contribution of each group member is : {curr} {contribute: .2f}")
        for j in range(num):
            if amt[j] < contribute:
                give = (contribute - amt[j])/(num-1)
                print(f"\n{names[j]} owes Rs. {give: .2f} to all other members of the group.")
            elif amt[j] > contribute:
                take = (amt[j] - contribute)/(num-1)
                print(f"\nAll other members of group owe Rs. {take: .2f} to {names[j]}.")
            else:
                pass
    else:
        pass

def main():
    grp_split()

if __name__=='__main__':
    main()
