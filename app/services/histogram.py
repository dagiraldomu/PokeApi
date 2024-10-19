import matplotlib.pyplot as plt
import numpy as np

def create_histogram(growth_times):
    plt.figure(figsize=(10, 6))
    plt.hist(growth_times, bins=np.arange(min(growth_times), max(growth_times) + 2), edgecolor='black')
    plt.title('Histogram of Berry Growth Times')
    plt.xlabel('Growth Time')
    plt.ylabel('Frequency')

    # Save the image to a file
    plt.savefig('../static/histogram.png')
    plt.close()

# # Example usage with growth times data
# growth_times = [3, 5, 3, 2]
# create_histogram(growth_times)

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Berry Growth Time Histogram</title>
    <style>
        body {
            font-family: sans-serif;
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        img {
            display: block;
            margin: 0 auto;
            border: 2px solid #ccc;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <h1>Berry Growth Time Histogram</h1>
    <img src="/static/histogram.png" alt="Histogram of Berry Growth Times" width="600">
</body>
</html>
"""
