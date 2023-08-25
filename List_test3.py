"""
Calcula o crescimento do site
comparando com os anos anteriores
"""


def percentage_growth(num_users, yrs_ago):
    growth = ((num_users[len(num_users) - 1] - num_users[len(num_users) - yrs_ago - 1])
              / num_users[len(num_users) - yrs_ago - 1])
    return growth


num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
print(percentage_growth(num_users_test, 1))
