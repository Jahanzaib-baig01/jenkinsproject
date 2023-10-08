# x_inputs=[50, 70, 100]
# w_weights=[2, 4, 1]
# threshhold=500
# weighted_sum=0
# for x,w in zip(x_inputs,w_weights):
#     items=x*w
#     weighted_sum = weighted_sum + items
# print(f"Total: {weighted_sum}")
# remaining = threshhold - weighted_sum 
# if weighted_sum <= threshhold:
#     print(f"{weighted_sum:} is in our budget! We got {w_weights[0]} Chips, {w_weights[1]} Sandwiches, {w_weights[2]} Coke and Rs.{remaining} left")
# else:
#     print(f"{weighted_sum:} out of budget!")

import random

x_inputs = [50, 70, 100]
threshold = 500
w_weights = []
weighted_sum = 0
remainder = 500

while (remainder >= 40 and weighted_sum < threshold) or ((remainder >= 40 or remainder < 0)):
    weighted_sum = 0
    for x in x_inputs:
        w = random.randint(1, 5)  
        w_weights.append(w)
        weighted_sum += x * w
    remainder=threshold-weighted_sum

print(remainder)


print("Randomly generated weights:")

for i, w in enumerate(w_weights):
    print(f"Weight for x{i + 1}: {w}")

print(f"Total: {weighted_sum}")

def step(value):
    return 1 if value <= threshold else 0

output = step(weighted_sum)
if output == 1:
    print(f"The perceptron output is 1: The items are in our budget!")
else:
    print(f"The perceptron output is 0: The items are out of budget!")


