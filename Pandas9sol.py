#511. Game Play Analysis I
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range(len(activity)):
        p_id = activity['player_id'][i]
        e_date = activity['event_date'][i]
        if p_id in mydictionary:
            if e_date < mydictionary[p_id]:
                mydictionary[p_id] = e_date
        else:
            mydictionary[p_id] = e_date
    
    result = []
    for key, value in mydictionary.items():
        result.append([key, value])
    
    return pd.DataFrame(result, columns=['player_id', 'first_login'])

#Efficient way
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(['player_id']) ['event_date'].min().reset_index()
    return df.rename(columns = {'event_date': 'first_login'})


import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by=['event_date']).drop_duplicates(['player_id'])
    return df[['player_id', 'event_date']].rename(columns = {'event_date':'first_login'})


#586. Customer Placing the Largest Number of Orders
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range(len(orders)):
        c_number = orders['customer_number'][i]  # Extract the customer number from the DataFrame
        if c_number not in mydictionary:
            mydictionary[c_number] = 0
        mydictionary[c_number] += 1  # Increment the count for the customer number
    
    if not mydictionary:  # Check if the dictionary is empty
        return pd.DataFrame(columns=['customer_number'])  # Return an empty DataFrame
    
    Max = max(mydictionary.values())  # Find the maximum count
    
    result = []
    for key, value in mydictionary.items():
        if value == Max:  # Check if the count matches the maximum count
            result.append([key])
    
    return pd.DataFrame(result, columns=['customer_number'])

#Alternative
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(['customer_number']).size().reset_index(name='count')
    df.sort_values(by='count', ascending=False, inplace=True)
    
    if len(df) == 0:
        return pd.DataFrame(columns=['customer_number'])  # Return an empty DataFrame
    
    return pd.DataFrame([df.iloc[0]['customer_number']], columns=['customer_number'])

#using mode()
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    mode_customer_numbers = orders['customer_number'].mode()
    
    if mode_customer_numbers.empty:
        return pd.DataFrame(columns=['customer_number'])  # Return an empty DataFrame
    
    return pd.DataFrame({'customer_number': mode_customer_numbers})





