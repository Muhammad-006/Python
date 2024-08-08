import pandas
import random
import datetime as dt
import smtplib

my_email = 'MuhammadhBilal717@gmail.com'
Password = 'wdhk xwao vryq qhnc'

letter_list = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

birthday_data = pandas.read_csv('birthdays.csv')
date_time = dt.datetime.now()
this_month = date_time.month
this_day = date_time.day
try:
    record = {'Name': row['name']  for index, row in birthday_data.iterrows() if row.month == this_month and row.day == this_day }
    record_data = birthday_data[birthday_data.name == record['Name']]
except:
    print("it is no ones birthday today.")
else:
    with open(random.choice(letter_list)) as letter:
        data_from_letter = letter.read()
        data_from_letter = data_from_letter.replace('[NAME],', record['Name'])
    with smtplib.SMTP('smtp.gmail.com', port = 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = Password)
        connection.sendmail(from_addr = my_email,
                            to_addrs = record_data.email,
                            msg = f'Subject:Congratulations!\n\n{data_from_letter}')




