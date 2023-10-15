import pickle

model_file = open("co2_prediction.pk", "rb")
model = pickle.load(model_file)
model_file.close()
co2_emissions = model.predict([[2,4,8]])
print(co2_emissions)
