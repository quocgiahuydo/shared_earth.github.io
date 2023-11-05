import matplotlib.pyplot as plt
from scipy import stats
from flask import Flask, request, render_template 



def main(animal,d_1,d_2,d_3,d_4,d_5,d_6,y_1,y_2,y_3,y_4,y_5,y_6,desired_data=0):
    data = [d_1,d_2,d_3,d_4,d_5,d_6]
    years = [y_1,y_2,y_3,y_4,y_5,y_6]
    slope, intercept, r, p, std_err = stats.linregress(data, years)
    print(slope,intercept)
    data_last = -intercept/slope
    print(data_last)
    data.append(data_last)
    years.append(0)

    def myfunc(data):
        return slope * data + intercept

    mymodel = list(map(myfunc, data))
    plt.scatter(data, years)
    plt.plot(data, mymodel)
    plt.savefig(f"graphs/{animal}.jpg")
    plt.clf()
    return myfunc(desired_data)

main("Hawksbill turtles",1970,1980,1990,2000,2010,2023,38000,30000,28000,24000,22000,20000)
main("Bornean Orangutan ",1970,1980,1990,2000,2010,2023,160000,140000,112000,100000,75000,50000)
main("African forest Elephant",1995,1998,2002,2007,2013,2015,286233,301733,402047,472269,426293,415428)
main("Black Rhinos",2009,2010,2012,2015,2017,2021,4879,4880,4845,5214,5494,6195)
main("Yangtze Finless Porpoise",2006,2008,2010,2012,2014,2016,2750,2250,2125,1125,1100,1000)
main("Mountain Gorillas",2002,2006,2015,2016,2018,2019,320,340,400,400,459,459)
main("Sunda Island Tiger",2000,2005,2010,2015,2020,2023,750,675,600,525,450,400)
main("Amur Leopard", 2011,2012,2013,2014,2015,2016,42,43,49,53,56,60)
main("Javan Rhinos",2010,2012,2013,2016,2018,2020,40,40,58,63,72,76)

app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template('index.html') 
 
@app.route('/process', methods=['POST']) 
def process(animal,d_1,d_2,d_3,d_4,d_5,d_6,y_1,y_2,y_3,y_4,y_5,y_6,year): 
    print(main(animal,d_1,d_2,d_3,d_4,d_5,d_6,y_1,y_2,y_3,y_4,y_5,y_6,year))
    
if __name__ == '__main__': 
    app.run(debug=True)