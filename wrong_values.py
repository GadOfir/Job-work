from exp import main
import re

def test_wrong_values_empty_response():
    params = [
        ('CLAW', 0, 'false', 'false', 'xboth', 9, 20, -2, 'Width leniency 0'),
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, -2, 'Width leniency 0'),

        # Add more test cases here as needed
    ]
    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        if param_set[4] != 'both' and param_set[4] != 'symmetrical' and param_set[4] != 'asymmetrical':
            print("Shape input issue ,it is " + param_set[4])
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i + 1}")  # Get the name value
            if param_set[4] == 'both' or param_set[4] == 'symmetrical' or param_set[4] == 'asymmetrical':
                print("no Shape input issue with " + result[key].get('Name') + "it is " + param_set[4])
        print('--------------------------')


if __name__ == "__main__":
    test_wrong_values_empty_response()
