# -*- coding: utf-8 -*-

import tensorflow as tf
import config

tf.flags.DEFINE_enum(
    'adjust', 'resize', enum_values=['resize', 'pad'], help="""mode to adjust image 101=>128""")