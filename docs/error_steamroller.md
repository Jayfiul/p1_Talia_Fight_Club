# Error Steamroller
I personally use the library `fuckit` to steamroll errors that may occur during execution. This is a nice and easy-to-use hack for when you don't want to deal with errors or implement long, complex error handling code. It's also useful for when you're just testing out a new library and don't want to deal with errors that may occur.

## Usage
```python
import fuckit

# Suppress all errors from the library "library_to_import"
fuckit("library_to_import")

# Function decorator that suppresses all errors from the function
@fuckit
def function_that_may_error():
    # Do something that may error
    some_undefined_variable

# It can be chained if one doesn't do the trick
fuckit(fuckit("library_to_import"))
```