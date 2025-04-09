def describe_school(school, county= 'Wicomico'):
    """Prints school and county"""
    print(f"{school} is in {county} County.")
    #print statement for school and county

describe_school('Parkside')
describe_school('Bennett')
describe_school('Snow Hill', 'Worcester')
#function calls passing school and county arguments