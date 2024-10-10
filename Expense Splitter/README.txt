# Expense Splitter

This interactive python script implements a unique ‘Expense Splitter’ functionality. 

The user can add the amount contributed by every group member with their name, along with the currency in which the user expects the calculation to be performed. 

The script, after its calculations, gives information about :

- Total Amount contributed by the group as a whole
- Total amount of contribution for each group member
- The amount which any of the group member(s) owe to any other group member(s).

Additional functionality is provided, which include detecting the following errors :

- Blank value for name of group member
- Blank value for amount contributed by any group member
- Contributed amount being negative

All these errors are also modified to be displayed in red colour using ANSI escape sequences for coloured text.