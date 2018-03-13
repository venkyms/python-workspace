monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


def total_takings(monthly_taking):
    circus_earning_year_list = list(monthly_taking.values())
    print(circus_earning_year_list)

    total_circus_earning_year = 0
    for monthly_earning in circus_earning_year_list:
        total_circus_earning_year += sum(monthly_earning)

    return total_circus_earning_year


print("Yearly earning:{}".format(total_takings(monthly_takings)))

# def total_takings(monthly_takings):
#     #total is used to sum up the monthly takings
#     total = 0
#     for month in monthly_takings.keys():
#         #I use the Python function sum to sum up over
#         #all the elements in a list
#         total = total + sum(monthly_takings[month])
#     return total
