import tensorflow as tf

input1 = tf.constant(2.0, tf.float32, name='input1')
input2 = tf.constant(3.0, tf.float32, name='input2')
input3 = tf.constant(4.0, tf.float32, name='input3')
product12 = tf.multiply(input1, input2)
sum = tf.add(product12, input3)

with tf.Session() as session:
    print(session.run(product12))
    print(session.run(sum))
