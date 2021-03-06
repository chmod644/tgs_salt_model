import tensorflow as tf

tf.flags.DEFINE_string(
    'input', "../input/train", """path to train data""")

tf.flags.DEFINE_string(
    'model', '../output/model', """path to model directory""")

tf.flags.DEFINE_enum(
    'adjust', 'symmetric', enum_values=['resize', 'reflect', 'constant', 'symmetric'], help="""mode to adjust image size""")

tf.flags.DEFINE_integer(
    'cv', 0, help="""index of k-fold cross validation. index must be in 0~9""")

tf.flags.DEFINE_integer(
    'batch_size', 32, """batch size""")

tf.flags.DEFINE_enum(
    'loss', 'bce-dice', enum_values=['bce', 'bce-dice', 'lovasz', 'lovasz-dice', 'lovasz-inv', 'lovasz-double'], help="""loss type""")

tf.flags.DEFINE_enum(
    'lovasz_pattern', 'elu(error)+1',
    enum_values=['elu(error)', 'elu(error+1)', 'elu(error+5)', 'elu(error)+1', 'elu(error+1)+1'],
    help="""lovasz loss pattern""")

tf.flags.DEFINE_bool('deep_supervised', False, """whether to use deep-supervised model""")

tf.flags.DEFINE_bool('with_depth', False, """whether to use depth information""")

