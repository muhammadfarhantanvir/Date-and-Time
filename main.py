import datetime as dt


# Creating a function that will return the nth position
def nth_position(n):
    nth = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
    }
    return nth[n]


# Creating a function that will compare the datetime with current datetime
def compare_date(param_date, i):
    # Creating a variable that will store the current datetime
    current = dt.datetime.now()
    result_str = ""
    if current.strftime("%Y.%m.%d-%H:%M") == param_date:
        result_str = f"The {nth_position(i+1)} date current date ({param_date})"
    elif current.strftime("%Y.%m.%d-%H:%M") > param_date:
        result_str= f"The {nth_position(i+1)} date will be reached! ({param_date})"
    else:
        result_str = f"The {nth_position(i+1)} date has been reached! ({param_date})"

    return result_str


# main function
if __name__ == "__main__":    
    current_datetime = dt.datetime.now()
    # Get n value for running a loop from user input
    n = int(input("How much data do you want to enter? "))
    # Create a list to store data
    data = {}
    # Loop to get data from user
    for i in range(n):
        # get date data from user input
        u_date = input("Please enter a date: ")
        # get time data from user input
        u_time = input("Please enter a time: ")
        data[i] = u_date + "-" + u_time
    # Print the data
    print(data)
    # Check the user input date and time with current datetime that reached or not additionally performed a unit test.
    for i in range(n):
        result = compare_date(data[i], i)
        print(result)
    print("Thank you very much. I will notify them!")
