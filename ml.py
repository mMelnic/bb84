import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from bb84_protocol import BB84Protocol, EveConfig


class MLDetector:
    FEATURES = ["error_rate", "sift_ratio"]

    def __init__(self):
        self.model = None
        self.is_trained = False
        self.metrics = None

    def generate_training_data(self, n_sessions=50, n_qubits=50, max_noise=0.05):
        data = []

        for eve_present in [False, True]:

            for _ in range(n_sessions):
                bb84 = BB84Protocol(n_qubits)
                noise_prob = np.random.uniform(0.0, max_noise)
                intercept_rate = np.random.uniform(0.3, 1.0) if eve_present else 0.0
                eve_config = EveConfig(active=eve_present, intercept_rate=intercept_rate)
                qber, key_len = bb84.run_session(eve_config=eve_config, noise_prob=noise_prob)
                data.append(
                    {"error_rate": qber, "sift_ratio": key_len / n_qubits, "eve": int(eve_present)}
                )

        return pd.DataFrame(data)

    def train(self, n_sessions=50, n_qubits=50):
        df = self.generate_training_data(n_sessions, n_qubits)

        X = df[self.FEATURES]
        y = df["eve"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

        self.model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42, max_iter=1000))
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        self.metrics = {
            "confusion_matrix": confusion_matrix(y_test, y_pred, labels=[0, 1]),
            "classification_report": classification_report(y_test, y_pred, zero_division=0, output_dict=True),
        }
        self.is_trained = True

        return self.model

    def predict(self, qber, sift_ratio):
        if not self.is_trained:
            raise ValueError("Model not trained. Call train() first.")

        features = pd.DataFrame([[qber, sift_ratio]], columns=self.FEATURES)
        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0, 1]

        return prediction, probability

    def evaluate_scenarios(self, scenarios, n_qubits=50, noise_prob=0.02):
        if not self.is_trained:
            raise ValueError("Model not trained. Call train() first.")

        results = []

        for name, eve_cfg in scenarios:
            bb84 = BB84Protocol(n_qubits)
          
            qber, key_len = bb84.run_session(eve_cfg, noise_prob)   
            prediction, probability = self.predict(qber, key_len / n_qubits)

            results.append(
                {
                    "Scenario": name,
                    "QBER": qber,
                    "Sift Ratio": key_len / n_qubits,
                    "ML Confidence": probability,
                    "Prediction": "ATTACK SUSPECTED" if prediction == 1 else "NO ATTACK PREDICTED",
                }
            )

        return pd.DataFrame(results)
