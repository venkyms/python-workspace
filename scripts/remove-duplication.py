def remove_duplicates(countries_list):
    """
    Remove duplicates from the countries list
    :param countries_list: list of countries
    :return: return list of unique countries
    """
    # match_found = False
    unique_countries_list = []
    for country in countries_list:
        if country not in unique_countries_list:
            unique_countries_list.append(country)
        # for unique_country in unique_countries_list:
        #     if country == unique_country:
        #         match_found = True
        #         break
        # if not match_found:
        #     unique_countries_list.append(country)
    return unique_countries_list


initial_countries_list = ['Angola', 'Maldives', 'United States', 'India']
final_countries_list = remove_duplicates(initial_countries_list)
print("initial_countries_list:{}".format(len(initial_countries_list)))
print("final_countries_list:{}".format(len(final_countries_list)))

initial_countries_list1 = ['Angola', 'Maldives', 'India', 'United States', 'India']
final_countries_list1 = remove_duplicates(initial_countries_list1)
print("initial_countries_list1:{}".format(len(initial_countries_list)))
print("final_countries_list1:{}".format(len(final_countries_list)))
