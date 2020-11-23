import json

emps = []


def read_records():
    global emps
    global data
    with open("emp.json") as json_file:
        data = json.load(json_file)
        emps = data['Employees']
        print(emps)

def correct_types():
    for e in emps:
        e['age'] = int(e['age'])

def find_avg_age():
    avg_age = sum([x['age'] for x in emps]) / len(emps)
    return avg_age


def find_avg_age_dept(dept):
    emps1 = []
    for i in emps:
        if i['dept'] == dept:
            emps1.append(i)
    print(emps1)
    avg_age = sum([s["age"] for s in emps1]) / len(emps1)
    return avg_age


def main():
    read_records()
    correct_types()
    print("Average emp age is:", find_avg_age())
    print("Average emp age for dept d1:", find_avg_age_dept("d1"))
    print("Average emp age for dept d2:", find_avg_age_dept("d2"))


if __name__ == "__main__":
    main()

