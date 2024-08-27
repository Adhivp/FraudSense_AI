import streamlit as st
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import os

st.set_page_config(
    page_title="Models Page",
    page_icon="images/favicon/favicon-32x32.png"
)

current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, "../images")

st.header("XGBoost Model")
st.write("**XGBoost:** Accuracy on training Data: 0.865")
st.write("**XGBoost:** Accuracy on test Data: 0.871")

xgb = XGBClassifier(learning_rate=0.4, max_depth=7)
st.code("""
from xgboost import XGBClassifier

xgb = XGBClassifier(learning_rate=0.4, max_depth=7)
""", language="python")

st.header("MLP Model")
st.write("**MLP:** Accuracy on training Data: 0.862")
st.write("**MLP:** Accuracy on test Data: 0.863")

mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=([100, 100, 100]))
st.code("""
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=([100,100,100]))
""", language="python")

st.subheader("Confusion Matrices")

xgb_train_image = os.path.join(images_dir, "xgb_confusion_matrix_train.png")
xgb_test_image = os.path.join(images_dir, "xgb_confusion_matrix_test.png")
mlp_train_image = os.path.join(images_dir, "mlp_confusion_matrix_train.png")
mlp_test_image = os.path.join(images_dir, "mlp_confusion_matrix_test.png")

st.write("### XGBoost Confusion Matrix (Training Data)")
st.image(xgb_train_image)

st.write("### XGBoost Confusion Matrix (Test Data)")
st.image(xgb_test_image)

st.write("### MLP Confusion Matrix (Training Data)")
st.image(mlp_train_image)

st.write("### MLP Confusion Matrix (Test Data)")
st.image(mlp_test_image)
