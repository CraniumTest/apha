import tensorflow as tf

def retrain_model_with_new_data(new_data_path, old_model_path, new_model_path):
    new_model = tf.keras.models.load_model(old_model_path)
    X_train, X_test, y_train, y_test = load_and_preprocess_data(new_data_path)
    new_model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
    new_model.save(new_model_path)
