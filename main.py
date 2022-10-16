from flask import Flask,request
from flask.templating import render_template
from App_Analyzer_module.Analyzer import StarbasedAnalyzer,NormalAnalyer
from App_Analyzer_module.App import AppInfo

app=Flask(__name__)

#def StarBasedLazy(appid,star):
    
#def StarBasedQuick(appid,star):
    
#def NormalQuick(appid):

#def NormalLazy(appid):

@app.route('/app-analyzier',methods=['GET','POST'])
def NormalAnalysisInputTaker():
    
    if request.method=="POST":
        try:
            appid=request.form['appid']
            chooice=request.form['chooice']
            
            if chooice=="1": 
                obj=NormalAnalyer()
                plot=obj.Quick_Analysis(appid)
                info=AppInfo()
                if plot==1:
                    return render_template('index.html',plot=plot,appinfo=info.Info(appid),permission=AppInfo.Permission(appid))
                else:
                    return render_template('index.html',error_msg=plot)
            if chooice=="2":
                obj=NormalAnalyer()
                plot=obj.Lazy_Analysis(appid)
                info=AppInfo()
                if plot==1:
                    return render_template('index.html',plot=plot,appinfo=info.Info(appid),permission=AppInfo.Permission(appid))
                else:
                    return render_template('index.html',error_msg=plot,script="")
        
        except Exception as e:
            return render_template('index.html',msg="Please provide values for all field")

    return render_template('index.html')

@app.route('/app-analyize-by-star',methods=['GET','POST'])
def StarBasedAnalysisInputTaker():
    
    if request.method=="POST":
        try:
            appid=request.form['appid']
            star=request.form['star']
            chooice=request.form['chooice']
            if chooice=="3": 
                obj=StarbasedAnalyzer()
                info=AppInfo()
                plot=obj.Star_Quick_Analysis(appid,star)
                if plot==1:
                    return render_template('index.html',plot=plot,no_of_star=star,star=1,appinfo=info.Info(appid),permission=AppInfo.Permission(appid))
                else:
                    return render_template('index.html',error_msg=plot,star=1)
                    
            if chooice=="4": 
                obj=StarbasedAnalyzer()
                info=AppInfo()
                plot=obj.Star_Lazy_Analysis(appid,star)
                if plot==1:
                    return render_template('index.html',plot=plot,no_of_star=star,star=1,appinfo=info.Info(appid),permission=AppInfo.Permission(appid))
                else:
                    return render_template('index.html',error_msg=plot,no_of_star=star,star=1)
        
        except Exception as e:
            return render_template('index.html',msg="Please provide values for all field",star=1)
       

    return render_template('index.html',star=1)

@app.route('/')
def welcome():
    return render_template('Welcome.html')

@app.route("/app-instructions")
def Instruction():
    return render_template('instructions.html')






