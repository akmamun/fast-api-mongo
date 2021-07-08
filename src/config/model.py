import os


def model() -> dict:

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = f"{base_path}/ml_models"

    return {
        "model_path": f"{model_path}/14_37_11 2021_model.pkl",
    }
