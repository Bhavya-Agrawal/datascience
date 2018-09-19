#!/usr/bin/python3
from flask import Flask,render_template,request
import pandas as pd
import csv
import mysql.connector as mysql

#creating connection with the mariadb database
conn = mysql.connect(user='#####',password='##########',host='127.0.0.1',database='Form')
cursor = conn.cursor()

#checking for the connection
if conn.is_connected():
    print('True')
else:
    print('check ur database connection once')

# define app name
app = Flask(__name__)

#define route
@app.route('/',methods=['GET','POST'])
def webpage():
    if request.method=='POST':
        name=request.form['n']
        age=request.form['a']
        stream=request.form['s']

        #passing entries into the database connected
        cursor.execute(f'insert into data(name,age,stream) VALUES("{name}",{int(age)},"{stream}");')

        conn.commit()
    xl_data()       
    return render_template('index.html')    


def xl_data():
    #entering data into excel file by taking data into csv file first
    cursor.execute("Select * from data")
    out = cursor.fetchall()
    print(out)
    form_data = [['name','age','stream']]
    for i in out:
        form_data.append(list(i))
    # open the file .csv for writing data into it    
    with open('data_input.csv','w') as f:
        example = csv.writer(f)
        example.writerows(form_data)
    # now exporting data from csv file to excel file
    df = pd.read_csv('data_input.csv')
    df.to_excel('data_form.xls')
    return 'data written in excel file successfully'

if __name__ == "__main__":
    app.run(debug=True)
