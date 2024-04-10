from datetime import datetime

def convert_date_format(input_date):
    # Parse the input date string
    input_datetime = datetime.strptime(input_date, '%m.%d.%Y')

    # Format the date in the desired format
    output_date = input_datetime.strftime('%Y.%m.%d')

    return output_date

# Example usage
input_date = '12.22.2023'
output_date = convert_date_format(input_date)
print(output_date)