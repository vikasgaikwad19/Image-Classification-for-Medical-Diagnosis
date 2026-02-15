from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data():

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        zoom_range=0.2,
        shear_range=0.2,
        horizontal_flip=True
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    train_data = train_datagen.flow_from_directory(
        "dataset/train",
        target_size=(224, 224),
        batch_size=32,
        class_mode="binary"
    )

    test_data = test_datagen.flow_from_directory(
        "dataset/test",
        target_size=(224, 224),
        batch_size=32,
        class_mode="binary"
    )

    return train_data, test_data
