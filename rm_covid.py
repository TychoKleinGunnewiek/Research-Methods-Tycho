import json
import sys

# the link to the data set used in this program is the following:
# https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data.
# on this page you will have to scroll down and use the JSON version of the dataset
# this dataset must be downloaded and stored in the same directory as this python file
# is in. in order for it to work, the name of the JSON file must be given as an argument.
# when running this python file in your shell.


def records_separator(covid_file):
    ''' this function takes a json data containing all the cases of
    covid infected cases and deaths + other meta data from everyday
    since 2019 december 31 from all countries in the world.
    opens the file and extracts the records from the Netherlands and Italy
    and puts them in a list of all the records linked to that country '''

    with open(covid_file, 'r') as covid_file:
        data = json.load(covid_file)

    netherlands_records = []
    italy_records = []
    for record in data["records"]:
        for k, v in record.items():
            if v == "Netherlands":
                netherlands_records.append(record)
            elif v == "Italy":
                italy_records.append(record)
    return netherlands_records, italy_records


def death_ratio(nl_ita):
    """ the first part of this function takes the nl and ita records lists as
    inputs and uses them to extract the amount of cases and deaths from
    everyday to seperate them from the other meta-data. Putting them
    in two lists, one containing the netherlands cases and deaths
    and one containing the Italy cases and deaths from every day.
    """
    nl, ita = nl_ita
    nl_case_death_list = [(int(record["cases"]),int(record["deaths"])) for record in nl if int(record["cases"]) != 0]
    ita_case_death_list = [(int(record["cases"]),int(record["deaths"])) for record in ita if int(record["cases"]) != 0]

    """ the second part of this function uses the case_death_list of 
    NL and Ita to calculate the death-ratio of both countries in the
    20 days with the most cases. using a simple formula of amount of 
    deaths divided by the amount of cases in those 20 days. and prints
    the death-ratio caused by Covid-19 in percentage for both countries """

    # average death-ratio netherlands
    old_case = 0
    old_death = 0
    for cases, deaths in sorted(nl_case_death_list):
        cases += old_case
        deaths += old_death
        old_case = cases
        old_death = deaths
    print(70 * "-")
    print("Average death-ratio from the Netherlands caused by Covid-19:")
    print('{0:0.2f} %\n'.format((deaths / cases * 100)))

    # average death-ratio Italy
    old_case = 0
    old_death = 0
    for cases, deaths in sorted(ita_case_death_list):
        cases += old_case
        deaths += old_death
        old_case = cases
        old_death = deaths
    print("Average death-ratio from Italy caused by Covid-19:")
    print('{0:0.2f} %'.format((deaths / cases * 100)))

    # death-ratio Netherlands first 30 days
    old_case = 0
    old_death = 0
    for cases, deaths in nl_case_death_list[-31:-1]:
        cases += old_case
        deaths += old_death
        old_case = cases
        old_death = deaths
    print(70 * "-")
    print("death-ratio in the first 30 days ")
    print("after the first detected Covid-19 case in the Netherlands:")
    print('{0:0.2f} %\n'.format((deaths / cases * 100)))

    # death-ratio Italy first 30 days
    old_case = 0
    old_death = 0
    for cases, deaths in ita_case_death_list[-31:-1]:
        cases += old_case
        deaths += old_death
        old_case = cases
        old_death = deaths
    print("death-ratio in the first 30 days")
    print("after the first detected Covid-19 case in Italy:")
    print('{0:0.2f} %'.format((deaths / cases * 100)))

    # average death-ratio Netherlands for the 30 days with the most cases
    old_case = 0
    old_death = 0
    for cases, deaths in sorted(nl_case_death_list)[-31:-1]:
        cases += old_case
        deaths += old_death
        old_case = cases
        old_death = deaths
    print(70 * "-")
    print("death-ratio in the 30 days ")
    print("with the most COVID-19 cases in the Netherlands:")
    print('{0:0.2f} %\n'.format((deaths / cases * 100)))

    # average death-ratio Italy for the 30 days with the most cases
    old_case = 0
    old_death = 0
    for cases, deaths in sorted(ita_case_death_list)[-31:-1]:
        cases += old_case
        deaths += old_death
        old_case = cases
        old_death = deaths
    print("death-ratio in the 30 days ")
    print("with the most COVID-19 cases in Italy:")
    print('{0:0.2f} %'.format((deaths / cases * 100)))
    print(70 * "-")


def main(data_file):
    death_ratio(records_separator(data_file))

if __name__ == "__main__":
    main(sys.argv[1])

