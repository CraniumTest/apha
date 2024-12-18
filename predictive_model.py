import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from data_preprocessing import load_and_preprocess_data

def build_model(input_shape):
    model = Sequential()
    model.add(Dense(64, input_shape=(input_shape,), activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Assuming binary classification for health outcome

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_and_save_model(data_path, model_path):
    X_train, X_test, y_train, y_test = load_and_preprocess_data(data_path)
    model = build_model(X_train.shape[1])
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
    model.save(model_path)
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f'Test accuracy: {test_acc}')
