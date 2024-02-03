# Python Package

**Python Package Types:**

In Python, a package is a way of organizing related modules into a single directory hierarchy. Packages allow you to create a modular and organized structure for your codebase. There are two main types of Python packages:

1. **Regular Packages:**

   Regular packages are simply directories that contain a special `__init__.py` file (which can be empty) and one or more module files (Python files). The `__init__.py` file is executed when the package is imported and can contain package-level initialization code. Regular packages allow you to group related modules together.

   Example directory structure:
   ```
   my_package/
   ├── __init__.py
   ├── module1.py
   └── module2.py
   ```

2. **Namespace Packages:**

   Namespace packages are used to split a single logical package across multiple directories. They allow you to create a package from modules that are distributed across different locations, possibly in different Python packages or libraries. Namespace packages don't require an `__init__.py` file, and they are automatically merged at runtime.

   Example directory structure:
   ```
   my_namespace_package/
   ├── module1.py
   └── module2.py
   ```

**Python Package Adding:**

To create and add packages to your Python project, follow these steps:

1. **Create a Directory:**

   Create a directory that will serve as your package's root directory. You can name it anything you like.

   ```
   my_package/
   ```

2. **Add Module Files:**

   Inside the package directory, add module files (Python files) that contain your code. These modules should have a `.py` file extension.

   ```
   my_package/
   ├── __init__.py
   ├── module1.py
   └── module2.py
   ```

3. **Add an `__init__.py` File (for Regular Packages):**

   In regular packages, you should have an `__init__.py` file (which can be empty) in the package's root directory. This file is executed when the package is imported and can contain package-level initialization code.

4. **Create Subpackages (Optional):**

   You can create subpackages by adding subdirectories with their own `__init__.py` files and module files inside the package directory. This allows you to organize your code hierarchically.

   ```
   my_package/
   ├── __init__.py
   ├── module1.py
   ├── module2.py
   └── subpackage/
       ├── __init__.py
       ├── submodule1.py
       └── submodule2.py
   ```

5. **Import and Use Your Package:**

   You can import and use your package and its modules in your Python code as follows:

   ```python
   import my_package.module1
   from my_package import module2

   my_package.module1.function_from_module1()
   module2.function_from_module2()
   ```

   You can also use relative imports within your package to import modules and submodules.

That's how you create and add packages to your Python project. Organizing your code into packages makes it more manageable, modular, and easier to maintain, especially in larger projects.