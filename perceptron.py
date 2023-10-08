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


