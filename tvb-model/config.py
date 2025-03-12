from charset_normalizer.constant import FREQUENCIES

TRAIN_DIR = "Dataset/Train/"
VALIDATION_DIR = "Dataset/Validation/"
TEST_DIR = "Dataset/Test/"

# data_loader.py config setting
BATCH_SIZE = 32
IMG_SIZE = (256, 256)
EPOCHS = 20
CLASS_MODE = 'binary'

# data_loader.py Image Aug
RESCALE = 1. / 255
ROTATION_RANGE = 20
WIDTH_SHIFT_RANGE = 0.2
HEIGHT_SHIFT_RANGE = 0.2
SHEAR_RANGE = 0.2
ZOOM_RANGE = 0.2
HORIZONTAL_FLIP = True
BRIGHTNESS_RANGE = [0.5, 1.5]
FILL_MODE = 'nearest'

# model.py config setting
XCEPTION_MODEL_WEIGHT = 'imagenet'
XCEPTION_MODEL_INCLUDE_TOP = False
XCEPTION_MODEL_INPUT_SHAPE = (256, 256, 3)

XCEPTION_MODEL_DENSE_LAYER = 1024
XCEPTION_MODEL_DENSE_ACTIVATION = 'relu'
XCEPTION_MODEL_DENSE_KERNEL_L2_REGULARIZER = 0.01

XCEPTION_MODEL_DROPOUT = 0.4
XCEPTION_MODEL_OUTPUT_DENSE_LAYER_ACTIVATION = 'sigmoid'

XCEPTION_MODEL_LOSS = 'binary_crossentropy'
XCEPTION_MODEL_METRICS = ['accuracy']

# Learning Schedular
INITIAL_LEARNING_RATE = 0.01
DECAY_STEPS = 43750
ALPHA = 0.01

# EARLY_STOP
MONITER = 'val_loss'
PATIENT = 4
RESTORE = True

# Tensor Board
TB_DIR = './logs'
FREQUENCY = 1