import math

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    horizontal_diff = x2 - x1
    vertical_diff = y2 - y1
    
    # Apply the Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
    distance = math.sqrt(horizontal_diff**2 + vertical_diff**2)
    return distance

if __name__ == "__main__":
    print("--- 2D Distance Calculator ---")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    result = calculate_distance(x1, y1, x2, y2)
    print(f"\nThe calculated distance between ({x1}, {y1}) and ({x2}, {y2}) is: {result:.2f}")
