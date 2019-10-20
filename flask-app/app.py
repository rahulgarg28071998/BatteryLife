# # from flask import Flask

# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return "Hello, World!"
    
# # @app.route("/salvador")
# # def salvador():
# #     return "Hello, Salvador"
    
# # if __name__ == "__main__":
# #     app.run(debug=True)



# # from flask import Flask, render_template      

# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return render_template("index.html")
    
# # @app.route("/salvador")
# # def salvador():
# #     return "Hello, Salvador"
    
# # if __name__ == "__main__":
# #     app.run(debug=True)




# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")
    
# @app.route("/about")
# def about():
#     return render_template("about.html")
    
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# class ReusableForm(Form):
#     name = TextField('Name:', validators=[validators.required()])
#     email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
#     password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    
#     @app.route("/", methods=['GET', 'POST'])
#     def hello():
#         form = ReusableForm(request.form)
    
#         print(form.errors)
#         if request.method == 'POST':
#             name=request.form['name']
#             battery=request.form['battery']
#             chargingstatus=request.form['chargingstatus']
#             buytime=request.form['buytime']
#             # voltage=request.form['voltage']
#             # current=request.form['current']
#             # temperature=request.form['temperature']

#             print(name, " ", battery, " ", chargingstatus, " ", buytime, " ",voltage," ", current, " ", temperature, " ")
    
#         if form.validate():
#         # Save the comment here.
#             flash('Thanks for registration ' + name)
#         else:
#             flash('Error: All the form fields are required. ')
    
#         return render_template('index.html', form=form)

# if __name__ == "__main__":
#     app.run()


from flask import Flask

UPLOAD_FOLDER = 'D:\one plus images'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024