# Date : 2023/03/10
# Title: Pytorch Tensor Tutorial

# Import Library
import torch
import numpy as np

# 1. Initialize Tensor

# 1.1 Generate directly from data
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(f"x_data: \n {x_data} \n")

# 1.2 Generate from NumPy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"x_np: \n {x_np} \n")

# 1.3 Generate from other tensor --> Generate based on Shape of Tensor
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

# 1.4 Using random or constant value
shape = (2, 3,) # (Row, Columns, )
rand_tensor = torch.rand(shape) # When the parameter is shape.
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

# 2. Tensor's Attribute
shape2 = (3, 4, )
tensor = torch.rand(shape2)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# 3. Tensor Operation

# 3.1 Before operation, Using GPU
if torch.cuda.is_available():
    tensor = tensor.to('cuda:2')
    print(f"Device tensor is stored on: {tensor.device}")

# 3.2 Standard Indexing & Slicing
tensor = torch.ones(4, 4) # 4x4 크기의 ones tensor 생성
tensor[:, 1] = 0 # all row & 2nd column 의 값 0 설정
print(tensor)


# 3.3 Concatenate Tensor
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

# 3.4 Multiply Tensor

# 3.4.1 element-wise product
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
print(f"tensor * tensor \n {tensor * tensor}")

# 3.4.2 matrix multiplication
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

# 3.5 In-place Operation
print(tensor, "\n")
tensor.add_(5) # _ 접미사를 갖는 연산은 in-place 연산(새로운 값 X, 기존 값 대체)
print(tensor)

# 4. Numpy Bridge(변환)
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

t.add_(1) # 텐서의 변경 사항이 numpy 배열에 반영
print(f"t: {t}")
print(f"n: {n}")

n = np.ones(5)
t = torch.from_numpy(n)

# numpy 배열의 변경 사항리 텐서에 반영
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")


