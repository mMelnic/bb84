import numpy as np
import pandas as pd
from bb84_protocol import BB84Protocol, EveConfig


class BB84Analyzer:

    @staticmethod
    def generate_dataset(n_sessions=50, n_qubits=50, noise_level=0.02, eve_rate=0.5):
        data = []

        n_without_eve = n_sessions // 2
        n_with_eve = n_sessions - n_without_eve

        # Sessions without Eve
        for eve_present, count in [(False, n_without_eve), (True, n_with_eve)] :
            for _ in range(count):

                bb84 = BB84Protocol(n_qubits)

                config = EveConfig(active=eve_present, intercept_rate=eve_rate)

                qber, key_len = bb84.run_session(eve_config=config, noise_prob=noise_level)

                data.append({
                    "QBER": qber,
                    "Key Length": key_len,
                    "Sift Ratio": key_len / n_qubits,
                    "Eve Present": "Yes" if eve_present else "No"
                })

        return pd.DataFrame(data)

    @staticmethod
    def compute_summary_statistics(df):
        summary = (
            df.groupby("Eve Present")
            .agg(
                {
                    "QBER": ["mean", "std", "min", "max"],
                    "Sift Ratio": ["mean", "std"],
                    "Key Length": ["mean", "std"],
                }
            )
            .round(4)
        )

        return summary

    @staticmethod
    def test_scenarios(scenarios, n_qubits=50):
        results = []

        for name, eve_cfg, noise in scenarios:
            bb84 = BB84Protocol(n_qubits)
            qber, key_len = bb84.run_session(eve_cfg, noise)

            results.append(
                {
                    "Scenario": name,
                    "QBER": qber,
                    "Key Length": key_len,
                    "Sift Ratio": key_len/n_qubits,
                    "Detection": "High risk" if key_len > 0 and qber > 0.11
                                  else "Insufficient data" if key_len == 0
                                  else "Below threshold"
                }
            )

        return pd.DataFrame(results)
