from google_play_scraper import app,permissions

class AppInfo:
    def Info(self,appid):
        App=app(
        appid,
        lang='en',
        )
        info={}
        info["no_of_installs"]=App['installs']
        info["ratings"]=App['ratings']
        info["totoal rating"]=App['score']
        info["reviewed by"]=App['reviews']
        info["developed by"]=App['developer']
        info["Developer website"]=App['developerWebsite']
        info["developerAddress"]=App['developerAddress']
        info["containsAds"]=App['containsAds']
        info["privacyploicy"]=App['privacyPolicy']
        info['Appvideo']=App['video']
        info['recentChanges']=App['recentChanges']
        info['comments']=App['comments']
        return App

    def Permission(self,appid):
        p=permissions(
            app_id=appid,
            lang='en',
            country='us'
        )
        return p 


