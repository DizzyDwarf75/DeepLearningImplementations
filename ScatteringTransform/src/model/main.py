import os
# Disable Tensorflow's INFO and WARNING messages
# See http://stackoverflow.com/questions/35911252
if 'TF_CPP_MIN_LOG_LEVEL' not in os.environ:
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import flags
import train_mnist
import tensorflow as tf
FLAGS = tf.app.flags.FLAGS


def launch_training():

    train_mnist.train_model()


def main(argv=None):

    # Only training is implemented at this stage
    assert FLAGS.run in ["train", "inference"], "Choose [train|inference]"

    if FLAGS.run == 'train':
        launch_training()


if __name__ == '__main__':
    flags.define_flags()
    tf.app.run()
