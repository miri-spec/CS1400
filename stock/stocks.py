'''
My file path name is:
C:/Users/10919/Downloads/stocks_data.csv
Depending on where your csv file is stored, use your own path in the
input.
This program uses the pandas package to enter the csv file as a database.
I then filter the data base for one of three stock types, and put the results
into their own database.
The main function sorts each stock database by ascending and then descending.
The output is the first value of each list. The average is found by using
the .mean() method.
'''
import pandas
filepath = input("Enter the file path for the stock data csv file: ")
df = pandas.read_csv(filepath)
f = open("stock_summary.txt" , 'w')

aapl = df[(df.Symbol == "AAPL")]
ibm = df[(df.Symbol == "IBM")]
msft = df[(df.Symbol == "MSFT")]

def main(stock):
    print("----")
    sorted_stock = stock.sort_values(by=["Adj Close"], ascending=False)
    maxi = "%0.2f" % sorted_stock.iloc[0,2]
    max_date = sorted_stock.iloc[0,1]
    print("Max: ", maxi, max_date)
    f.write("Max: " + str(maxi) + " " + str(max_date) + "\n")
    
    reverse_stock = stock.sort_values(by=["Adj Close"], ascending=True)
    mini = "%0.2f" % reverse_stock.iloc[0,2]
    mini_date = reverse_stock.iloc[0,1]
    print("Min: " , mini , mini_date)
    f.write("Min: " + str(mini) + " " + str(mini_date) + "\n")
    
    ave = "%0.2f" % stock["Adj Close"].mean()
    print("Ave: " , ave)
    f.write("Ave: " + str(ave))
    
    sorted_total = df.sort_values(by=["Adj Close"], ascending=False)
    total_max = "%0.2f" % sorted_total.iloc[0,2]
    max_symbol = sorted_total.iloc[0,0]
    max_date = sorted_total.iloc[0,1]
    print("\nHighest: ", max_symbol , total_max , max_date)
    f.write("\n\nHighest: "+ str(max_symbol) + " " + str(total_max) + " " + str(max_date))
    
    sorted_reverse = df.sort_values(by=["Adj Close"], ascending=True)
    total_min = "%0.2f" % sorted_reverse.iloc[0,2]
    min_symbol = sorted_total.iloc[0,0]
    min_date = sorted_total.iloc[0,1]
    print("Lowest: ", min_symbol , total_min , min_date)
    f.write("\nLowest: " + str(min_symbol) + " " + str(total_min) + " " + str(min_date))
    
if __name__ == "__main__":
    print("\nAAPL:")
    f.write("AAPL:" + "\n----\n")
    main(aapl)
    print("\nIBM:")
    f.write("\n\nIBM:" + "\n----\n")
    main(ibm)
    print("\nMSFT:")
    f.write("\n\nMSFT:" + "\n----\n")
    main(msft)
    
    

f.close()