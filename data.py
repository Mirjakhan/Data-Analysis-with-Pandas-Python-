import pandas as pd

def analyze_data():
    # Load the dataset
    data = pd.read_csv('data.csv')

    # Display the first few rows of the dataset
    print("First 5 rows of the dataset:")
    print(data.head())

    # Basic statistics
    print("\nBasic statistics:")
    print(data.describe())

    # Count of unique values in a specific column
    print("\nCount of unique values in 'column_name':")
    print(data['column_name'].value_counts())

    # Data visualization (requires matplotlib)
    import matplotlib.pyplot as plt

    data['column_name'].value_counts().plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Value Counts of column_name')
    plt.show()

if __name__ == "__main__":
    analyze_data()
