from flask import Flask,redirect,request
import sqlite3
app = Flask(__name__)
@app.route("/")
def home():
    con = sqlite3.connect('table_manager.db')
    result = con.execute('SELECT * FROM topic')
    topics = result.fetchall()
    print(topics[1][1])

    nav = '<ol>'
    for topic in topics:
        nav = nav+'<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</li>'
    nav = nav+'</ol>'
    content='''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                <p><a href="/create">create</a></p>
                Hello, WEB!
            </body>
        </html>
    '''
    return content

@app.route("/create")
def create():
    con = sqlite3.connect('table_manager.db')
    result = con.execute('SELECT * FROM topic')
    topics = result.fetchall()
    print(topics[1][1])

    nav = '<ol>'
    for topic in topics:
        nav = nav+'<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav+'</ol>'
    content='''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <form method="post" action="/create_process">
                    <p><input type="text" name="title" placeholder="title" ></p>
                    <p><textarea name="body" placeholder="body" ></textarea></p>
                    <p><input type="submit" value="create"></p>
                </form>
            </body>
        </html>
    '''
    return content

@app.route("/create_process", methods = ['POST'])
def create_process():
    con = sqlite3.connect('table_manager.db')
    title = request.form['title']
    body=request.form['body']
    sql = "INSERT INTO topic(title,body) VALUES('"+title+"','"+body+"')"
    result = con.execute(sql)
    con.commit()
    return redirect("/read/"+str(result.lastrowid))

@app.route("/read/<topicid>")
def read(topicid):
    con = sqlite3.connect('table_manager.db')
    result = con.execute('SELECT * FROM topic WHERE id ='+topicid)
    topic = result.fetchone()
    content = '<h2>'+topic[1]+'</h2>'+topic[2]
    contents='''
        <!DOCTYPE html>
        <html>
            <body>
                '''+content+'''
            </body>
        </html>
    '''
    return contents
app.run()