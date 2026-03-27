### Calling a Python library for image processing from MATLAB. In this case, we'll use Python's OpenCV library to perform edge detection on an image from within MATLAB.

1. **Install OpenCV:**
   Make sure you have OpenCV installed in your Python environment. You can install it using:

   ```bash
   pip install opencv-python
   ```

2. **Create a Python Script:**
   Create a Python script named `edge_detection.py` with the following content:

   ```python
   # edge_detection.py
   import cv2
   import matlab.engine
   import numpy as np

   def perform_edge_detection(image_path):
       # Read the image
       img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

       # Perform Canny edge detection
       edges = cv2.Canny(img, 50, 150)

       # Return the resulting edges
       return edges

   if __name__ == "__main__":
       # Connect to MATLAB Engine
       eng = matlab.engine.start_matlab()

       # Get the image path from MATLAB
       image_path = eng.eval("image_path", nargout=1)

       # Perform edge detection
       edges_result = perform_edge_detection(image_path)

       # Return the results to MATLAB
       eng.workspace['edges_result'] = matlab.double(edges_result.tolist())
   ```

3. **Call Python Script from MATLAB:**
   Create a MATLAB script or use the MATLAB command prompt:

   ```matlab
   % MATLAB script
   % Start MATLAB Engine
   eng = matlab.engine.start_matlab();

   % Define the image path
   image_path = 'path/to/your/image.jpg';

   % Call the Python script
   eng.eval("image_path = '" + image_path + "';", nargout=0);
   eng.eval("run('edge_detection.py');", nargout=0);

   % Retrieve the results
   edges_result = eng.workspace('edges_result');

   % Display the original and edges images in MATLAB
   original_image = imread(image_path);
   figure;
   subplot(1, 2, 1); imshow(original_image); title('Original Image');
   subplot(1, 2, 2); imshow(uint8(edges_result)); title('Edges');

   % Stop MATLAB Engine
   eng.quit();
   ```

   Save this MATLAB script in a file named, for example, `image_processing.m`. Make sure to replace `'path/to/your/image.jpg'` with the actual path to an image file on your system.

4. **Run the MATLAB Script:**
   Execute the MATLAB script (`image_processing.m`). This will start the MATLAB Engine, call the Python script for edge detection, retrieve the results, and display the original and edges images in the MATLAB environment.

   ```matlab
   image_processing
   ```

This example demonstrates the integration of a Python script using OpenCV for image processing within MATLAB. It showcases the ability to pass parameters between MATLAB and Python, execute Python scripts, and retrieve the results for further analysis or visualization in the MATLAB environment. 