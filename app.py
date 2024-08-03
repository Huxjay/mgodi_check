# # from flask import Flask

# # app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return "Hello, Flask!"

# # if __name__ == "__main__":
# #     app.run(debug=True)

# from flask import Flask, render_template, request
# import numpy as np
# import pickle

# app = Flask(__name__)

# # Load the trained model (ensure you have saved it using pickle)
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def mgodi():
#     return render_template('mgodi.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Example: expecting features features
#         #  date = datetime(request.form['date'])
#          precipitation = float(request.form['precipitation'])
#          temp_max = float(request.form['temp_max'])
#          temp_min = float(request.form['temp_min'])
#          wind = float(request.form['wind'])



#         # Create an array in the shape expected by your model
#          input_features = [[date,precipitation,temp_max,temp_min,wind,]]
#          final_features = np.array(input_features).reshape(1,-1)
#         # Make prediction
#          prediction = model.predict(input_features)
         
#          weather_predic = {
#             1: 'rain', 2:'sun', 3:'snow', 4:'fog', 5:'drizzle'
#          }

#          weather = weather_predic.get(prediction[0]),""
#          result = "{}".format(weather)

#     except ValueError:
#         # Handle conversion errors
#         result = "Invalid input. Please enter valid numerical values."

#         return render_template('mgodi.html', prediction_text=f'Predicted Value: {prediction[0]}')
         
# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, render_template
# import pickle
# import numpy as np
# from datetime import datetime

# app = Flask(__name__)

# # Load the model
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/')
# def mgodi():
#     return render_template('mgodi.html', prediction=None)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Convert the date input to a datetime object and then to a numeric value if needed
#         date_str = request.form['date']
#         date = datetime.strptime(date_str, "%Y-%m-%d").timestamp()

#         precipitation = float(request.form['precipitation'])
#         temp_max = float(request.form['temp_max'])
#         temp_min = float(request.form['temp_min'])
#         wind = float(request.form['wind'])

#         # Features array
#         input_features = [[date, precipitation, temp_max, temp_min, wind]]
#         prediction = model.predict(input_features)[0]

#         return render_template('mgodi.html', prediction=prediction)
#     except Exception as e:
#         return render_template('mgodi.html', prediction=f"Error: {e}")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, render_template
import pickle
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Define the weather mapping
weather_mapping = {
    0: 'safe',
    1: 'unsafe',
    2: 'unsafe',
    3: 'risk!'
}

@app.route('/')
def mgodi():
    return render_template('mgodi.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert the date input to a datetime object and then to a numeric value if needed
        date_str = request.form['date']
        date = datetime.strptime(date_str, "%Y-%m-%d").timestamp()

        precipitation = float(request.form['precipitation'])
        temp_max = float(request.form['temp_max'])
        temp_min = float(request.form['temp_min'])
        wind = float(request.form['wind'])

        # Features array
        input_features = [[date, precipitation, temp_max, temp_min, wind]]
        prediction_numeric = model.predict(input_features)[0]

        # Map the numeric prediction to the human-readable label
        prediction = weather_mapping.get(prediction_numeric, "Unknown")

        return render_template('mgodi.html', prediction=prediction)
    except Exception as e:
        return render_template('mgodi.html', prediction=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)

