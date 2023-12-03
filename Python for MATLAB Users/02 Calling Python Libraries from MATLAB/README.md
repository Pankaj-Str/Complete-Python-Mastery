Calling Python libraries from MATLAB is possible through the use of the MATLAB Engine API for Python. This allows you to evaluate MATLAB functions and exchange data between MATLAB and Python. Here's a step-by-step example:

1. **Install MATLAB Engine API for Python:**
   Make sure you have MATLAB installed on your machine. After installation, navigate to the `matlabroot/extern/engines/python` directory and run the `setup.py` script to install the MATLAB Engine API for Python.

   ```bash
   cd matlabroot/extern/engines/python
   python setup.py install
   ```

   Replace `matlabroot` with the actual path to your MATLAB installation directory.

2. **Start MATLAB Engine from Python:**
   You can use the following Python code to start the MATLAB Engine:

   ```python
   import matlab.engine

   eng = matlab.engine.start_matlab()
   ```

3. **Call MATLAB Functions from Python:**
   Once the MATLAB Engine is started, you can call MATLAB functions from Python. For example, let's create a simple MATLAB function named `multiply` that multiplies two numbers:

   ```matlab
   % save this MATLAB function in a file named multiply.m
   function result = multiply(a, b)
       result = a * b;
   end
   ```

   Now, you can call this function from Python:

   ```python
   result = eng.multiply(3, 4)
   print(result)
   ```

4. **Exchange Data:**
   You can also exchange data between Python and MATLAB. For example, sending a NumPy array from Python to MATLAB:

   ```python
   import numpy as np

   # Create a NumPy array
   arr = np.array([[1, 2, 3], [4, 5, 6]])

   # Send the array to MATLAB
   mat_arr = matlab.double(arr.tolist())
   eng.workspace['mat_arr'] = mat_arr

   # Call a MATLAB function that uses the array
   eng.eval("result = sum(mat_arr);", nargout=0)

   # Retrieve the result from MATLAB
   result = eng.workspace['result']
   print(result)
   ```

   Here, the NumPy array is converted to a MATLAB double array before being sent to MATLAB.

5. **Stop MATLAB Engine:**
   After you're done using the MATLAB Engine, stop it to release resources:

   ```python
   eng.quit()
   ```

Remember to adjust file paths, function names, and variable names based on your specific use case. This example assumes MATLAB is properly installed and configured on your system.