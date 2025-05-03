
def main() -> None:
    print("Welcome to the tip calculator")
    total_bill = float(input("What was the total bill? $ "))
    tip_list_perc = [10, 12, 15]
    chosen_tip = int(input("How high tip you want to give? 10, 12, or 15? "))
    ppl_number = int(input("How many people are in the group? "))
    if chosen_tip in tip_list_perc:
        meal_cost = chosen_tip * total_bill * 0.01 + total_bill
        print(f"The total cost of the meal was {meal_cost} but divided by\n{ppl_number} ppl so your cost would be: {meal_cost/ppl_number}$")
    else:
        print("you need to choose the tip value from the list")




if __name__ == "__main__":
    main()