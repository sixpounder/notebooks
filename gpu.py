import tensorflow as tf
def print_gpu_info():
    print(f"Tensorflow version: {tf.__version__}")
    print("Tensorflow GPU support:", tf.test.is_built_with_gpu_support())
    print("GPU device(s):", tf.config.list_physical_devices("GPU"))
