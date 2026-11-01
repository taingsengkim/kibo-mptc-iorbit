import random
battery = 100.0
for waypoint in range(1, 11):
    consumption = random.uniform(1.5, 3.5)
    battery -= consumption

    print(f"Waypoint {waypoint}: Battery = {battery:.2f}%")

    # Check battery level
    if battery < 80:
        print("[CAUTION] Battery is below 80%!")

    # Emergency return condition
    if battery < 75:
        print("[EMERGENCY RETURN TRIGGERED]")
        break

print("Flight simulation ended.")