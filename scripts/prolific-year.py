Beatles_Discography = {'Rubber Soul': 1965, 'Magical Mystery Tour': 1967, "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                       'Revolver': 1966, 'The Beatles': 1968, 'With the Beatles': 1963, 'Beatles for Sale': 1964,
                       'Yellow Submarine': 1969, "A Hard Day's Night": 1964, 'Help': 1965, 'Let It Be': 1970,
                       'Abbey Road': 1969, 'Twist and Shout': 1964, 'Please Please Me': 1963}


def most_prolific(beatles_discography):
    release_years_list = list(beatles_discography.values()) # get the list of years from beatles_discography
    year_count_dic = {}
    for year in release_years_list:      # generate dictionary with year and count
        year_count_dic[year] = release_years_list.count(year)

    year_count_list = list(year_count_dic.values())

    max_release = max(year_count_list) # find max release for the year

    prolific_year = []
    for release_year in year_count_dic: # generate list of years which has max release
        if year_count_dic[release_year] == max_release:
            prolific_year.append(release_year)

    if len(prolific_year) == 1:
        return prolific_year[0]
    else:
        return prolific_year


print("List of Prolific year:{}".format(most_prolific(Beatles_Discography)))



# def most_prolific(discs):
#     #We will store a dictionary of years
#     #and number of albums per year
#     years = {}
#     maxyears = []
#     maxnumber = 0
#     for disc in discs:
#         year = discs[disc]
#         if year in years:
#             years[year] += 1
#         else:
#             years[year] = 1
#
#         #find the year in which the maximum
#     #number of albums was published
#     #there are more elegant ways of accomplishing this,
#     #but the code below works
#     for year in years:
#         if years[year] > maxnumber:
#             maxyears=[]
#             maxyears.append(year)
#             maxnumber = years[year]
#         elif years[year] == maxnumber and not (year in maxyears):
#             maxyears.append(year)
#     if (len(maxyears) == 1):
#         return maxyears[0]
#     else:
#         return maxyears