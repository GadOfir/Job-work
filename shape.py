from exp import main
import re

def shape():
    params = [
        ('CLAW', 1, 'false', 'false', 'symmetrical', 9, 20, -1, 'Wireless false'),
        ('CLAW', 2, 'false', 'false', 'symmetrical', 9, 20, -1, 'Wireless false'),
        ('CLAW', 3, 'true', 'false', 'asymmetrical', 9, 20, -1, 'Wireless true'),
        ('CLAW', 4, 'true', 'false', 'both', 9, 20, -1, 'Wireless true'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i+1}")  # Get the name value
            shape = result[key].get('Shape')  # Use i as the key
            #print(f"Test Case {i+1}: Description: {description}, Name: {issue_name}, Wireless Integrity Result: {wireless_result}")
            pattern = r'Expected Shape: (\w+) \| Actual Shape: (\w+)'
            match = re.search(pattern, shape)
            expected_shpe = match.group(1)
            actual_shpe = match.group(2)

            if expected_shpe != 'both':
                if expected_shpe.lower() != actual_shpe.lower():
                    print(f"Test Case {i + 1}: Description: {description}, Name: {issue_name}, Shape: {shape}")
            else:
                continue

if __name__ == "__main__":
    shape()

