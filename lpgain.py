def tolerance(win, loss):
    for i in range (100, 0, -1):
        print(i)
        if(win * i - loss * (100 - i) < 0):
            return i + 1 
    return 0
def main():
   win = input("Enter LP for a win:")
   loss = input("Enter LP for a loss")
   print(win, loss)
   result = tolerance(win, loss)
   if(result == 0):
       print("Enter proper values")
   else:
       print("You will have positive gains with a:", result , " % win rate")
   return
if __name__ == "__main__":
    main()