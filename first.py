import numpy as np
from numba import cuda

@cuda.jit
def square_array(array):
    # Get the thread ID
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    # Get the block size
    block_size = cuda.blockDim.x
    # Get the grid size
    grid_size = cuda.gridDim.x

    start = tx + ty * block_size
    stride = block_size * grid_size

    for i in range(start, array.size, stride):
        array[i] *= array[i]




# Create an array of 100 elements
arr = np.array([1, 2, 3, 4, 5], dtype=np.float32)
array = cuda.to_device(arr)

threadsperblock = 32
blockspergrid = (array.size + (threadsperblock - 1)) // threadsperblock
# Launch the kernel
square_array[blockspergrid, threadsperblock](array)

# Copy the result back to the host
result = array.copy_to_host()

# Print the result
print(result)
