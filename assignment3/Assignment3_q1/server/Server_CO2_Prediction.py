from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])         # Decorator
def root():
    # read the index.html from templates directory
    # and send the contents as return value
    return render_template("index.html")


@app.route("/predict", methods=["GET"])         # Decorator
def predict():
    print(f"query string: {request.args}")
    ENGINESIZE = float(request.args.get('ENGINESIZE'))
    CYLINDERS = float(request.args.get('CYLINDERS'))
    FUELCONSUMPTION_COMB = float(request.args.get('FUELCONSUMPTION_COMB'))


    import pickle

    model_file = open("co2_prediction.pk", "rb")
    model = pickle.load(model_file)
    co2_emissions = model.predict([[ENGINESIZE, CYLINDERS, FUELCONSUMPTION_COMB]])
    model_file.close()
    print(f"ENGINESIZE = {ENGINESIZE}, CYLINDERS = {CYLINDERS}, FUELCONSUMPTION_COMB = {FUELCONSUMPTION_COMB}")
    return f"Your CO2 Emission = {co2_emissions[0]}"


app.run(port=8080, host="0.0.0.0", debug=True)


