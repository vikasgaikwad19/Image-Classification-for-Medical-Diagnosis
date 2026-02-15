from src.train_model import train
from src.predict import predict_image

if __name__ == "__main__":

    print("1. Train Model")
    print("2. Predict Image")

    choice = input("Enter choice: ")

    if choice == "1":
        train()

    elif choice == "2":
        path = input("Enter image path: ")
        result = predict_image(path)
        print("\nPrediction:", result)

    else:
        print("Invalid choice")
