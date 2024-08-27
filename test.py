import pickle
from sklearn.neural_network import MLPClassifier
import joblib
with open('Trained_models/MLP.pkl', 'rb') as mlp_file:
    mlp_model = joblib.load(mlp_file)
    print(type(mlp_model))

# Check the type of the loaded model
