
company_eployees = {}

while True:
    input_line = input()
    if input_line == 'End':
        break

    company_name, employee_id = input_line.split(' -> ')

    if company_name in company_eployees:
        if not employee_id in company_eployees.get(company_name):
            company_eployees[company_name].append(employee_id)
    else:
        company_eployees[company_name] = [employee_id]

for company_name in company_eployees.keys():
    formated_list = [f'-- {emp_id}' for emp_id in company_eployees.get(company_name)]
    print(company_name)
    print(*formated_list, sep='\n')