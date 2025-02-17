import random
from flask import Flask,render_template,request
app=Flask(__name__)


#import random 
movies={
    "action":["War (2019)","Pathaan (2023)","Dhoom 2 (2006)","Singham (2011)","Agneepath (2012)","Gadar: Ek Prem Katha (2001)","Khiladi (1992)"],
    "comedy":["Hera Pheri (2000)","Andaz Apna Apna (1994)","Dhamaal (2007)","Chupke Chupke (1975)","Golmaal: Fun Unlimited (2006)","Fukrey (2013)","Welcome (2007)"],
    "drama":["Taare Zameen Par (2007)","Swades (2004)","Kabir Singh (2019)","Udaan (2010)","Chak De! India (2007)","Barfi! (2012)","Masaan (2015)","Kapoor & Sons (2016)"],
    "crime":["Gangs of Wasseypur (2012)","Drishyam (2015)","Black Friday (2007)","Talvar (2015)","Badlapur (2015)","Shootout at Lokhandwala (2007)","Once Upon a Time in Mumbaai (2010)"],
    "sci-fi":["Ra.One (2011)","Robot (2010)","PK (2014)","2.0 (2018)","Cargo (2020)","Attack (2022)","Aditya 369 (1991)"],
    "horror":["Tumbbad (2018)","Bhoot (2003)","Raaz (2002)","Stree (2018)","1920 (2008)","Pari (2018)"]
}
@app.route("/",methods=["GET","POST"])
def index():
    recommend=None 
    error_message=None
    if request.method == "POST":
        types=request.form.get("types", "").lower()
        if types in movies:
            recommend=random.choice(movies[types])
        else:
            error_message = "⚠️ That category is not available yet!"
            
    return render_template("index.html",recommend=recommend ,error_message=error_message)
if __name__=="__main__":
    app.run(debug=True)
            
            
# print("Available types:")
# for types in movies.keys():
#     print("->",types)

# choose_type=input("enter your movie type:").strip().lower()

# if choose_type in movies:
#     recommend=random.choice(movies[choose_type])
#     print(f"You can watch:{recommend}")
# else:
#     print("That type is not available yet!!") 
