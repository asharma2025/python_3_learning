# Define variables
weight = 5.5
ground_shipping_premium = 125.00

# Ground shipping
if weight <= 2:
  ground_cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  ground_cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  ground_cost = weight * 4.00 + 20.00
else:
  ground_cost = weight * 4.75 + 20.00

# Drone shipping
if weight <= 2:
   drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12.00
else:
  drone_cost = weight * 14.25 

print("Ground Shipping Cost: $", ground_cost)
print("Ground Shipping Premium: $", ground_shipping_premium)

print("Drone Shipping Cost: $", drone_cost)