
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected,flatten
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization

def pilotnet(width,height,lr):
    network = input_data(shape=[None,width,height,1],name='input')
    network = conv_2d(network,nb_filter=24,filter_size=(5,5),strides=(2,2),activation='elu')
    network = conv_2d(network,nb_filter=36,filter_size=(5,5),strides=(2,2),activation='elu')
    network = conv_2d(network,nb_filter=48,filter_size=(5,5),strides=(2,2),activation='elu')
    network = conv_2d(network,nb_filter=64,filter_size=(3,3),activation='elu')
    network = conv_2d(network,nb_filter=64,filter_size=(3,3),activation='elu')
    network = flatten(network)
    network = fully_connected(network,100)
    network = fully_connected(network,50)
    network = fully_connected(network,10)
    network = fully_connected(network,2)
    network = regression(network,optimizer='adam',loss='mean_square',learning_rate=lr,name='targets')

    model = tflearn.DNN(network,checkpoint_path='model_pilotNet',
                          max_checkpoints=1,tensorboard_verbose=0,tensorboard_dir='log')

    return model