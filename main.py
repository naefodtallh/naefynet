from flask import Flask
import pandas as pd
from lxml import etree
app = Flask(__name__)

@app.route('/')
@app.route('/ynet')
def ynet():
    data = "C:\Users\User\Desktop\yynetn\StoryRss2.xml"
    tree = etree.parse(data)
    lstKey = []
     lstValue = []
    for p in tree.iter() :
    lstKey.append(tree.getpath(p).replace("/",".")[1:])
    lstValue.append(p.text)
    df = pd.DataFrame({'key' : lstKey, 'value' : lstValue})
    df.sort_values('key')



if __name__ == "__main__":
    app.run(host='0.0.0.0')


