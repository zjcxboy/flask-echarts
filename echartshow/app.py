from flask import Flask, render_template,jsonify
import pymysql
app = Flask(__name__)

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='1234567',
    db='student',
    charset='utf8'
)


@app.route('/')
def index():
    return render_template("index.html")

# 读取Mysql中数据并利用jsonify解析成json
@app.route('/stu')
def get_stu_data():
    cur = conn.cursor()
    sql="select name,number from stu_table"
    cur.execute(sql)
    studata = cur.fetchall()
    conn.commit()
    conn.close()
    name = []
    number = []
    for a, b in studata:
        name.append(a)
        number.append(int(b))
    return jsonify({"name": name, "number": number})
    return content


if __name__ == '__main__':

    app.run(debug=True)