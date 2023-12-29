import pickle
from flask import Flask, render_template, request



# OOPs
# Class, Objects, Methods, Inheritence, Polymorphism, Abstraction, Encapsulation
# Decorators, Generastors, Dunder Methods, Abstract methods, Static methods

# Create an object of the class Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

# url/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    try:
        temperature=request.form.get('temperature')
        prediction = model.predict([[float(temperature)]])
        output = round(prediction[0],2)
        return render_template('index.html', prediction_text=f'Total revenue generated is Rs. {output}/-')
    except:
        return render_template('index.html', prediction_text=f'Invalid input')
if __name__=='__main__':
    app.run(debug=True)
