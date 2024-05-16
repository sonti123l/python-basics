def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60

def main():
    time_str = input("Whaat time is it? ")
    time = convert(time_str)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()

