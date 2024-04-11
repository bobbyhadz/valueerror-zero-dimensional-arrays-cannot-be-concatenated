# ValueError: zero-dimensional arrays cannot be concatenated

import numpy as np

arr = np.array([1, 2, 3])

new_array = np.concatenate([arr])

print(new_array)  # 👉️ [1 2 3]