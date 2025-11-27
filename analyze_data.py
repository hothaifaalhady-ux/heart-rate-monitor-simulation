import pandas as pd
import numpy as np

def analyze_numbers(numbers):
    numbers = np.array(numbers)
    result = {
        "mean": float(np.mean(numbers)),
        "std_dev": float(np.std(numbers)),
        "max": float(np.max(numbers)),
        "min": float(np.min(numbers)),
    }
    return result

if __name__ == "__main__":
    sample = [3, 7, 2, 9, 4]
    print("Sample numbers:", sample)
    print("Analysis:", analyze_numbers(sample))
