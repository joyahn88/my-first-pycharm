from flask import Flask, render_template , jsonify, request
app = Flask(__name__)

articles=[]
article_no=1

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API
@app.route('/post', methods=['POST'])
def post():
   global articles
   global article_no

   url_receive = request.form['url_give']
   comment_receive = request.form['comment_give']
   category_receive = request.form['category_give']

   article={'url':url_receive, 'comment':comment_receive, 'category_receive':category_receive, 'no':article_no}

   article_no=article_no +1
   articles.append(article)

   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
    global articles
    return jsonify({'result':'success', 'articles':articles})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)