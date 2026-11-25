
def calculate_bill(connection_type, units):
    if connection_type == "domestic":
        base, extra, fixed = 3, 5, 50
    elif connection_type == "commercial":
        base, extra, fixed = 6, 8, 100
    elif connection_type == "industrial":
        base, extra, fixed = 8, 10, 200
    else:
        return None

    if units <= 100:
        return fixed + units * base

    return fixed + 100 * base + (units - 100) * extra


def main():
    name = input("Consumer name: ")
    meter = input("Meter number: ")
    connection_type = input("Connection type (domestic/commercial/industrial): ").lower()
    units = int(input("Units consumed: "))

    bill = calculate_bill(connection_type, units)

    if bill is None:
        print("Invalid connection type")
    else:
        print("\n----- Electricity Bill -----")
        print("Consumer name:", name)
        print("Meter number:", meter)
        print("Connection type:", connection_type)
        print("Units consumed:", units)
        print("Total bill amount: Rs.", bill)


if __name__ == "__main__":
    main()
