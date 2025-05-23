import tf_keras
from tf_keras.applications import Xception
from tf_keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tf_keras.models import Model
from tf_keras.optimizers.schedules import CosineDecay
import tensorflow as tf
from tf_keras.regularizers import l2
from config import *
from tf_keras.optimizers import Adam
def build_xception():
    xception_model = Xception(weights=XCEPTION_MODEL_WEIGHT, include_top=XCEPTION_MODEL_INCLUDE_TOP, input_shape=XCEPTION_MODEL_INPUT_SHAPE)

    x = xception_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(XCEPTION_MODEL_DENSE_LAYER, activation=XCEPTION_MODEL_DENSE_ACTIVATION, kernel_regularizer=l2(XCEPTION_MODEL_DENSE_KERNEL_L2_REGULARIZER))(x)
    x = Dropout(XCEPTION_MODEL_DROPOUT)(x)
    x = Dense(1, activation=XCEPTION_MODEL_OUTPUT_DENSE_LAYER_ACTIVATION)(x)

    optimizer = tf_keras.optimizers.Adam(learning_rate=learningSchedular_CosineDecay())

    model = Model(inputs=xception_model.input, outputs=x)
    model.compile(optimizer=optimizer, loss=XCEPTION_MODEL_LOSS, metrics=XCEPTION_MODEL_METRICS)

    return model

def learningSchedular_CosineDecay() :
    return CosineDecay(
        initial_learning_rate=INITIAL_LEARNING_RATE,
        decay_steps=DECAY_STEPS,
        alpha=ALPHA
    )