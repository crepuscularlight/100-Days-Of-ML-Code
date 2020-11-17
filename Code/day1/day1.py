import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import sklearn

dataset=pd.read_csv("./data.csv")
# print(dataset[dataset["age"]>3])
# print(dataset.dtypes)
# print(dataset.iloc[1:10,0:2])
# dataset.iloc[1:10,2].plot()


# x=np.array([1,2,3,4,5])
# y=np.array([2,3,4,5,6])

# fig=plt.scatter(x,y)
# plt.show()



# x=pd.DataFrame({ "Name":["Braund, Mr. Owen Harris", \
#     "Allen, Mr. William Henry",              \
#         "Bonnell, Miss. Elizabeth"],  \
#             "Age":[22, 35, 58],   \
#                 "Sex":["male", "male", "female"]})
# y=pd.DataFrame({"Name":["LiudiYang","YuchanMa"],\
#     "Age":[14,22],\
#     "wage":[1111,1234]}
#     )

# z=pd.Series({"Name":["LiudiYang","YuchanMa","Gaojiaqi"]})
# print(y["Age"].max())
# print(z.max())

'''fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
print(fig)
print(ax)
plt.show()'''

ax=plt.subplot(2,2,1)
ax.plot([1, 2, 3, 4], [1, 4, 2,4])
ax.plot([1, 2, 3, 4])
ax.set_title(1)
fig=plt.figure()
ax2=plt.subplot(2,2,4)
ax2.plot([1, 2, 3, 4], [1, 4, 2,4])
ax2.set_xlabel("afs")
plt.show()