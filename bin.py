import tensorflow as tf
import sys

def printPersonality(personalityNumber):
    personalities = [ 'Sportive', 'Geek', 'Artist', 'Nightlife', 'Crazy' ];
    print(personalities[personalityNumber[0]]);

x_data = [
    [2, 0, 3, 1, 4],
    [2, 4, 3, 1, 4],
    [2, 1, 3, 1, 1],
    [0, 1, 2, 2, 3],
    [0, 1, 0, 2, 0],
    [0, 0, 1, 2, 0],
    [1, 2, 2, 4, 1],
    [3, 2, 3, 4, 3],
    [1, 4, 2, 4, 1],
    [4, 4, 1, 0, 3],
    [4, 0, 1, 0, 3],
    [3, 4, 1, 0, 3],
    [3, 3, 4, 3, 2],
    [3, 3, 3, 3, 2],
    [3, 3, 4, 3, 4],
]
y_data = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
]

questionCount = 5
personalities = 5

X = tf.placeholder("float", [None, questionCount])
Y = tf.placeholder("float", [None, personalities])
nb_classes = personalities
W = tf.Variable(tf.random_normal([questionCount, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name="bias")
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(5000):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
    d = sess.run(hypothesis, feed_dict={ X: [[float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])]]})
    printPersonality(sess.run(tf.argmax(d, 1)))