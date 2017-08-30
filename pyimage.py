import requests
from flask import Flask
from flask import render_template
app = Flask(__name__)



def fetch(item=""):
    imageurl= 'http://so.picasso.adesk.com/v1/search/wallpaper/resource/'+ str(item) + '?limit=30&channel=androidesk&adult=false&first=0'
    head = {'user-agent': "picasso,174,androidesk", 'Accept-Encoding': 'gzip', 'host': 'so.picasso.adesk.com'}
    conn = requests.get(imageurl, headers=head)
    conn = conn.json()
    res = conn.content
    return conn # change this to "res" if there is type error 


# def recursive_items(dictionary):
#     for key, value in dictionary.items():
#         if type(value) is dict:
#             yield (key, value)
#             yield from recursive_items(value)
#         else:
#             yield (key, value)
def extractdic(dicIn, itemToExtract=None):
    outDic = []
    itemsExtract = ["name", "thumb", "rank", "tag", "preview", "wp", "favs", "views", "id", "desc"]
    if len(dicIn["res"]["wallpaper"]) >0:
        for i in range(0, len(dicIn["res"]["wallpaper"])):
            try:
                for k, v in dicIn["res"]["wallpaper"][i].items():
                    if "thumb" in k and len(v) > 4:
                        outDic.append(v)
            except IndexError:
                print("index error")
    else:
        for i in range(0, 29):
            try:
                for k, v in dicIn["res"]["wallpaper"][i].items():
                    if "thumb" in k and len(v) > 4:
                        outDic.append(v)
            except IndexError:
                print("index error")
    return outDic


@app.route('/<searchTerm>')
def drawmage(searchTerm):
    searchTerm= fetch(searchTerm)
    dicout = extractdic(searchTerm)
    return render_template("index.html", imageDict=dicout)


if __name__ == "__main__":
    app.run(debug=True)




