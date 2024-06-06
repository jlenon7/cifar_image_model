import random
import numpy as np
import matplotlib.pyplot as plt
from helpers import get_df, load_model

(X_train, y_train), (X_test, y_test) = get_df()

X_test = X_test / 255

model = load_model()

index = random.randint(0, len(X_test))
cifarCategories = {
  0: 'airplane',
  1: 'automobile',
  2: 'bird',
  3: 'cat',
  4: 'deer',
  5: 'dog',
  6: 'frog',
  7: 'horse',
  8: 'ship',
  9: 'truck'
}

img = X_test[index]
category = cifarCategories[y_test[index][0]]

print(f"Image is originally from {category} category")
plt.imshow(img)

prediction = model.predict(img.reshape(1, 32, 32, 3), verbose=0)
prediction = np.argmax(prediction, axis=1)

print(f"Model predicted that image is from {cifarCategories[prediction[0]]} category")
print("Image has been oppened in your machine. Close it to exit the program")

plt.show()
