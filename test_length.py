from exp import main
import re



def test_length():
    params = [
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, 5, 'Width leniency 0'),
        ('CLAW', 1, 'false', 'false', 'both', 9, 20, 5, 'Width leniency 1'),
        ('CLAW', 2, 'false', 'false', 'both', 9, 20, 5, 'Width leniency 2'),
        ('CLAW', 3, 'false', 'false', 'both', 9, 20, 5, 'Width leniency 3'),
        ('CLAW', 4, 'false', 'false', 'both', 9, 20, 5, 'Width leniency 4'),
        # Add more test cases here as needed
    ]
    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i+1}")  # Get the name value
            length = result[key].get('Length')  # Extract grip_width instead of wireless_result
            print(f"Test Case {i+1}: Description: {description}, Name: {issue_name}, length: {length}")


if __name__ == "__main__":

    test_length()
