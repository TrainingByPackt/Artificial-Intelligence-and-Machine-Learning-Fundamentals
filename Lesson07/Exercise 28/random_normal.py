import tensorflow as tf

randomMatrix = tf.Variable(tf.random_normal([3, 4]))

with tf.Session() as session:
    initializer = tf.global_variables_initializer()
    session.run(initializer)
    print(session.run(randomMatrix))
