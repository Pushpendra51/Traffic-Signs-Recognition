import pandas as pd
import numpy as np
from PIL import Image
from keras.models import load_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Load model
model = load_model("src/my_model.h5", compile=False)

# Load test data
df = pd.read_csv("Test.csv")

X = []
y = []

for _, row in df.iterrows():
    image = Image.open(row["Path"]).convert("RGB")
    image = image.resize((30, 30))
    X.append(np.array(image))
    y.append(row["ClassId"])

X = np.array(X)
y = np.array(y)

# Predictions
predictions = model.predict(X, batch_size=32, verbose=1)
y_pred = np.argmax(predictions, axis=1)

# Metrics
print("\n===== MODEL PERFORMANCE =====")
print("Accuracy :", accuracy_score(y, y_pred))
print("Precision:", precision_score(y, y_pred, average="weighted", zero_division=0))
print("Recall   :", recall_score(y, y_pred, average="weighted", zero_division=0))
print("F1 Score :", f1_score(y, y_pred, average="weighted", zero_division=0))

# Confusion matrix
cm = confusion_matrix(y, y_pred)
print("\nConfusion Matrix Shape:", cm.shape)
print(cm)