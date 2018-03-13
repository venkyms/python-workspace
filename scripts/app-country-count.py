from scripts.countries import country_list  # Note: since the list is so large, it's tidier

# to put in in a separate file. We'll learn more
# about "import" later on.

country_counts = {}
for country in country_list:
    country_counts[country] = country_list.count(country)

print(country_counts)

# todo: insert countries into the country_count dict.
# If the country isn't in the dict already, add it and set the value to 1
# If the country is in the dict, increment its value by one to keep count
