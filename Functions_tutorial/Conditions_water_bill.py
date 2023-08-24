def get_water_bill(num_gallons):
    bill = 1
    if num_gallons <= 8000:
        bill = (num_gallons / 1000) * 5
    elif num_gallons >= 8001:
        bill = (num_gallons / 1000) * 6
    elif num_gallons >= 22001:
        bill = (num_gallons / 1000) * 7
    elif num_gallons >= 30001:
        bill = (num_gallons / 1000) * 10

    return bill


print(get_water_bill(23000))
