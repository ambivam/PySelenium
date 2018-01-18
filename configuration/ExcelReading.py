import xlrd
import os
from data import xpmsdata
import json

class ExcelOperations:

    def getExecutionList(self):
        executionList = []
        try:
            excelFile = os.path.abspath(__file__ +"/../../data/ExcelData") +"/"+ xpmsdata.TestSuiteExcel
            print("Excelfile path is:",excelFile)
            result_data = []

            workbook = xlrd.open_workbook(excelFile)
            worksheet = workbook.sheet_by_name("TestSuite") # We need to read the data
            num_rows = worksheet.nrows  #Number of Rows
            num_cols = worksheet.ncols  #Number of Columns
            #**********************************************
            for curr_row in range(0, num_rows, 1):
                row_data = []
                for curr_col in range(0, num_cols, 1):
                    data = worksheet.cell_value(curr_row, curr_col)  # Read the data in the current cell
                    # print(data)
                    row_data.append(data)
                result_data.append(row_data)
            #**********************************************
            for l in range(1,result_data.__len__(),1):
                print(result_data[l])
                if(result_data[l][2]=="Y"):
                    print(result_data[l][1])
                    #executionList.append(result_data[l][0]+"_"+result_data[l][1]+"_"+result_data[l][2])
                    executionList.append(result_data[l][0] + "_" + result_data[l][1])

        except(Exception):
            executionList = []
        return executionList
        #**********************************************

    def getExcelData(self,tcName,dataColumn):
        result_data = ''
        try:
            excelFile = os.path.abspath(__file__ + "/../../data/ExcelData") + "/" + xpmsdata.TestDataExcel

            workbook = xlrd.open_workbook(excelFile)
            worksheet = workbook.sheet_by_name("TestData")  # We need to read the data
            num_rows = worksheet.nrows  # Number of Rows
            num_cols = worksheet.ncols  # Number of Columns
            # **********************************************
            tempColumn = '';tempRow = ''
            for curr_col in range(0, (num_cols), 1):
                data = worksheet.cell_value(0, curr_col)
                if(data==dataColumn):
                    tempColumn = curr_col
                print("data :",data)
            # **********************************************
            for curr_row in range(0, (num_rows), 1):
                data = worksheet.cell_value(curr_row, 0)
                if (data == tcName):
                    tempRow = curr_row
                print("Row data :", data)
                # **********************************************
            result_data = worksheet.cell_value(tempRow, tempColumn)
            print("Required Value Is :",result_data)
            return result_data

        except:
            result_data = ''

    #*******************************************************

