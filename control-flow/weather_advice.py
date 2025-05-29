#step1:prompt user for weather input.
 
weather=input("What's the weather like today(sunny/rainy/cold): ").lower()

# provide clothing recommendations based on user input
if weather=="sunny":
     print("wear a t-shirt and sunglasses.")
elif weather=="rainy":
     print("dont forget your umbrella and a raincoat.")
elif weather=="cold":
       print("Make sure to wear a warm coat and a scarf.")
else:
      print("Sorry, i don't have recommendations for this weather.")
      
