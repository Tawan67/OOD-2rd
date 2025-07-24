print("Enter your High and Weight : ",end="")
high,weight = map(float,(input().split(" ")))
# print(high,weight)

BMI = weight / (high**2)
# print(BMI)
if BMI < 18.50 :
    print("Less Weight")
elif 18.50 <= BMI  < 23 :
    print("Normal Weight")
elif 23 <= BMI  < 25:
    print("More than Normal Weight")
elif 25 <= BMI  < 30:
    print("Getting Fat")
elif BMI  >= 30:
    print("Fat")