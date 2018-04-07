#import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("/tmp/data",one_hot=True)

n_nodes_hl1=10
n_nodes_hl2=10
n_nodes_hl3=10
n_classes=10
batch_size=100
#height x width
x=tf.placeholder('float',[None,784])
y=tf.placeholder('float')

def neural_net_model(data):
    # input_data x weights + biases
    hidden_layer_1={'weights':tf.Variable(tf.random_normal([784,n_nodes_hl1])),
    'biases':tf.Variable(tf.random_normal(n_nodes_hl1)}

    hidden_layer_2={'weights':tf.Variable(tf.random_normal([n_nodes_hl1,n_nodes_hl2])),
    'biases':tf.Variable(tf.random_normal(n_nodes_hl2)}

    hidden_layer_3={'weights':tf.Variable(tf.random_normal([n_nodes_hl2,n_nodes_hl3])),
    'biases':tf.Variable(tf.random_normal(n_nodes_hl3)}

    output_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl3,n_classes])),
    'biases':tf.Variable(tf.random_normal(n_classes)}

    l1=tf.add(tf.matmul(data,hidden_layer_1['weights']),hidden_layer_1['biases']))
    l1=tf.nn.relu(l1)

    l2=tf.add(tf.matmul(l1,hidden_layer_2['weights']),hidden_layer_2['biases']))
    l2=tf.nn.relu(l2)

    l3=tf.add(tf.matmul(l2,hidden_layer_3['weights']),hidden_layer_3['biases']))
    l3=tf.nn.relu(l3)

    output=tf.add(tf.matmul(l3,output_layer['weights']),output_layer['biases']))
    return output

def train_neural_net(x):
    prediction=neural_net_model(x)
    cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction,y))

    # learning rate = 0.001
    optimizer=tf.train.AdamOptimizer().minimize(cost)

    hm_epochs=5
    with tf.Session as sess:
        #start session
        see.run(tf.initialize_all_variables())

        for epoch in range(hm_epochs):
            epoch_loss=0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                x,y=mnist.train.next.batch(batch_size)
                _,c=sess.run([optimizer,cost],feed_dict={x:x,y:y})
                epoch_loss+=c
            print('Epoch',epoch+1,'completed out of ',hm_epochs,'loss:',epoch_loss)
        correct=tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))
        accuracy=tf.reduce(tf.cast(correct,'float'))
        print('Accuracy:',accuracy.eval({x:mnist.test.images,y:.mnist.test.images.labels}))

train_neural_net(x)

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello).decode())
