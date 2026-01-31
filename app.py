from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route('/',methods=["GET"])
def registration_page():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method =='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
    
        return render_template(
            'submit.html',
            name=name,
            email=email,
            phone=phone
        )

    return "Invalid Request"


    

if __name__ == '__main__':
    app.run(debug=True)