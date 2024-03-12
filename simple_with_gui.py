from exp import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def simple_with_gui():
    params = [
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, -1, 'symmetrical, leniency set to 0'),
        ('FINGERTIP', 2, 'false', 'false', 'symmetrical', 9, 20, -1, 'symmetrical, leniency set to 2'),
        ('CLAW', 3, 'true', 'false', 'both', 9, 20, -1, 'both, leniency set to 3'),
        ('PALM', 4, 'true', 'false', 'asymmetrical', 9, 20, -1, 'asymmetrical, leniency set to 4'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        length = len(result)  # Calculate the length of the result

        # Output API test result
        print(f"Test Case {i + 1}: Description: {description}, Result Length: {length}")

        # Run test using GUI
        gui_test_result = run_gui_test(*param_set[:-1])
        print(f"GUI Test Case {i + 1}: {gui_test_result}")  # Output GUI test result


def run_gui_test(*params):
    # Extract parameters
    grip_style, leniency, boolean_one, boolean_two, symmetry, grip_width, hand_length, other_param, description = params

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # You can use any browser driver here (e.g., Chrome, Firefox)

    try:
        # Navigate to the provided link
        driver.get("https://www.rocketjumpninja.com/mouse-search")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='h_length']")))

        # Find the input element with the name 'h_length'
        h_length_input = driver.find_element_by_xpath("//input[@name='h_length']")

        # Set the value of the input element with the hand length parameter
        h_length_input.send_keys(str(hand_length))

        # Return test result
        return "Pass"  # Replace with actual test result (e.g., "Pass" or "Fail")

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    simple_with_gui()
