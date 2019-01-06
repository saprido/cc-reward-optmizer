# Create random credit card transactional data
import pandas as pd
import random


def main():
    # List with transactional data
    transactions = []

    # Create 100 transactions
    for x in range(0,1000):
        row_data = create_data(random.randint(0,101))
        transactions.append(row_data)

    # Create data frame from list with named columns
    columns = ['Amount', 'Date', 'Merchant', 'Category', 'Card']
    transactions_df = pd.DataFrame(transactions)
    transactions_df.columns = columns

    # Print first 5 rows of DF
    transactions_df.head()

    # Write DF to csv
    transactions_df.to_csv('sample_transaction_data.csv', index=False)


# Create random transactional data, return list with info
def create_data(num):

    # Categories: Dining, Travel, Entertainment, Shopping, Groceries
    if num < 20:
       return [random.randint(1,50),
               str(random.randint(1,13)) + '/' + str(random.randint(1,29)) + '/2019',
               'Merchant',
               'Dining',
               'My Card']
    elif num < 40:
        return [random.randint(100, 200),
                str(random.randint(1, 13)) + '/' + str(random.randint(1, 29)) + '/2019',
                'Merchant',
                'Travel',
                'My Card']
    elif num < 60:
        return [random.randint(10, 50),
                str(random.randint(1, 13)) + '/' + str(random.randint(1, 29)) + '/2019',
                'Merchant',
                'Entertainment',
                'My Card']
    elif num < 80:
        return [random.randint(1, 200),
                str(random.randint(1, 13)) + '/' + str(random.randint(1, 29)) + '/2019',
                'Merchant',
                'Shopping',
                'My Card']
    else:
        return [random.randint(10, 100),
                str(random.randint(1, 13)) + '/' + str(random.randint(1, 29)) + '/2019',
                'Merchant',
                'Groceries',
                'My Card']

main()