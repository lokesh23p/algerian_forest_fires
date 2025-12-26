import pickle
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# If you used a DataFrame during training, this will show the column names:
try:
    print("Expected Feature Names:", scaler.feature_names_in_)
except AttributeError:
    print("Expected Number of Features:", scaler.n_features_in_)