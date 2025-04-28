def main():
    C = 299792458

    while True:
        try:
            user_input = input("Enter kilos of mass (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting the program.")
                break

            mass = float(user_input)

            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")

            energy = mass * C**2
            print(f"\n{energy} joules of energy!\n")

        except ValueError:
            print("Please enter a valid number for mass or 'q' to quit.\n")


if __name__ == '__main__':
    main()
