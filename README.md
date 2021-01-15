# Knowledge of python data type conversion

***Key Points***

1. Type Conversion is the conversion of object from one data type to another data type.
2. Implicit Type Conversion is automatically performed by the Python interpreter.
3. Python avoids the loss of data in Implicit Type Conversion.
4. Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
5. In Type Casting, loss of data may occur as we enforce the object to a specific data type.

**Implicit Type Conversion**

- In Implicit type conversion, Python automatically converts one data type to another data type.
- This process doesn't need any user involvement.
- Example: 

            a = 5
            b = 5.5
            sum = a + b
            print (sum)
            print (type (sum)) #type() is used to display the datatype of a variable

            Output:
            10.5
            <class ‘float’>

**Explicit Type Conversion**

- In Explicit Type Conversion, users convert the data type of an object to required data type.
- We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
- Syntax for explicit type conversion:

        (required_data type)(expression)
        
- Example:

            a = 5
            b = 5.5
            sum = int(a + b) # type conversion to integer type
            print (sum)
            print (type (sum)) 

            Output:
            10
            <class 'int'>
            
- Following table contains some of the in-built functions for type conversion, along with their descriptions.

| Function |	Description     |
|----------|--------------------|
| int(y [base]) |	It converts y to an integer, and Base specifies the number base. For example, if you want to convert the string in decimal number then you’ll use 10 as base.
| float(y)	| It converts y to a floating-point number.
| complex(real [imag])  | It creates a complex number.
| str(y) |	It converts y to a string.
| tuple(y) |	It converts y to a tuple.
| list(y)	| It converts y to a list.
| set(y)| 	It converts y to a set.
| dict(y)|	It creates a dictionary and y should be a sequence of (key,value) tuples.
| ord(y)|	It converts a character into an integer.
| hex(y)|	It converts an integer to a hexadecimal string.
| oct(y)|	It converts an integer to an octal string
        