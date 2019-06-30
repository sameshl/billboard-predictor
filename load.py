
# import numpy as np
# import keras.models
import pandas as pd


def init():
    from keras.models import model_from_json
    import tensorflow as tf
    json_file = open('./model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load woeights into new model
    loaded_model.load_weights("./model/model.h5")
    print("Loaded Model from disk")

    # compile and evaluate loaded model
    loaded_model.compile(optimizer='adam', loss='binary_crossentropy',
                         metrics=['accuracy'])
    # loss,accuracy = model.evaluate(X_test,y_test)
    # print('loss:', loss)
    # print('accuracy:', accuracy)
    graph = tf.get_default_graph()

    return loaded_model, graph


def get_standard_scalar():
    # To export standard scalar with appropriate values

    # Read the machine learning model's scaled model data which
    # needs to be scaled
    # Clean the data before applying standard scalar
    new_data = pd.read_csv('standard_scalar_data.csv')
    X = new_data.drop('BillboardHit', axis=1)
    # y = new_data['BillboardHit']
    mode = pd.get_dummies(X['Mode'], drop_first=True)
    key = pd.get_dummies(X['Key'], drop_first=True)
    X.drop(['Mode', 'Key'], inplace=True, axis=1)
    X = pd.concat([X, mode, key], axis=1)

    # Import standard scalar
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    return sc
