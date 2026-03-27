#### Use a Python library, specifically `scikit-learn`, within MATLAB. We'll perform a simple linear regression using Python's `scikit-learn` from MATLAB.

1. **Install scikit-learn:**
   Ensure that you have `scikit-learn` installed in your Python environment. You can install it using:

   ```bash
   pip install scikit-learn
   ```

2. **Create a Python Script:**
   Create a Python script named `linear_regression.py` with the following content:

   ```python
   # linear_regression.py
   from sklearn.linear_model import LinearRegression
   import numpy as np
   import matlab.engine

   def perform_linear_regression(x, y):
       # Reshape the input data if needed
       x = np.array(x).reshape(-1, 1)
       y = np.array(y)

       # Create and train the linear regression model
       model = LinearRegression()
       model.fit(x, y)

       # Return the coefficients (slope and intercept)
       return model.coef_[0], model.intercept_

   if __name__ == "__main__":
       # Example data
       x_data = [1, 2, 3, 4, 5]
       y_data = [2, 4, 5, 4, 5]

       # Perform linear regression
       slope, intercept = perform_linear_regression(x_data, y_data)

       # Print the results
       print("Slope:", slope)
       print("Intercept:", intercept)
   ```

3. **Call Python Script from MATLAB:**
   Now, let's call this Python script from MATLAB using the MATLAB Engine API. Create a MATLAB script or use the MATLAB command prompt:

   ```matlab
   % MATLAB script
   % Start MATLAB Engine
   eng = matlab.engine.start_matlab();

   % Define input data
   x_data = [1, 2, 3, 4, 5];
   y_data = [2, 4, 5, 4, 5];

   % Call the Python script
   [slope, intercept] = eng.python_call_linear_regression(x_data, y_data);

   % Display the results
   disp(['Slope: ' num2str(slope)]);
   disp(['Intercept: ' num2str(intercept)]);

   % Stop MATLAB Engine
   eng.quit();
   ```

   Save this MATLAB script in a file named, for example, `matlab_script.m`. In this script, we assume that you've added the current directory to MATLAB's path.

4. **Update Python Script for MATLAB Integration:**
   Update the `linear_regression.py` script to make it callable from MATLAB:

   ```python
   # linear_regression.py
   from sklearn.linear_model import LinearRegression
   import numpy as np
   import matlab.engine

   def perform_linear_regression(x, y):
       # Reshape the input data if needed
       x = np.array(x).reshape(-1, 1)
       y = np.array(y)

       # Create and train the linear regression model
       model = LinearRegression()
       model.fit(x, y)

       # Return the coefficients (slope and intercept)
       return model.coef_[0], model.intercept_

   if __name__ == "__main__":
       # Connect to MATLAB Engine
       eng = matlab.engine.start_matlab()

       # Get input data from MATLAB
       x_data = eng.eval("x_data", nargout=1)
       y_data = eng.eval("y_data", nargout=1)

       # Perform linear regression
       slope, intercept = perform_linear_regression(x_data, y_data)

       # Return the results to MATLAB
       eng.workspace['slope'] = slope
       eng.workspace['intercept'] = intercept
   ```

5. **Run the MATLAB Script:**
   Execute the MATLAB script (`matlab_script.m`). This will start the MATLAB Engine, call the Python script, retrieve the results, and display them in the MATLAB environment.

   ```matlab
   matlab_script
   ```

This example demonstrates how you can seamlessly integrate a Python script (using a popular machine learning library) into MATLAB and exchange data between the two environments. Adjust the code according to your specific requirements and data.