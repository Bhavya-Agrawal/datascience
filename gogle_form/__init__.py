#!/usr/bin/python3

from flask import Flask,render_template,request
import pandas as pd
import os
import xlsxwriter
app = Flask(__name__)
df=pd.DataFrame(columns=['FirstName'])
@app.route('/',methods=['GET','POST'])
def form_data(): 
    
    if request.method =='POST':
        # initially read data from the excel file to which we need to append further data if the desired file exists
        exists = os.path.exists('pandas.xlsx')

        if exists:
            print('in if part')

            # call insert_data()
            insert_data()
            
        else:
            print('in else part')
            
            # call create_file()
            create_file() 

    return render_template('index.html')             


def insert_data():
    out = pd.read_excel('pandas.xlsx')


    # get data from form
    f_name=request.form['n']
    s_name = request.form['s']
    age = request.form['a']


    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'FirstName': [f_name],'LastName':[s_name],'AGE':[age]})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas.xlsx', engine='xlsxwriter')

    # pass concatenated data from dflist into a variable
    appended_list = pd.concat([out,df])
    
    # pass this appended_list to the excel sheet within the same sheet_name ie 'Sheet1' pass index=0 so 
    #that the data gets inserted from the first column itself
    appended_list.to_excel(writer,sheet_name='Sheet1',index=0)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


# creating an empty xlsx file using xlsxwriter
def create_file():
    workbook = xlsxwriter.Workbook('pandas.xlsx')
    worksheet = workbook.add_worksheet()   
    workbook.close() 
    insert_data()
       

if __name__ == "__main__":
    app.run(debug=True)

