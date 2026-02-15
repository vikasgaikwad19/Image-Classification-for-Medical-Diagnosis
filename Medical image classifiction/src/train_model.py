from src.data_preprocessing import load_data
from src.cnn_model import build_model

def train():

    print("\nLoading Dataset...")
    train_data, test_data = load_data()

    print("\nBuilding Model...")
    model = build_model()

    print("\nTraining Started...\n")

    model.fit(
        train_data,
        epochs=10,
        validation_data=test_data
    )

    model.save("models/medical_cnn_model.h5")

    print("\n✅ Training Complete & Model Saved!")
