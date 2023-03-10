# Pytorch Tensor

## Date : 2023/03/10

## 1. Tensor

### 1.1 What is the 'Tensor'?
- 텐서는 Pytorch에서 사용할 수 있는 자료구조로서 배열, 행렬과 유사하다.

### 1.2 How to make Tensor?
- 텐서를 초기화하는 방법은 크게 4가지이다.

 - 데이터로부터 직접 생성하기
 - Numpy 배열로부터 생성하기
 - 다른 텐서로부터 생성하기
 - 무작위 또는 상수 값 사용해 생성하기

### 1.3 Tensor's Attribute
- 텐서의 속성은 3가지이다.

 - shape : 텐서의 행렬
 - dtype : 텐서의 데이터 타입
 - device : 텐서가 저장된 장치(cpu or cuda)

### 1.4 Tensor's Operation
- Tensor 연산을 진행하기 전 체크해야 할 사항: CUDA 설정
- torch.cuda.is_available() : True or False
- tensor.to('cuda:2')

 - Indexing & Slicing
 - Concatenate
 - Multiply(element-wise product & matrix multiplication)
 - In-place

### 1.5 Numpy Bridge
- Tensor << ---- >> Numpy 변환
- tensor.numpy()
- torch.from_numpy(numpy_array)
- 이렇게 생성된 Tensor or Numpy들은 origin data 값의 변동에 영향을 받음

