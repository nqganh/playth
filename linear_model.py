import tensorflow as tf
import numpy as np

# number of epochs
num_epoch = 100

# training data
x = np.array([0., 1., 2., 3.], dtype=np.float32).reshape(-1, 1)
y = np.array([2., 3., 4., 5.], dtype=np.float32).reshape(-1, 1)

# test data
x_test = x + 0.5
y_test = y + 0.5

# Create trainable variables
W = tf.Variable(tf.random.normal([1, 1], stddev=0.1))
B = tf.Variable(tf.constant(0.1, shape=[1]))

# learning rate & optimizer
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

# RMS loss (same as sqrt(MSE), constant 1/2 removed for simplicity)
def rms_loss(y_true, y_pred):
    return tf.sqrt(tf.reduce_mean(tf.square(y_true - y_pred)))

# model
def model(x):
    return x * W + B

# training loop
for epoch in range(num_epoch):
    with tf.GradientTape() as tape:
        y_pred = model(x)
        loss_value = rms_loss(y, y_pred)

    # compute gradients
    grads = tape.gradient(loss_value, [W, B])
    optimizer.apply_gradients(zip(grads, [W, B]))

    print(f"Epoch {epoch}: loss = {loss_value.numpy():.4f}")

# Test model
y_pred_test = model(x_test)

print("\nGround truth y:", y_test.flatten())
print("Predicted y   :", y_pred_test.numpy().flatten())
print("\nLearned W =", W.numpy())
print("Learned B =", B.numpy())
