import numpy as np

first_data = np.load("new_train_data_0.npy",allow_pickle=True)

# second_data = np.load("new_train_data_1.npy",allow_pickle=True)
for i in range(1,20):
    file_name = "new_train_data_{}.npy".format(i)
    train_data = np.load(file_name,allow_pickle=True)
    first_data=np.append(first_data,train_data,0)

whole_data = first_data

print(len(whole_data))

# train_model(whole_data)