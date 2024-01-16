# Difference Between Constructor and Destructor


| Feature       | Constructor                   | Destructor                    |
|---------------|-------------------------------|-------------------------------|
| **Name**      | `__init__`                    | `__del__`                     |
| **Purpose**   | Initializes object attributes | Performs cleanup operations   |
| **Invocation**| Automatically called on object creation | Automatically called before object destruction (not guaranteed) |
| **Syntax**    | `def __init__(self, ...)`:     | `def __del__(self):`          |
| **Usage**     | Initialize object properties   | Release resources, close files, etc. |
| **Common**    | Commonly used in every class   | Not commonly used due to automatic garbage collection |
| **Example**   | ```python                    | ```python                     |
|               | def __init__(self, x, y):     | def __del__(self):            |
|               |     self.x = x               |     # cleanup operations     |
|               |     self.y = y               | ```                           |
