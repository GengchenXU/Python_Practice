'''
Description: 
Sample Intput: 
Output: 
Author: GengchenXu
CreateDate: 2020-07-11 12:35:00
LastEditTime: 2021-10-29 22:30:36
'''
import tensorflow as tf

hello = tf.constant('Hello tensorfolw')
sess = tf.Session()
print(sess.run(hello))