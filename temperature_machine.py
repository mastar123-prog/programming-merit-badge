def convert_temperature():
    try:
        val = float(input("Enter temperature value: "))
        in_unit = input("Enter current unit (C, F, K): ").upper()
        out_unit = input("Enter target unit (C, F, K): ").upper()

        units = ['C', 'F', 'K']
        if in_unit not in units or out_unit not in units:
            raise ValueError("Invalid unit entered. Use C, F, or K.")

        if in_unit == 'C':
            celsius = val
        elif in_unit == 'F':
            celsius = (val - 32) * 5/9
        else:
            celsius = val - 273.15

        if out_unit == 'C':
            result = celsius
        elif out_unit == 'F':
            result = (celsius * 9/5) + 32
        else:
            result = celsius + 273.15

        print(f"{val}{in_unit} is equal to {result:.2f}{out_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_temperature()
