import re

string_to_check = '''
    280-15-88
    070-01-01
    071-10-10
    060-02-01
'''

my_dict = {
    r'0[1-5]\d-\d\d-\d\d':'Office Supplies',
    r'060-0[0-1]-\d\d':'Industrial Supplies',
    r'060-02-\d\d':'Industrial Supplies',
    r'060-0[3-4]-\d\d':'Facitily Management',
    r'07\d-\d\d-\d\d':'Office Supplies',
    r'080-0[0-3]-\d\d':'Office Supplies',
    r'080-04-\d\d':'Office Supplies',
    r'080-0[5-9]-\d\d':'Office Supplies',
    r'080-10-\d\d':'Office Supplies',
    r'080-11-\d\d':'Facitily Management',
    r'080-1[2-3]-\d\d':'Office Supplies',
    r'080-14-\d\d':'Information Technology',
    r'080-15-\d\d':'Office Supplies',
    r'09\d-\d\d-\d\d':'Office Supplies',
    r'1\d\d-\d\d-\d\d':'Office Supplies',
    r'2[1-3]\d-\d\d-\d\d':'Office Supplies',
    r'240-0[0-5]-\d\d':'Office Supplies',
    r'240-06-\d\d':'Facitily Management',
    r'240-07-\d\d':'Office Supplies',
    r'250-0[0-3]-\d\d':'Office Supplies',
    r'250-04-\d\d':'Information Technology',
    r'250-05-\d\d':'Office Supplies',
    r'250-10-\d\d':'Office Supplies',
    r'260-0[0-1]-\d\d':'Office Supplies',
    r'260-02-\d\d':'Industrial Supplies',
    r'260-0[3-4]-\d\d':'Facitily Management',
    r'260-30-\d\d':'Facitily Management',
    r'280-0[0-3]-\d\d':'Office Supplies',
    r'280-0[4-5]-\d\d':'Information Technology',
    r'280-0[6-9]-\d\d':'Office Supplies',
    r'280-10-\d\d':'Office Supplies',
    r'280-11-\d\d':'Facitily Management',
    r'280-1[2-4]-\d\d':'Office Supplies',
    r'280-1[5-9]-\d\d':'Information Technology',
    r'280-2[0-1]-\d\d':'Office Supplies',
    r'280-22-\d\d':'Information Technology',
    r'280-2[3|5]-\d\d':'Office Supplies',
    r'280-26-\d\d':'Information Technology',
    r'280-30-\d\d':'Information Technology',
}

def classify_commodity_code(my_dict, string_to_check):

    for key, value in my_dict.items():
        pattern = re.compile(str(key))
        matches = pattern.finditer(string_to_check)

        matches_list = []

        for match in matches:
            matches_list.append(match.group(0))

        if len(matches_list) != 0:
            print(value + ' - ' + str(matches_list))


def main():

    classify_commodity_code(my_dict, string_to_check)

if __name__ == '__main__':
    main()
