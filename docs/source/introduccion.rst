Introduccion al Lenguaje de Programacion Python
===============================================

https://en.wikipedia.org/wiki/Python_%28programming_language%29

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[34]

Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language, and he first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[36]

Python consistently ranks as one of the most popular programming languages, and it has gained widespread use in the machine learning community.[37][38][39][40] It is widely taught as an introductory programming language.[41]
History
Main article: History of Python
The designer of Python, Guido van Rossum, at PyCon US 2024

Python was conceived in the late 1980s[42] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands; it was conceived as a successor to the ABC programming language, which was inspired by SETL,[43] capable of exception handling and interfacing with the Amoeba operating system.[13] Python implementation began in December, 1989.[44] Van Rossum assumed sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from responsibilities as Python's "benevolent dictator for life" (BDFL); this title was bestowed on him by the Python community to reflect his long-term commitment as the project's chief decision-maker.[45] (He has since come out of retirement and is self-titled "BDFL-emeritus".) In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[46][47]

The name Python is said to derive from the British comedy series Monty Python's Flying Circus.[48]

Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 2.7's end-of-life was initially set for 2015, and then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[50][51] It no longer receives security patches or updates.[52][53] While Python 2.7 and older versions are officially unsupported, a different unofficial Python implementation, PyPy, continues to support Python 2, i.e., "2.7.18+" (plus 3.10), with the plus signifying (at least some) "backported security updates".[54]

Python 3.0 was released on 3 December 2008, with some new semantics and changed syntax. Several releases in the Python 3.x series have added new syntax to the language; a few releases in 3.x have also removed outdated modules.

As of 11 June 2025, Python 3.13.5 is the latest stable release, and is the only Python version to get bugfixes (it is highly recommended to upgrade to it, or upgrade to any other recent version past Python 3.9). This version currently receives full bug-fix and security updates, while Python 3.12—released in October 2023—had active bug-fix support only until April 2025, and since then only security fixes. Python 3.9[55] is the oldest supported version of Python (albeit in the 'security support' phase), because Python 3.8 has become an end-of-life product.[56][57] Starting with Python 3.13, it and later versions receive two years of full support (which has increased from one and a half years), followed by three years of security support; this is the same total duration of support as previously.

Security updates were expedited in 2021 and again twice in 2022. More issues were fixed in 2023 and in September 2024 (for Python versions 3.8.20 through 3.12.6)—all versions (including 2.7)[58] had been insecure because of issues leading to possible remote code execution[59] and web-cache poisoning.[60]

Python 3.10 added the | union type operator[61] and added structural pattern matching capability to the language, with the new match and case keywords.[62] Python 3.11 expanded exception handling functionality. Python 3.12 added the new keyword type. Notable changes from version 3.10 to 3.11 include increased program execution speed and improved error reporting.[63] Python 3.11 is claimed to be 10–60% faster than Python 3.10, and Python 3.12 increases by an additional 5%. Python 3.12 also includes improved error messages (again improved in 3.14) and many other changes.

Python 3.13 introduced more syntax for types; a new and improved interactive interpreter (REPL), featuring multi-line editing and color support; an incremental garbage collector, which results in shorter pauses for collection in programs that have many objects, as well as increasing the improved speed in 3.11 and 3.12); an experimental just-in-time (JIT) compiler (such features need to be enabled specifically for the increase in speed);[64] and an experimental free-threaded build mode, which disables the global interpreter lock (GIL), allowing threads to run more concurrently, as enabled in python3.13t or python3.13t.exe.

Python Enhancement Proposal (PEP) 711 proposes PyBI—a standard format for distributing Python binaries.[65]

Python 3.14.0 is now in the release candidate 1 phase (introduces e.g. a new opt-in interpreter, up to 30% faster).

Python 3.15 will "Make UTF-8 mode default";[66] This mode is supported in all current Python versions, but it currently must be opted into. UTF-8 is already used by default on Windows (and other operating systems) for most purposes; an exception is opening files. Enabling UTF-8 also makes code fully cross-platform.

Potentially breaking changes

Python 3.0 introduced very breaking changes, but all breaking changes in 3.x discussed below, are designed to affect few users.

Python 3.12 dropped some outdated modules, and more will be dropped in the future, deprecated as of 3.13; already deprecated array 'u' format code will emit DeprecationWarning since 3.13 and will be removed in Python 3.16. The 'w' format code should be used instead. Part of ctypes is also deprecated and http.server.CGIHTTPRequestHandler will emit a DeprecationWarning, and will be removed in 3.15. Using that code already has a high potential for both security and functionality bugs. Parts of the typing module are deprecated, e.g. creating a typing.NamedTuple class using keyword arguments to denote the fields and such (and more) will be disallowed in Python 3.15. Python 3.12 removed wstr meaning Python extensions[67] need to be modified.[68]

Python 3.13 introduces some changes in behavior, i.e., new "well-defined semantics", fixing bugs, and removing many deprecated classes, functions and methods (as well as some of the Python/C API and outdated modules). "The old implementation of locals() and frame.f_locals was slow, inconsistent and buggy, and it had many corner cases and oddities. Code that works around those may need revising; code that uses locals() for simple templating or print debugging should continue to work correctly."[69]

Python 3.13 introduces the experimental free-threaded build mode, which disables the Global Interpreter Lock (GIL); the GIL is a feature of CPython that previously prevented multiple threads from executing Python bytecode simultaneously. This optional build, introduced through PEP 703, enables better exploitation of multi-core CPUs. By allowing multiple threads to run Python code in parallel, the free-threaded mode addresses long-standing performance bottlenecks associated with the GIL. This change offers a new path for parallelism in Python, without resorting to multiprocessing or external concurrency frameworks.[70]

Regarding annotations in upcoming Python version: "In Python 3.14, from __future__ import annotations will continue to work as it did before, converting annotations into strings."[71]

Python 3.14 drops the PGP digital verification signatures, it had deprecated in version 3.11, when its replacement Sigstore was added for all CPython artifacts; the use of PGP has been criticized by security practitioners.[72]

Some additional standard-library modules will be removed in Python 3.15 or 3.16, as will be many deprecated classes, functions and methods.[73][74]
Design philosophy and features

Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of their features support functional programming and aspect-oriented programming (including metaprogramming[75] and metaobjects).[76] Many other paradigms are supported via extensions, including design by contract[77][78] and logic programming.[79] Python is often referred to as a 'glue language'[80] because it can seamlessly integrate components written in other languages.

Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management.[81] It uses dynamic name resolution (late binding), which binds method and variable names during program execution.

Python's design offers some support for functional programming in the Lisp tradition. It has filter,mapandreduce functions; list comprehensions, dictionaries, sets, and generator expressions.[82] The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.[83]

Python's core philosophy is summarized in the Zen of Python (PEP 20), which includes aphorisms such as these:[84]

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Readability counts.

However, Python features regularly violate these principles and have received criticism for adding unnecessary language bloat.[85] Responses to these criticisms note that the Zen of Python is a guideline rather than a rule.[86] The addition of some new features had been controversial: Guido van Rossum resigned as Benevolent Dictator for Life after conflict about adding the assignment expression operator in Python 3.8.[87][88]

Nevertheless, rather than building all functionality into its core, Python was designed to be highly extensible via modules. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which represented the opposite approach.[42]

Python claims to strive for a simpler, less-cluttered syntax and grammar, while giving developers a choice in their coding methodology. In contrast to Perl's motto "there is more than one way to do it", Python advocates an approach where "there should be one—and preferably only one—obvious way to do it.".[84] In practice, however, Python provides many ways to achieve a given goal. There are, for example, at least three ways to format a string literal, with no certainty as to which one a programmer should use.[89] Alex Martelli is a Fellow at the Python Software Foundation and Python book author; he wrote that "To describe something as 'clever' is not considered a compliment in the Python culture."[90]

Python's developers usually try to avoid premature optimization; they also reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity.[91] Execution speed can be improved by moving speed-critical functions to extension modules written in languages such as C, or by using a just-in-time compiler like PyPy. It is also possible to cross-compile to other languages; but this approach either fails to achieve the expected speed-up, since Python is a very dynamic language, or only a restricted subset of Python is compiled (with potential minor semantic changes).[92]

Python's developers aim for the language to be fun to use. This goal is reflected in the name—a tribute to the British comedy group Monty Python[93]—and in playful approaches to some tutorials and reference materials. For instance, some code examples use the terms "spam" and "eggs" (in reference to a Monty Python sketch), rather than the typical terms "foo" and "bar".[94][95] A common neologism in the Python community is pythonic, which has a wide range of meanings related to program style. Pythonic code may use Python idioms well; be natural or show fluency in the language; or conform with Python's minimalist philosophy and emphasis on readability.[96]
Syntax and semantics
Main article: Python syntax and semantics
Block of Python code showing sample source code
An example of Python code and indentation
C code featuring curly braces and semicolon
Example of C# code with curly braces and semicolons

Python is meant to be an easily readable language. Its formatting is visually uncluttered and often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are allowed but rarely used. It has fewer syntactic exceptions and special cases than C or Pascal.[97]
Indentation
Main article: Python syntax and semantics § Indentation

Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.[98] Thus, the program's visual structure accurately represents its semantic structure.[99] This feature is sometimes termed the off-side rule. Some other languages use indentation this way; but in most, indentation has no semantic meaning. The recommended indent size is four spaces.[100]
Statements and control flow

Python's statements include the following:

    The assignment statement, using a single equals sign =
    The if statement, which conditionally executes a block of code, along with else and elif (a contraction of else if)
    The for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block
    The while statement, which executes a block of code as long as boolean condition is true
    The try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses (or new syntax except* in Python 3.11 for exception groups[101]); the try statement also ensures that clean-up code in a finally block is always run regardless of how the block exits
    The raise statement, used to raise a specified exception or re-raise a caught exception
    The class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming
    The def statement, which defines a function or method
    The with statement, which encloses a code block within a context manager, allowing resource-acquisition-is-initialization (RAII)-like behavior and replacing a common try/finally idiom[102] Examples of a context include acquiring a lock before some code is run, and then releasing the lock; or opening and then closing a file
    The break statement, which exits a loop
    The continue statement, which skips the rest of the current iteration and continues with the next
    The del statement, which removes a variable—deleting the reference from the name to the value, and producing an error if the variable is referred to before it is redefined [c]
    The pass statement, serving as a NOP (i.e., no operation), which is syntactically needed to create an empty code block
    The assert statement, used in debugging to check for conditions that should apply
    The yield statement, which returns a value from a generator function (and also an operator); used to implement coroutines
    The return statement, used to return a value from a function
    The import and from statements, used to import modules whose functions or variables can be used in the current program
    The match and case statements, analogous to a switch statement construct, which compares an expression against one or more cases as a control-flow measure

The assignment statement (=) binds a name as a reference to a separate, dynamically allocated object. Variables may subsequently be rebound at any time to any object. In Python, a variable name is a generic reference holder without a fixed data type; however, it always refers to some object with a type. This is called dynamic typing—in contrast to statically-typed languages, where each variable may contain only a value of a certain type.

Python does not support tail call optimization or first-class continuations; according to Van Rossum, the language never will.[103][104] However, better support for coroutine-like functionality is provided by extending Python's generators.[105] Before 2.5, generators were lazy iterators; data was passed unidirectionally out of the generator. From Python 2.5 on, it is possible to pass data back into a generator function; and from version 3.3, data can be passed through multiple stack levels.[106]
Expressions

Python's expressions include the following:

    The +, -, and * operators for mathematical addition, subtraction, and multiplication are similar to other languages, but the behavior of division differs. There are two types of division in Python: floor division (or integer division) //, and floating-point division /.[107] Python uses the ** operator for exponentiation.
    Python uses the + operator for string concatenation. The language uses the * operator for duplicating a string a specified number of times.
    The @ infix operator is intended to be used by libraries such as NumPy for matrix multiplication.[108][109]
    The syntax :=, called the "walrus operator", was introduced in Python 3.8. This operator assigns values to variables as part of a larger expression.[110]
    In Python, == compares two objects by value. Python's is operator may be used to compare object identities (i.e., comparison by reference), and comparisons may be chained—for example, a <= b <= c.
    Python uses and, or, and not as Boolean operators.
    Python has a type of expression called a list comprehension, and a more general expression called a generator expression.[82]
    Anonymous functions are implemented using lambda expressions; however, there may be only one expression in each body.
    Conditional expressions are written as x if c else y.[111] (This is different in operand order from the c ? x : y operator common to many other languages.)
    Python makes a distinction between lists and tuples. Lists are written as [1, 2, 3], are mutable, and cannot be used as the keys of dictionaries (since dictionary keys must be immutable in Python). Tuples, written as (1, 2, 3), are immutable and thus can be used as the keys of dictionaries, provided that all of the tuple's elements are immutable. The + operator can be used to concatenate two tuples, which does not directly modify their contents, but produces a new tuple containing the elements of both. For example, given the variable t initially equal to (1, 2, 3), executing t = t + (4, 5) first evaluates t + (4, 5), which yields (1, 2, 3, 4, 5); this result is then assigned back to t—thereby effectively "modifying the contents" of t while conforming to the immutable nature of tuple objects. Parentheses are optional for tuples in unambiguous contexts.[112]
    Python features sequence unpacking where multiple expressions, each evaluating to something assignable (e.g., a variable or a writable property) are associated just as in forming tuple literal; as a whole, the results are then put on the left-hand side of the equal sign in an assignment statement. This statement expects an iterable object on the right-hand side of the equal sign to produce the same number of values as the writable expressions on the left-hand side; while iterating, the statement assigns each of the values produced on the right to the corresponding expression on the left.[113]
    Python has a "string format" operator % that functions analogously to printf format strings in the C language—e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2". In Python 2.6+ and 3+, this operator was supplemented by the format() method of the str class, e.g., "spam={0} eggs={1}".format("blah", 2). Python 3.6 added "f-strings": spam = "blah"; eggs = 2; f'spam={spam} eggs={eggs}'.[114]
    Strings in Python can be concatenated by "adding" them (using the same operator as for adding integers and floats); e.g., "spam" + "eggs" returns "spameggs". If strings contain numbers, they are concatenated as strings rather than as integers, e.g. "2" + "2" returns "22".
    Python supports string literals in several ways:
        Delimited by single or double quotation marks; single and double quotation marks have equivalent functionality (unlike in Unix shells, Perl, and Perl-influenced languages). Both marks use the backslash (\) as an escape character. String interpolation became available in Python 3.6 as "formatted string literals".[114]
        Triple-quoted, i.e., starting and ending with three single or double quotation marks; this may span multiple lines and function like here documents in shells, Perl, and Ruby.
        Raw string varieties, denoted by prefixing the string literal with r. Escape sequences are not interpreted; hence raw strings are useful where literal backslashes are common, such as in regular expressions and Windows-style paths. (Compare "@-quoting" in C#.)
    Python has array index and array slicing expressions in lists, which are written as a[key], a[start:stop] or a[start:stop:step]. Indexes are zero-based, and negative indexes are relative to the end. Slices take elements from the start index up to, but not including, the stop index. The (optional) third slice parameter, called step or stride, allows elements to be skipped or reversed. Slice indexes may be omitted—for example, a[:] returns a copy of the entire list. Each element of a slice is a shallow copy.

In Python, a distinction between expressions and statements is rigidly enforced, in contrast to languages such as Common Lisp, Scheme, or Ruby. This distinction leads to duplicating some functionality, for example:

    List comprehensions vs. for-loops
    Conditional expressions vs. if blocks
    The eval() vs. exec() built-in functions (in Python 2, exec is a statement); the former function is for expressions, while the latter is for statements

A statement cannot be part of an expression; because of this restriction, expressions such as list and dict comprehensions (and lambda expressions) cannot contain statements. As a particular case, an assignment statement such as a = 1 cannot be part of the conditional expression of a conditional statement.
Methods

Methods of objects are functions attached to the object's class; the syntax for normal methods and functions, instance.method(argument), is syntactic sugar for Class.method(instance, argument). Python methods have an explicit self parameter to access instance data, in contrast to the implicit self (or this) parameter in some object-oriented programming languages (e.g., C++, Java, Objective-C, Ruby).[115] Python also provides methods, often called dunder methods (because their names begin and end with double underscores); these methods allow user-defined classes to modify how they are handled by native operations including length, comparison, arithmetic, and type conversion.[116]
Typing
The standard type hierarchy in Python 3

Python uses duck typing, and it has typed objects but untyped variable names. Type constraints are not checked at definition time; rather, operations on an object may fail at usage time, indicating that the object is not of an appropriate type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are poorly defined (e.g., adding a number and a string) rather than quietly attempting to interpret them.

Python allows programmers to define their own types using classes, most often for object-oriented programming. New instances of classes are constructed by calling the class, for example, SpamClass() or EggsClass()); the classes are instances of the metaclass type (which is an instance of itself), thereby allowing metaprogramming and reflection.

Before version 3.0, Python had two kinds of classes, both using the same syntax: old-style and new-style.[117] Current Python versions support the semantics of only the new style.

Python supports optional type annotations.[5][118] These annotations are not enforced by the language, but may be used by external tools such as mypy to catch errors.[119][120] Mypy also supports a Python compiler called mypyc, which leverages type annotations for optimization.[121]
Summary of Python 3's built-in types Type 	Mutability 	Description 	Syntax examples
bool 	immutable 	Boolean value 	True
False
bytearray 	mutable 	Sequence of bytes 	bytearray(b'Some ASCII')
bytearray(b"Some ASCII")
bytearray([119, 105, 107, 105])
bytes 	immutable 	Sequence of bytes 	b'Some ASCII'
b"Some ASCII"
bytes([119, 105, 107, 105])
complex 	immutable 	Complex number with real and imaginary parts 	3+2.7j
3 + 2.7j
dict 	mutable 	Associative array (or dictionary) of key and value pairs; can contain mixed types (keys and values); keys must be a hashable type 	{'key1': 1.0, 3: False}
{}
types.EllipsisType 	immutable 	An ellipsis placeholder to be used as an index in NumPy arrays 	...
Ellipsis
float 	immutable 	Double-precision floating-point number. The precision is machine-dependent, but in practice it is generally implemented as a 64-bit IEEE 754 number with 53 bits of precision.[122] 	

1.33333
frozenset 	immutable 	Unordered set, contains no duplicates; can contain mixed types, if hashable 	frozenset([4.0, 'string', True])
int 	immutable 	Integer of unlimited magnitude[123] 	42
list 	mutable 	List, can contain mixed types 	[4.0, 'string', True]
[]
types.NoneType 	immutable 	An object representing the absence of a value, often called null in other languages 	None
types.NotImplementedType 	immutable 	A placeholder that can be returned from overloaded operators to indicate unsupported operand types. 	NotImplemented
range 	immutable 	An immutable sequence of numbers, commonly used for iterating a specific number of times in for loops[124] 	range(−1, 10)
range(10, −5, −2)
set 	mutable 	Unordered set, contains no duplicates; can contain mixed types, if hashable 	{4.0, 'string', True}
set()
str 	immutable 	A character string: sequence of Unicode codepoints 	'Wikipedia'
"Wikipedia"

"""Spanning
multiple
lines"""

tuple 	immutable 	Tuple, can contain mixed types 	(4.0, 'string', True)
('single element',)
()
Arithmetic operations

Python includes conventional symbols for arithmetic operators (+, -, *, /), the floor-division operator //, and the modulo operator %. (With the module operator, a remainder can be negative, e.g., 4 % -3 == -2.) Python also offers the ** symbol for exponentiation, e.g. 5**3 == 125 and 9**0.5 == 3.0; it also offers the matrix‑multiplication operator @ .[125] These operators work as in traditional mathematics; with the same precedence rules, the infix operators + and - can also be unary, to represent positive and negative numbers respectively.

Division between integers produces floating-point results. The behavior of division has changed significantly over time:[126]

    The current version of Python (i.e., since 3.0) changed the / operator to always represent floating-point division, e.g., 5/2 == 2.5.
    The floor division // operator was introduced. Thus 7//3 == 2, -7//3 == -3, 7.5//3 == 2.0, and -7.5//3 == -3.0. For outdated Python 2.7 adding the from __future__ import division statement causes a module in Python 2.7 to use Python 3.0 rules for division instead (see above).

In Python terms, the / operator represents true division (or simply division), while the // operator represents floor division. Before version 3.0, the / operator represents classic division.[126]

Rounding towards negative infinity, though a different method than in most languages, adds consistency to Python. For instance, this rounding implies that the equation (a + b)//b == a//b + 1 is always true. The rounding also implies that the equation b*(a//b) + a%b == a is valid for both positive and negative values of a. As expected, the result of a%b lies in the half-open interval [0, b), where b is a positive integer; however, maintaining the validity of the equation requires that the result must lie in the interval (b, 0] when b is negative.[127]

Python provides a round function for rounding a float to the nearest integer. For tie-breaking, Python 3 uses the round to even method: round(1.5) and round(2.5) both produce 2.[128] Python versions before 3 used the round-away-from-zero method: round(0.5) is 1.0, and round(-0.5) is −1.0.[129]

Python allows Boolean expressions that contain multiple equality relations to be consistent with general usage in mathematics. For example, the expression a < b < c tests whether a is less than b and b is less than c.[130] C-derived languages interpret this expression differently: in C, the expression would first evaluate a < b, resulting in 0 or 1, and that result would then be compared with c.[131]

Python uses arbitrary-precision arithmetic for all integer operations. The Decimal type/class in the decimal module provides decimal floating-point numbers to a pre-defined arbitrary precision with several rounding modes.[132] The Fraction class in the fractions module provides arbitrary precision for rational numbers.[133]

Due to Python's extensive mathematics library and the third-party library NumPy, the language is frequently used for scientific scripting in tasks such as numerical data processing and manipulation.[134][135]
Function syntax

Functions are created in Python by using the def keyword. A function is defined similarly to how it is called, by first providing the function name and then the required parameters. Here is an example of a function that prints its inputs:

def printer(input1, input2="already there"):
    print(input1)
    print(input2)
    
printer("hello")
    
# Example output:
# hello
# already there

To assign a default value to a function parameter in case no actual value is provided at run time, variable-definition syntax can be used inside the function header.
Code examples

"Hello, World!" program:

print('Hello, world!')

Program to calculate the factorial of a positive integer:

n = int(input('Type a number, and its factorial will be printed: '))

if n < 0:
    raise ValueError('You must enter a non-negative integer')

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(factorial)

Libraries

Python's large standard library[136] is commonly cited as one of its greatest strengths. For Internet-facing applications, many standard formats and protocols such as MIME and HTTP are supported. The language includes modules for creating graphical user interfaces, connecting to relational databases, generating pseudorandom numbers, arithmetic with arbitrary-precision decimals,[132] manipulating regular expressions, and unit testing.

Some parts of the standard library are covered by specifications—for example, the Web Server Gateway Interface (WSGI) implementation wsgiref follows PEP 333[137]—but most parts are specified by their code, internal documentation, and test suites. However, because most of the standard library is cross-platform Python code, only a few modules must be altered or rewritten for variant implementations.

As of 13 March 2025, the Python Package Index (PyPI), the official repository for third-party Python software, contains over 614,339[138] packages. These have a wide range of functionality, including the following:

    Automation
    Data analytics
    Databases
    Documentation
    Graphical user interfaces
    Image processing
    Machine learning
    Mobile apps
    Multimedia
    Computer networking
    Scientific computing
    System administration
    Test frameworks
    Text processing
    Web frameworks
    Web scraping

Development environments
See also: Comparison of integrated development environments § Python

Most Python implementations (including CPython) include a read–eval–print loop (REPL); this permits the environment to function as a command line interpreter, with which users enter statements sequentially and receive results immediately.

Python is also bundled with an integrated development environment (IDE) called IDLE, which is oriented toward beginners.

Other shells, including IDLE and IPython, add additional capabilities such as improved auto-completion, session-state retention, and syntax highlighting.

Standard desktop IDEs include PyCharm, IntelliJ Idea, Visual Studio Code; there are also web browser-based IDEs, such as the following environments:

    SageMath, for developing science- and math-related programs;
    Jupyter Notebooks, an open-source interactive computing platform;
    PythonAnywhere, a browser-based IDE and hosting environment; and
    Canopy IDE, a commercial IDE that emphasizes scientific computing.[139][140]

Implementations
See also: List of Python software § Python implementations
Reference implementation

CPython is the reference implementation of Python. This implementation is written in C, meeting the C11 standard[141] (since version 3.11, older versions use the C89 standard with several select C99 features), but third-party extensions are not limited to older C versions—e.g., they can be implemented using C11 or C++.[142][143] CPython compiles Python programs into an intermediate bytecode,[144] which is then executed by a virtual machine.[145] CPython is distributed with a large standard library written in a combination of C and native Python.

CPython is available for many platforms, including Windows and most modern Unix-like systems, including macOS (and Apple M1 Macs, since Python 3.9.1, using an experimental installer). Starting with Python 3.9, the Python installer intentionally fails to install on Windows 7 and 8;[146][147] Windows XP was supported until Python 3.5, with unofficial support for VMS.[148] Platform portability was one of Python's earliest priorities.[149] During development of Python 1 and 2, even OS/2 and Solaris were supported;[150] since that time, support has been dropped for many platforms.

All current Python versions (since 3.7) support only operating systems that feature multithreading, by now supporting not nearly as many operating systems (dropping many outdated) than in the past.
Other implementations

All alternative implementations have at least slightly different semantic. For example, an alternative may include unordered dictionaries, in contrast to other current Python versions. As another example in the larger Python ecosystem, PyPy does not support the full C Python API. Alternative implementations include the following:

    PyPy is a fast, compliant interpreter of Python 2.7 and 3.10.[151][152] PyPy's just-in-time compiler often improves speed significantly relative to CPython, but PyPy does not support some libraries written in C.[153] PyPy offers support for the RISC-V instruction-set architecture.
    Codon is an implentation with an ahead-of-time (AOT) compiler, which compiles a statically-typed Python-like language whose "syntax and semantics are nearly identical to Python's, there are some notable differences"[154] For example, Codon uses 64-bit machine integers for speed, not arbitrarily as with Python; Codon developers claim that speedups over CPython are usually on the order of ten to a hundred times. Codon compiles to machine code (via LLVM) and supports native multithreading.[155] Codon can also compile to Python extension modules that can be imported and used from Python.
    MicroPython and CircuitPython are Python 3 variants that are optimized for microcontrollers, including the Lego Mindstorms EV3.[156]
    Pyston is a variant of the Python runtime that uses just-in-time compilation to speed up execution of Python programs.[157]
    Cinder is a performance-oriented fork of CPython 3.8 that features a number of optimizations, including bytecode inline caching, eager evaluation of coroutines, a method-at-a-time JIT, and an experimental bytecode compiler.[158]
    The Snek[159][160][161] embedded computing language "is Python-inspired, but it is not Python. It is possible to write Snek programs that run under a full Python system, but most Python programs will not run under Snek."[162] Snek is compatible with 8-bit AVR microcontrollers such as ATmega 328P-based Arduino, as well as larger microcontrollers that are compatible with MicroPython. Snek is an imperative language that (unlike Python) omits object-oriented programming. Snek supports only one numeric data type, which features 32-bit single precision (resembling JavaScript numbers, though smaller).

Unsupported implementations

Stackless Python is a significant fork of CPython that implements microthreads. This implementation uses the call stack differently, thus allowing massively concurrent programs. PyPy also offers a stackless version.[163]

Just-in-time Python compilers have been developed, but are now unsupported:

    Google began a project named Unladen Swallow in 2009: this project aimed to speed up the Python interpreter five-fold by using LLVM, and improve multithreading capability for scaling to thousands of cores,[164] while typical implementations are limited by the global interpreter lock.
    Psyco is a discontinued just-in-time specializing compiler, which integrates with CPython and transforms bytecode to machine code at runtime. The emitted code is specialized for certain data types and is faster than standard Python code. Psyco does not support Python 2.7 or later.
    PyS60 was a Python 2 interpreter for Series 60 mobile phones, which was released by Nokia in 2005. The interpreter implemented many modules from Python's standard library, as well as additional modules for integration with the Symbian operating system. The Nokia N900 also supports Python through the GTK widget library, allowing programs to be written and run on the target device.[165]

Cross-compilers to other languages

There are several compilers/transpilers to high-level object languages; the source language is unrestricted Python, a subset of Python, or a language similar to Python:

    Brython,[166] Transcrypt,[167][168] and Pyjs compile Python to JavaScript. (The latest release of Pyjs was in 2012.)
    Cython compiles a superset of Python to C. The resulting code can be used with Python via direct C-level API calls into the Python interpreter.
    PyJL compiles/transpiles a subset of Python to "human-readable, maintainable, and high-performance Julia source code".[92] Despite the developers' performance claims, this is not possible for arbitrary Python code; that is, compiling to a faster language or machine code is known to be impossible in the general case. The semantics of Python might potentially be changed, but in many cases speedup is possible with few or no changes in the Python code. The faster Julia source code can then be used from Python or compiled to machine code.
    Nuitka compiles Python into C.[169] This compiler works with Python 3.4 to 3.12 (and 2.6 and 2.7) for Python's main supported platforms (and Windows 7 or even Windows XP) and for Android. The compiler developers claim full support for Python 3.10, partial support for Python 3.11 and 3.12, and experimental support for Python 3.13. Nuitka supports macOS including Apple Silicon-based versions. The compiler is free of cost, though it has commercial add-ons (e.g., for hiding source code).
    Numba is a JIT compiler that is used from Python; the compiler translates a subset of Python and NumPy code into fast machine code. This tool is enabled by adding a decorator to the relevant Python code.
    Pythran compiles a subset of Python 3 to C++ (C++11).[170]
    RPython can be compiled to C, and it is used to build the PyPy interpreter for Python.
    The Python → 11l → C++ transpiler[171] compiles a subset of Python 3 to C++ (C++17).

There are also specialized compilers:

    MyHDL is a Python-based hardware description language (HDL) that converts MyHDL code to Verilog or VHDL code.

Some older projects existed, as well as compilers not designed for use with Python 3.x and related syntax:

    Google's Grumpy transpiles Python 2 to Go.[172][173][174] The latest release was in 2017.
    IronPython allows running Python 2.7 programs with the .NET Common Language Runtime.[175] An alpha version (released in 2021), is available for "Python 3.4, although features and behaviors from later versions may be included."[176]
    Jython compiles Python 2.7 to Java bytecode, allowing the use of Java libraries from a Python program.[177]
    Pyrex (last released in 2010) and Shed Skin (last released in 2013) compile to C and C++ respectively.

Performance

A performance comparison among various Python implementations, using a non-numerical (combinatorial) workload, was presented at EuroSciPy '13.[178] In addition, Python's performance relative to other programming languages is benchmarked by The Computer Language Benchmarks Game.[179]

There are several approaches to optimizing Python performance, given the inherent slowness of an interpreted language. These approaches include the following strategies or tools:

    Just-in-time compilation: Dynamically compiling Python code just before it is executed. This technique is used in libraries such as Numba and PyPy.
    Static compilation: Python code is compiled into machine code sometime before execution. An example of this approach is Cython, which compiles Python into C.
    Concurrency and parallelism: Multiple tasks can be run simultaneously. Python contains modules such as `multiprocessing` to support this form of parallelism. Moreover, this approach helps to overcome limitations of the Global Interpreter Lock (GIL) in CPU tasks.
    Efficient data structures: Performance can also be improved by using data types such as Set for membership tests, or deque from collections for queue operations.

Language Development

Python's development is conducted largely through the Python Enhancement Proposal (PEP) process; this process is the primary mechanism for proposing major new features, collecting community input on issues, and documenting Python design decisions.[180] Python coding style is covered in PEP 8.[181] Outstanding PEPs are reviewed and commented on by the Python community and the steering council.[180]

Enhancement of the language corresponds with development of the CPython reference implementation. The mailing list python-dev is the primary forum for the language's development. Specific issues were originally discussed in the Roundup bug tracker hosted by the foundation.[182] In 2022, all issues and discussions were migrated to GitHub.[183] Development originally took place on a self-hosted source-code repository running Mercurial, until Python moved to GitHub in January 2017.[184]

CPython's public releases have three types, distinguished by which part of the version number is incremented:

    Backward-incompatible versions, where code is expected to break and must be manually ported. The first part of the version number is incremented. These releases happen infrequently—version 3.0 was released 8 years after 2.0. According to Guido van Rossum, a version 4.0 will probably never exist.[185]
    Major or "feature" releases are largely compatible with the previous version but introduce new features. The second part of the version number is incremented. Starting with Python 3.9, these releases are expected to occur annually.[186][187] Each major version is supported by bug fixes for several years after its release.[188]
    Bug fix releases,[189] which introduce no new features, occur approximately every three months; these releases are made when a sufficient number of bugs have been fixed upstream since the last release. Security vulnerabilities are also patched in these releases. The third and final part of the version number is incremented.[189]

Many alpha, beta, and release-candidates are also released as previews and for testing before final releases. Although there is a rough schedule for releases, they are often delayed if the code is not ready yet. Python's development team monitors the state of the code by running a large unit test suite during development.[190]

The major academic conference on Python is PyCon. There are also special Python mentoring programs, such as PyLadies.
API documentation generators

Tools that can generate documentation for Python API include pydoc (available as part of the standard library); Sphinx; and Pdoc and its forks, Doxygen and Graphviz.[191]
Naming

Python's name is inspired by the British comedy group Monty Python, whom Python creator Guido van Rossum enjoyed while developing the language. Monty Python references appear frequently in Python code and culture;[192] for example, the metasyntactic variables often used in Python literature are spam and eggs, rather than the traditional foo and bar.[192][193] The official Python documentation also contains various references to Monty Python routines.[194][195] Python users are sometimes referred to as "Pythonistas".[196]

The affix Py is often used when naming Python applications or libraries. Some examples include the following:

    Pygame, a binding of Simple DirectMedia Layer to Python (commonly used to create games);
    PyQt and PyGTK, which bind Qt and GTK to Python respectively;
    PyPy, a Python implementation originally written in Python;
    NumPy, a Python library for numerical processing.

Popularity

Since 2003, Python has consistently ranked in the top ten of the most popular programming languages in the TIOBE Programming Community Index; as of December 2022, Python was the most popular language.[39] Python was selected as Programming Language of the Year (for "the highest rise in ratings in a year") in 2007, 2010, 2018, and 2020—the only language to have done so four times as of 2020[197]). In the TIOBE Index, monthly rankings are based on the volume of searches for programming languages on Google, Amazon, Wikipedia, Bing, and 20 other platforms. According to the accompanying graph, Python has shown a marked upward trend since the early 2000s, eventually passing more established languages such as C, C++, and Java. This trend can be attributed to Python's readable syntax, comprehensive standard library, and application in data science and machine learning fields.[198]
TIOBE Index Chart showing Python's popularity compared to other programming languages

Large organizations that use Python include Wikipedia, Google,[199] Yahoo!,[200] CERN,[201] NASA,[202] Facebook,[203] Amazon, Instagram,[204] Spotify,[205] and some smaller entities such as Industrial Light & Magic[206] and ITA.[207] The social news networking site Reddit was developed mostly in Python.[208] Organizations that partly use Python include Discord[209] and Baidu.[210]
Types of Use
Main article: List of Python software
Software that is powered by Python

Python has many uses, including the following:

    Scripting for web applications
    Scientific computing
    Artificial intelligence and machine learning projects
    Graphical user interfaces and desktop environments
    Embedded scripting in software and hardware products
    Operating systems
    Information security

Python can serve as a scripting language for web applications, e.g., via the mod_wsgi module for the Apache web server.[211] With Web Server Gateway Interface, a standard API has evolved to facilitate these applications. Web frameworks such as Django, Pylons, Pyramid, TurboGears, web2py, Tornado, Flask, Bottle, and Zope support developers in the design and maintenance of complex applications. Pyjs and IronPython can be used to develop the client-side of Ajax-based applications. SQLAlchemy can be used as a data mapper to a relational database. Twisted is a framework to program communication between computers; this framework is used by Dropbox, for example.

Libraries such as NumPy, SciPy and Matplotlib allow the effective use of Python in scientific computing,[212][213] with specialized libraries such as Biopython and Astropy providing domain-specific functionality. SageMath is a computer algebra system with a notebook interface that is programmable in Python; the SageMath library covers many aspects of mathematics, including algebra, combinatorics, numerical mathematics, number theory, and calculus.[214] OpenCV has Python bindings with a rich set of features for computer vision and image processing.[215]

Python is commonly used in artificial-intelligence and machine-learning projects, with support from libraries such as TensorFlow, Keras, Pytorch, scikit-learn and ProbLog (a logic language).[216][217][218][219][220] As a scripting language with a modular architecture, simple syntax, and rich text processing tools, Python is often used for natural language processing.[221]

The combination of Python and Prolog has proven useful for AI applications, with Prolog providing knowledge representation and reasoning capabilities. The Janus system, in particular, exploits similarities between these two languages, in part because of their dynamic typing and their simple, recursive data structures. This combination is typically applied natural language processing, visual query answering, geospatial reasoning, and handling semantic web data.[222][223] The Natlog system, implemented in Python, uses Definite Clause Grammars (DCGs) to create prompts for two types of generators: text-to-text generators such as GPT3, and text-to-image generators such as DALL-E or Stable Diffusion.[224]

Python can be used for graphical user interfaces (GUIs), by using libraries such as Tkinter.[225] Similarly, for the One Laptop per Child XO computer, most of the Sugar desktop environment is written in Python (as of 2008).[226]

Python is embedded in many software products (and some hardware products) as a scripting language. These products include the following:

    finite element method software such as Abaqus,
    3D parametric modelers such as FreeCAD,
    3D animation packages such as 3ds Max, Blender, Cinema 4D, Lightwave, Houdini, Maya, modo, MotionBuilder, Softimage,
    the visual effects compositor Nuke,
    2D imaging programs such as GIMP,[227] Inkscape, Scribus and Paint Shop Pro,[228] and
    musical notation programs such as scorewriter and capella.

Similarly, GNU Debugger uses Python as a pretty printer to show complex structures such as C++ containers. Esri promotes Python as the best choice for writing scripts in ArcGIS.[229] Python has also been used in several video games,[230][231] and it has been adopted as first of the three programming languages available in Google App Engine (the other two being Java and Go).[232] LibreOffice includes Python, and its developers plan to replace Java with Python; LibreOffice's Python Scripting Provider is a core feature[233] since version 4.0 (from 7 February 2013).

Among hardware products, the Raspberry Pi single-board computer project has adopted Python as its main user-programming language.

Many operating systems include Python as a standard component. Python ships with most Linux distributions,[234] AmigaOS 4 (using Python 2.7), FreeBSD (as a package), NetBSD, and OpenBSD (as a package); it can be used from the command line (terminal). Many Linux distributions use installers written in Python: Ubuntu uses the Ubiquity installer, while Red Hat Linux and Fedora Linux use the Anaconda installer. Gentoo Linux uses Python in its package management system, Portage.[235]

Python is used extensively in the information security industry, including in exploit development.[236][237]
Languages influenced by Python

Python's design and philosophy have influenced many other programming languages:

    Boo uses indentation, a similar syntax, and a similar object model.[238]
    Cobra uses indentation and a similar syntax; its Acknowledgements document lists Python first among influencing languages.[239]
    CoffeeScript, a programming language that cross-compiles to JavaScript, has a Python-inspired syntax.
    ECMAScript–JavaScript borrowed iterators and generators from Python.[240]
    GDScript, a Python-like scripting language that is built in to the Godot game engine.[241]
    Go is designed for "speed of working in a dynamic language like Python";[242] Go shares Python's syntax for slicing arrays.
    Groovy was motivated by a desire to incorporate the Python design philosophy into Java.[243]
    Julia was designed to be "as usable for general programming as Python".[28]
    Mojo is a non-strict[29][244] superset of Python (e.g., omitting classes, and adding struct).[245]
    Nim uses indentation and a similar syntax.[246]
    Ruby's creator, Yukihiro Matsumoto, said that "I wanted a scripting language that was more powerful than Perl, and more object-oriented than Python. That's why I decided to design my own language."[247]
    Swift, a programming language developed by Apple, has some Python-inspired syntax.[248]
    Kotlin blends Python and Java features, which minimizes boilerplate code and enhances developer efficiency.[249]

Python's development practices have also been emulated by other languages. For example, Python requires a document that describes the rationale and context for any language change; this document is known as a Python Enhancement Proposal or PEP. This practice is also used by the developers of Tcl,[250] Erlang,[251] and Swift.[252]
See also

    iconComputer programming portalFree and open-source software portal

    Python syntax and semantics
    pip (package manager)
    List of programming languages
    History of programming languages
    Comparison of programming languages

Notes

since 3.5, but those hints are ignored, except with unofficial tools[5]

    Tier 1: 64-bit Linux, macOS; 64- and 32-bit Windows 10+[6]
    Tier 2: E.g. 32-bit WebAssembly (WASI)
    Tier 3: 64-bit Android,[7] iOS, FreeBSD, and (32-bit) Raspberry Pi OS
    Unofficial (or has been known to work): Other Unix-like/BSD variants) and a few other platforms[8][9][10]

    del in Python does not behave the same way delete in languages such as C++ does, where such a word is used to call the destructor and deallocate heap memory.

References

"General Python FAQ – Python 3 documentation". docs.python.org. Retrieved 7 July 2024.
"Python 0.9.1 part 01/21". alt.sources archives. Archived from the original on 11 August 2021. Retrieved 11 August 2021.
Thomas Wouters (11 June 2025). "Python 3.13.5 is now available!". Retrieved 11 June 2025.
"Why is Python a dynamic language and also a strongly typed language". Python Wiki. Archived from the original on 14 March 2021. Retrieved 27 January 2021.
"PEP 483 – The Theory of Type Hints". Python.org. Archived from the original on 14 June 2020. Retrieved 14 June 2018.
"PEP 11 – CPython platform support | peps.python.org". Python Enhancement Proposals (PEPs). Retrieved 22 April 2024.
"PEP 738 – Adding Android as a supported platform | peps.python.org". Python Enhancement Proposals (PEPs). Retrieved 19 May 2024.
"Download Python for Other Platforms". Python.org. Archived from the original on 27 November 2020. Retrieved 18 August 2023.
"test – Regression tests package for Python – Python 3.7.13 documentation". docs.python.org. Archived from the original on 17 May 2022. Retrieved 17 May 2022.
"platform – Access to underlying platform's identifying data – Python 3.10.4 documentation". docs.python.org. Archived from the original on 17 May 2022. Retrieved 17 May 2022.
Holth, Moore (30 March 2014). "PEP 0441 – Improving Python ZIP Application Support". Archived from the original on 26 December 2018. Retrieved 12 November 2015.
"Starlark Language". Archived from the original on 15 June 2020. Retrieved 25 May 2019.
"Why was Python created in the first place?". General Python FAQ. Python Software Foundation. Archived from the original on 24 October 2012. Retrieved 22 March 2007. "I had extensive experience with implementing an interpreted language in the ABC group at CWI, and from working with this group I had learned a lot about language design. This is the origin of many Python features, including the use of indentation for statement grouping and the inclusion of very high-level data types (although the details are all different in Python)."
"Ada 83 Reference Manual (raise statement)". Archived from the original on 22 October 2019. Retrieved 7 January 2020.
Kuchling, Andrew M. (22 December 2006). "Interview with Guido van Rossum (July 1998)". amk.ca. Archived from the original on 1 May 2007. Retrieved 12 March 2012. "I'd spent a summer at DEC's Systems Research Center, which introduced me to Modula-2+; the Modula-3 final report was being written there at about the same time. What I learned there later showed up in Python's exception handling, modules, and the fact that methods explicitly contain 'self' in their parameter list. String slicing came from Algol-68 and Icon."
"itertools – Functions creating iterators for efficient looping – Python 3.7.1 documentation". docs.python.org. Archived from the original on 14 June 2020. Retrieved 22 November 2016. "This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML."
van Rossum, Guido (1993). "An Introduction to Python for UNIX/C Programmers". Proceedings of the NLUUG Najaarsconferentie (Dutch UNIX Users Group). CiteSeerX 10.1.1.38.2023. "even though the design of C is far from ideal, its influence on Python is considerable."
"Classes". The Python Tutorial. Python Software Foundation. Archived from the original on 23 October 2012. Retrieved 20 February 2012. "It is a mixture of the class mechanisms found in C++ and Modula-3"
Lundh, Fredrik. "Call By Object". effbot.org. Archived from the original on 23 November 2019. Retrieved 21 November 2017. "replace "CLU" with "Python", "record" with "instance", and "procedure" with "function or method", and you get a pretty accurate description of Python's object model."
Simionato, Michele. "The Python 2.3 Method Resolution Order". Python Software Foundation. Archived from the original on 20 August 2020. Retrieved 29 July 2014. "The C3 method itself has nothing to do with Python, since it was invented by people working on Dylan and it is described in a paper intended for lispers"
Kuchling, A. M. "Functional Programming HOWTO". Python v2.7.2 documentation. Python Software Foundation. Archived from the original on 24 October 2012. Retrieved 9 February 2012. "List comprehensions and generator expressions [...] are a concise notation for such operations, borrowed from the functional programming language Haskell."
Schemenauer, Neil; Peters, Tim; Hetland, Magnus Lie (18 May 2001). "PEP 255 – Simple Generators". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 5 June 2020. Retrieved 9 February 2012.
"More Control Flow Tools". Python 3 documentation. Python Software Foundation. Archived from the original on 4 June 2016. Retrieved 24 July 2015. "By popular demand, a few features commonly found in functional programming languages like Lisp have been added to Python. With the lambda keyword, small anonymous functions can be created."
"re – Regular expression operations – Python 3.10.6 documentation". docs.python.org. Archived from the original on 18 July 2018. Retrieved 6 September 2022. "This module provides regular expression matching operations similar to those found in Perl."
"CoffeeScript". coffeescript.org. Archived from the original on 12 June 2020. Retrieved 3 July 2018.
"Perl and Python influences in JavaScript". www.2ality.com. 24 February 2013. Archived from the original on 26 December 2018. Retrieved 15 May 2015.
Rauschmayer, Axel. "Chapter 3: The Nature of JavaScript; Influences". O'Reilly, Speaking JavaScript. Archived from the original on 26 December 2018. Retrieved 15 May 2015.
"Why We Created Julia". Julia website. February 2012. Archived from the original on 2 May 2020. Retrieved 5 June 2014. "We want something as usable for general programming as Python [...]"
Krill, Paul (4 May 2023). "Mojo language marries Python and MLIR for AI development". InfoWorld. Archived from the original on 5 May 2023. Retrieved 5 May 2023.
Ring Team (4 December 2017). "Ring and other languages". ring-lang.net. ring-lang. Archived from the original on 25 December 2018. Retrieved 4 December 2017.
Bini, Ola (2007). Practical JRuby on Rails Web 2.0 Projects: bringing Ruby on Rails to the Java platform. Berkeley: APress. p. 3. ISBN 978-1-59059-881-8.
Lattner, Chris (3 June 2014). "Chris Lattner's Homepage". Chris Lattner. Archived from the original on 25 December 2018. Retrieved 3 June 2014. "The Swift language is the product of tireless effort from a team of language experts, documentation gurus, compiler optimization ninjas, and an incredibly important internal dogfooding group who provided feedback to help refine and battle-test ideas. Of course, it also greatly benefited from the experiences hard-won by many other languages in the field, drawing ideas from Objective-C, Rust, Haskell, Ruby, Python, C#, CLU, and far too many others to list."
"V documentation (Introduction)". GitHub. Retrieved 24 December 2024.
Kuhlman, Dave. "A Python Book: Beginning Python, Advanced Python, and Python Exercises". Section 1.1. Archived from the original (PDF) on 23 June 2012.
Rossum, Guido Van (20 January 2009). "The History of Python: A Brief Timeline of Python". The History of Python. Archived from the original on 5 June 2020. Retrieved 5 March 2021.
Peterson, Benjamin (20 April 2020). "Python 2.7.18, the last release of Python 2". Python Insider. Archived from the original on 26 April 2020. Retrieved 27 April 2020.
"Stack Overflow Developer Survey 2022". Stack Overflow. Archived from the original on 27 June 2022. Retrieved 12 August 2022.
"The State of Developer Ecosystem in 2020 Infographic". JetBrains: Developer Tools for Professionals and Teams. Archived from the original on 1 March 2021. Retrieved 5 March 2021.
"TIOBE Index". TIOBE. Archived from the original on 25 February 2018. Retrieved 3 January 2023. "The TIOBE Programming Community index is an indicator of the popularity of programming languages" Updated as required.
Healy, John; McInnes, Leland; Weir, Colin (2017). "Bridging the Cyber-Analysis Gap: The Democratization of Data Science". The Cyber Defense Review. 2 (1): 109–118. doi:10.2307/26267404. ISSN 2474-2120. "Python is the lingua franca of data science and machine learning."
Sultana, Simon G.; Reed, Philip A. (2017). "Curriculum for an Introductory Computer Science Course: Identifying Recommendations from Academia and Industry". The Journal of Technology Studies. 43 (2): 80–92. doi:10.2307/90023144. ISSN 1071-6084.
Venners, Bill (13 January 2003). "The Making of Python". Artima Developer. Artima. Archived from the original on 1 September 2016. Retrieved 22 March 2007.
van Rossum, Guido (29 August 2000). "SETL (was: Lukewarm about range literals)". Python-Dev (Mailing list). Archived from the original on 14 July 2018. Retrieved 13 March 2011.
van Rossum, Guido (20 January 2009). "A Brief Timeline of Python". The History of Python. Archived from the original on 5 June 2020. Retrieved 20 January 2009.
Fairchild, Carlie (12 July 2018). "Guido van Rossum Stepping Down from Role as Python's Benevolent Dictator For Life". Linux Journal. Archived from the original on 13 July 2018. Retrieved 13 July 2018.
"PEP 8100". Python Software Foundation. Archived from the original on 4 June 2020. Retrieved 4 May 2019.
"PEP 13 – Python Language Governance". Python.org. Archived from the original on 27 May 2021. Retrieved 25 August 2021.
Briggs, Jason R.; Lipovača, Miran (2013). Python for kids: a playful introduction to programming. San Francisco, Calif: No Starch Press. ISBN 978-1-59327-407-8.
Kuchling, A. M.; Zadka, Moshe (16 October 2000). "What's New in Python 2.0". Python Software Foundation. Archived from the original on 23 October 2012. Retrieved 11 February 2012.
"PEP 373 – Python 2.7 Release Schedule". python.org. Archived from the original on 19 May 2020. Retrieved 9 January 2017.
"PEP 466 – Network Security Enhancements for Python 2.7.x". python.org. Archived from the original on 4 June 2020. Retrieved 9 January 2017.
"Sunsetting Python 2". Python.org. Archived from the original on 12 January 2020. Retrieved 22 September 2019.
"PEP 373 – Python 2.7 Release Schedule". Python.org. Archived from the original on 13 January 2020. Retrieved 22 September 2019.
mattip (25 December 2023). "PyPy v7.3.14 release". PyPy. Archived from the original on 5 January 2024. Retrieved 5 January 2024.
Langa, Łukasz (17 May 2022). "Python 3.9.13 is now available". Python Insider. Archived from the original on 17 May 2022. Retrieved 21 May 2022.
"Status of Python versions". Python Developer's Guide. Retrieved 7 October 2024.
"Python". endoflife.date. 8 October 2024. Retrieved 20 November 2024.
"CVE-2021-3177". Red Hat Customer Portal. Archived from the original on 6 March 2021. Retrieved 26 February 2021.
"CVE-2021-3177". CVE. Archived from the original on 27 February 2021. Retrieved 26 February 2021.
"CVE-2021-23336". CVE. Archived from the original on 24 February 2021. Retrieved 26 February 2021.
"Built-in Types".
"PEP 634 – Structural Pattern Matching: Specification". Python.org. Archived from the original on 6 May 2021. Retrieved 14 February 2021.
corbet (24 October 2022). "Python 3.11 released [LWN.net]". lwn.net. Retrieved 15 November 2022.
"What's New In Python 3.13". Python documentation. Retrieved 30 April 2024.
"PEP 711: PyBI: a standard format for distributing Python Binaries". Discussions on Python.org. 7 April 2023. Retrieved 20 November 2024.
"PEP 686 – Make UTF-8 mode default | peps.python.org". Python Enhancement Proposals (PEPs). Retrieved 20 November 2024.
"1. Extending Python with C or C++ – Python 3.9.1 documentation". docs.python.org. Archived from the original on 23 June 2020. Retrieved 14 February 2021.
"PEP 623 – Remove wstr from Unicode". Python.org. Archived from the original on 5 March 2021. Retrieved 14 February 2021.
"PEP 667 – Consistent views of namespaces | peps.python.org". Python Enhancement Proposals (PEPs). Retrieved 7 October 2024.
"PEP 703 – Making the GIL Optional in CPython". Python Enhancement Proposals (PEPs). Retrieved 30 March 2025.
"PEP 749 – Implementing PEP 649 | peps.python.org". Python Enhancement Proposals (PEPs). Retrieved 20 November 2024.
"PEP 761 – Deprecating PGP signatures for CPython artifacts | peps.python.org". Python Enhancement Proposals (PEPs). Retrieved 6 January 2025.
Wouters, Thomas (9 April 2024). "Python Insider: Python 3.12.3 and 3.13.0a6 released". Python Insider. Retrieved 29 April 2024.
"PEP 594 – Removing dead batteries from the standard library". Python Enhancement Proposals. Python Software Foundation. 20 May 2019.
The Cain Gang Ltd. "Python Metaclasses: Who? Why? When?" (PDF). Archived from the original (PDF) on 30 May 2009. Retrieved 27 June 2009.
"3.3. Special method names". The Python Language Reference. Python Software Foundation. Archived from the original on 15 December 2018. Retrieved 27 June 2009.
"PyDBC: method preconditions, method postconditions and class invariants for Python". Archived from the original on 23 November 2019. Retrieved 24 September 2011.
"Contracts for Python". Archived from the original on 15 June 2020. Retrieved 24 September 2011.
"PyDatalog". Archived from the original on 13 June 2020. Retrieved 22 July 2012.
"Glue It All Together With Python". Python.org. Retrieved 30 September 2024.
"Extending and Embedding the Python Interpreter: Reference Counts". Docs.python.org. Archived from the original on 18 October 2012. Retrieved 5 June 2020. "Since Python makes heavy use of malloc() and free(), it needs a strategy to avoid memory leaks as well as the use of freed memory. The chosen method is called reference counting."
Hettinger, Raymond (30 January 2002). "PEP 289 – Generator Expressions". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 14 June 2020. Retrieved 19 February 2012.
"6.5 itertools – Functions creating iterators for efficient looping". Docs.python.org. Archived from the original on 14 June 2020. Retrieved 22 November 2016.
Peters, Tim (19 August 2004). "PEP 20 – The Zen of Python". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 26 December 2018. Retrieved 24 November 2008.
Lutz, Mark (January 2022). "Python Changes 2014+". Learning Python. Archived from the original on 15 March 2024. Retrieved 25 February 2024.
"Confusion regarding a rule in The Zen of Python". Python Help - Discussions on Python.org. 3 May 2022. Archived from the original on 25 February 2024. Retrieved 25 February 2024.
Ambi, Chetan (4 July 2021). "The Most Controversial Python Walrus Operator". Python Simplified. Archived from the original on 27 August 2023. Retrieved 5 February 2024.
Grifski, Jeremy (24 May 2020). "The Controversy Behind The Walrus Operator in Python". The Renegade Coder. Archived from the original on 28 December 2023. Retrieved 25 February 2024.
Bader, Dan. "Python String Formatting Best Practices". Real Python. Archived from the original on 18 February 2024. Retrieved 25 February 2024.
Martelli, Alex; Ravenscroft, Anna; Ascher, David (2005). Python Cookbook, 2nd Edition. O'Reilly Media. p. 230. ISBN 978-0-596-00797-3. Archived from the original on 23 February 2020. Retrieved 14 November 2015.
"Python Culture". ebeab. 21 January 2014. Archived from the original on 30 January 2014.
"Transpiling Python to Julia using PyJL" (PDF). Archived (PDF) from the original on 19 November 2023. Retrieved 20 September 2023. "After manually modifying one line of code by specifying the necessary type information, we obtained a speedup of 52.6×, making the translated Julia code 19.5× faster than the original Python code."
"Why is it called Python?". General Python FAQ. Docs.python.org. Archived from the original on 24 October 2012. Retrieved 3 January 2023.
"15 Ways Python Is a Powerful Force on the Web". Archived from the original on 11 May 2019. Retrieved 3 July 2018.
"pprint – Data pretty printer – Python 3.11.0 documentation". docs.python.org. Archived from the original on 22 January 2021. Retrieved 5 November 2022. "stuff=['spam', 'eggs', 'lumberjack', 'knights', 'ni']"
"Code Style – The Hitchhiker's Guide to Python". docs.python-guide.org. Archived from the original on 27 January 2021. Retrieved 20 January 2021.
"Is Python a good language for beginning programmers?". General Python FAQ. Python Software Foundation. Archived from the original on 24 October 2012. Retrieved 21 March 2007.
"Myths about indentation in Python". Secnetix.de. Archived from the original on 18 February 2018. Retrieved 19 April 2011.
Guttag, John V. (12 August 2016). Introduction to Computation and Programming Using Python: With Application to Understanding Data. MIT Press. ISBN 978-0-262-52962-4.
"PEP 8 – Style Guide for Python Code". Python.org. Archived from the original on 17 April 2019. Retrieved 26 March 2019.
"8. Errors and Exceptions – Python 3.12.0a0 documentation". docs.python.org. Archived from the original on 9 May 2022. Retrieved 9 May 2022.
"Highlights: Python 2.5". Python.org. Archived from the original on 4 August 2019. Retrieved 20 March 2018.
van Rossum, Guido (22 April 2009). "Tail Recursion Elimination". Neopythonic.blogspot.be. Archived from the original on 19 May 2018. Retrieved 3 December 2012.
van Rossum, Guido (9 February 2006). "Language Design Is Not Just Solving Puzzles". Artima forums. Artima. Archived from the original on 17 January 2020. Retrieved 21 March 2007.
van Rossum, Guido; Eby, Phillip J. (10 May 2005). "PEP 342 – Coroutines via Enhanced Generators". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 29 May 2020. Retrieved 19 February 2012.
"PEP 380". Python.org. Archived from the original on 4 June 2020. Retrieved 3 December 2012.
"division". python.org. Archived from the original on 20 July 2006. Retrieved 30 July 2014.
"PEP 0465 – A dedicated infix operator for matrix multiplication". python.org. Archived from the original on 4 June 2020. Retrieved 1 January 2016.
"Python 3.5.1 Release and Changelog". python.org. Archived from the original on 14 May 2020. Retrieved 1 January 2016.
"What's New in Python 3.8". Archived from the original on 8 June 2020. Retrieved 14 October 2019.
van Rossum, Guido; Hettinger, Raymond (7 February 2003). "PEP 308 – Conditional Expressions". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 13 March 2016. Retrieved 13 July 2011.
"4. Built-in Types – Python 3.6.3rc1 documentation". python.org. Archived from the original on 14 June 2020. Retrieved 1 October 2017.
"5.3. Tuples and Sequences – Python 3.7.1rc2 documentation". python.org. Archived from the original on 10 June 2020. Retrieved 17 October 2018.
"PEP 498 – Literal String Interpolation". python.org. Archived from the original on 15 June 2020. Retrieved 8 March 2017.
"Why must 'self' be used explicitly in method definitions and calls?". Design and History FAQ. Python Software Foundation. Archived from the original on 24 October 2012. Retrieved 19 February 2012.
Sweigart, Al (2020). Beyond the Basic Stuff with Python: Best Practices for Writing Clean Code. No Starch Press. p. 322. ISBN 978-1-59327-966-0. Archived from the original on 13 August 2021. Retrieved 7 July 2021.
"The Python Language Reference, section 3.3. New-style and classic classes, for release 2.7.1". Archived from the original on 26 October 2012. Retrieved 12 January 2011.
"PEP 484 – Type Hints | peps.python.org". peps.python.org. Archived from the original on 27 November 2023. Retrieved 29 November 2023.
"typing — Support for type hints". Python documentation. Python Software Foundation. Archived from the original on 21 February 2020. Retrieved 22 December 2023.
"mypy – Optional Static Typing for Python". Archived from the original on 6 June 2020. Retrieved 28 January 2017.
"Introduction". mypyc.readthedocs.io. Archived from the original on 22 December 2023. Retrieved 22 December 2023.
"15. Floating Point Arithmetic: Issues and Limitations – Python 3.8.3 documentation". docs.python.org. Archived from the original on 6 June 2020. Retrieved 6 June 2020. "Almost all machines today (November 2000) use IEEE-754 floating point arithmetic, and almost all platforms map Python floats to IEEE-754 "double precision"."
Zadka, Moshe; van Rossum, Guido (11 March 2001). "PEP 237 – Unifying Long Integers and Integers". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 28 May 2020. Retrieved 24 September 2011.
"Built-in Types". Archived from the original on 14 June 2020. Retrieved 3 October 2019.
"PEP 465 – A dedicated infix operator for matrix multiplication". python.org. Archived from the original on 29 May 2020. Retrieved 3 July 2018.
Zadka, Moshe; van Rossum, Guido (11 March 2001). "PEP 238 – Changing the Division Operator". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 28 May 2020. Retrieved 23 October 2013.
"Why Python's Integer Division Floors". 24 August 2010. Archived from the original on 5 June 2020. Retrieved 25 August 2010.
"round", The Python standard library, release 3.2, §2: Built-in functions, archived from the original on 25 October 2012, retrieved 14 August 2011
"round", The Python standard library, release 2.7, §2: Built-in functions, archived from the original on 27 October 2012, retrieved 14 August 2011
Beazley, David M. (2009). Python Essential Reference (4th ed.). Addison-Wesley Professional. p. 66. ISBN 9780672329784.
Kernighan, Brian W.; Ritchie, Dennis M. (1988). The C Programming Language (2nd ed.). p. 206.
Batista, Facundo (17 October 2003). "PEP 327 – Decimal Data Type". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 4 June 2020. Retrieved 24 November 2008.
"What's New in Python 2.6". Python v2.6.9 documentation. 29 October 2013. Archived from the original on 23 December 2019. Retrieved 26 September 2015.
"10 Reasons Python Rocks for Research (And a Few Reasons it Doesn't) – Hoyt Koepke". University of Washington Department of Statistics. Archived from the original on 31 May 2020. Retrieved 3 February 2019.
Shell, Scott (17 June 2014). "An introduction to Python for scientific computing" (PDF). Archived (PDF) from the original on 4 February 2019. Retrieved 3 February 2019.
Piotrowski, Przemyslaw (July 2006). "Build a Rapid Web Development Environment for Python Server Pages and Oracle". Oracle Technology Network. Oracle. Archived from the original on 2 April 2019. Retrieved 12 March 2012.
Eby, Phillip J. (7 December 2003). "PEP 333 – Python Web Server Gateway Interface v1.0". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 14 June 2020. Retrieved 19 February 2012.
"PyPI". PyPI. 13 March 2025. Archived from the original on 22 February 2025.
Enthought, Canopy. "Canopy". www.enthought.com. Archived from the original on 15 July 2017. Retrieved 20 August 2016.
"Project Jupyter". Jupyter.org. Archived from the original on 12 October 2023. Retrieved 2 April 2025.
"PEP 7 – Style Guide for C Code | peps.python.org". peps.python.org. Archived from the original on 24 April 2022. Retrieved 28 April 2022.
"4. Building C and C++ Extensions – Python 3.9.2 documentation". docs.python.org. Archived from the original on 3 March 2021. Retrieved 1 March 2021.
van Rossum, Guido (5 June 2001). "PEP 7 – Style Guide for C Code". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 1 June 2020. Retrieved 24 November 2008.
"CPython byte code". Docs.python.org. Archived from the original on 5 June 2020. Retrieved 16 February 2016.
"Python 2.5 internals" (PDF). Archived (PDF) from the original on 6 August 2012. Retrieved 19 April 2011.
"Changelog – Python 3.9.0 documentation". docs.python.org. Archived from the original on 7 February 2021. Retrieved 8 February 2021.
"Download Python". Python.org. Archived from the original on 8 December 2020. Retrieved 13 December 2020.
"history [vmspython]". www.vmspython.org. Archived from the original on 2 December 2020. Retrieved 4 December 2020.
"An Interview with Guido van Rossum". Oreilly.com. Archived from the original on 16 July 2014. Retrieved 24 November 2008.
"Download Python for Other Platforms". Python.org. Archived from the original on 27 November 2020. Retrieved 4 December 2020.
"PyPy compatibility". Pypy.org. Archived from the original on 6 June 2020. Retrieved 3 December 2012.
Team, The PyPy (28 December 2019). "Download and Install". PyPy. Archived from the original on 8 January 2022. Retrieved 8 January 2022.
"speed comparison between CPython and Pypy". Speed.pypy.org. Archived from the original on 10 May 2021. Retrieved 3 December 2012.
"Codon: Differences with Python". Archived from the original on 25 May 2023. Retrieved 28 August 2023.
Lawson, Loraine (14 March 2023). "MIT-Created Compiler Speeds up Python Code". The New Stack. Archived from the original on 6 April 2023. Retrieved 28 August 2023.
"Python-for-EV3". LEGO Education. Archived from the original on 7 June 2020. Retrieved 17 April 2019.
Yegulalp, Serdar (29 October 2020). "Pyston returns from the dead to speed Python". InfoWorld. Archived from the original on 27 January 2021. Retrieved 26 January 2021.
"cinder: Instagram's performance-oriented fork of CPython". GitHub. Archived from the original on 4 May 2021. Retrieved 4 May 2021.
Aroca, Rafael (7 August 2021). "Snek Lang: feels like Python on Arduinos". Yet Another Technology Blog. Archived from the original on 5 January 2024. Retrieved 4 January 2024.
Aufranc (CNXSoft), Jean-Luc (16 January 2020). "Snekboard Controls LEGO Power Functions with CircuitPython or Snek Programming Languages (Crowdfunding) – CNX Software". CNX Software – Embedded Systems News. Archived from the original on 5 January 2024. Retrieved 4 January 2024.
Kennedy (@mkennedy), Michael. "Ready to find out if you're git famous?". pythonbytes.fm. Archived from the original on 5 January 2024. Retrieved 4 January 2024.
Packard, Keith (20 December 2022). "The Snek Programming Language: A Python-inspired Embedded Computing Language" (PDF). Archived (PDF) from the original on 4 January 2024. Retrieved 4 January 2024.
"Application-level Stackless features – PyPy 2.0.2 documentation". Doc.pypy.org. Archived from the original on 4 June 2020. Retrieved 17 July 2013.
"Plans for optimizing Python". Google Project Hosting. 15 December 2009. Archived from the original on 11 April 2016. Retrieved 24 September 2011.
"Python on the Nokia N900". Stochastic Geometry. 29 April 2010. Archived from the original on 20 June 2019. Retrieved 9 July 2015.
"Brython". brython.info. Archived from the original on 3 August 2018. Retrieved 21 January 2021.
"Transcrypt – Python in the browser". transcrypt.org. Archived from the original on 19 August 2018. Retrieved 22 December 2020.
"Transcrypt: Anatomy of a Python to JavaScript Compiler". InfoQ. Archived from the original on 5 December 2020. Retrieved 20 January 2021.
"Nuitka Home | Nuitka Home". nuitka.net. Archived from the original on 30 May 2020. Retrieved 18 August 2017.
Guelton, Serge; Brunet, Pierrick; Amini, Mehdi; Merlini, Adrien; Corbillon, Xavier; Raynaud, Alan (16 March 2015). "Pythran: enabling static optimization of scientific Python programs". Computational Science & Discovery. 8 (1). IOP Publishing: 014001. Bibcode:2015CS&D....8a4001G. doi:10.1088/1749-4680/8/1/014001. ISSN 1749-4699.
"The Python → 11l → C++ transpiler". Archived from the original on 24 September 2022. Retrieved 17 July 2022.
"google/grumpy". 10 April 2020. Archived from the original on 15 April 2020. Retrieved 25 March 2020 – via GitHub.
"Projects". opensource.google. Archived from the original on 24 April 2020. Retrieved 25 March 2020.
Francisco, Thomas Claburn in San. "Google's Grumpy code makes Python Go". www.theregister.com. Archived from the original on 7 March 2021. Retrieved 20 January 2021.
"IronPython.net /". ironpython.net. Archived from the original on 17 April 2021.
"GitHub – IronLanguages/ironpython3: Implementation of Python 3.x for .NET Framework that is built on top of the Dynamic Language Runtime". GitHub. Archived from the original on 28 September 2021.
"Jython FAQ". www.jython.org. Archived from the original on 22 April 2021. Retrieved 22 April 2021.
Murri, Riccardo (2013). Performance of Python runtimes on a non-numeric scientific code. European Conference on Python in Science (EuroSciPy). arXiv:1404.6388. Bibcode:2014arXiv1404.6388M.
"The Computer Language Benchmarks Game". Archived from the original on 14 June 2020. Retrieved 30 April 2020.
Warsaw, Barry; Hylton, Jeremy; Goodger, David (13 June 2000). "PEP 1 – PEP Purpose and Guidelines". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 6 June 2020. Retrieved 19 April 2011.
"PEP 8 – Style Guide for Python Code". Python.org. Archived from the original on 17 April 2019. Retrieved 26 March 2019.
Cannon, Brett. "Guido, Some Guys, and a Mailing List: How Python is Developed". python.org. Python Software Foundation. Archived from the original on 1 June 2009. Retrieved 27 June 2009.
"Moving Python's bugs to GitHub [LWN.net]". Archived from the original on 2 October 2022. Retrieved 2 October 2022.
"Python Developer's Guide – Python Developer's Guide". devguide.python.org. Archived from the original on 9 November 2020. Retrieved 17 December 2019.
Hughes, Owen (24 May 2021). "Programming languages: Why Python 4.0 might never arrive, according to its creator". TechRepublic. Archived from the original on 14 July 2022. Retrieved 16 May 2022.
"PEP 602 – Annual Release Cycle for Python". Python.org. Archived from the original on 14 June 2020. Retrieved 6 November 2019.
"Changing the Python release cadence [LWN.net]". lwn.net. Archived from the original on 6 November 2019. Retrieved 6 November 2019.
Norwitz, Neal (8 April 2002). "[Python-Dev] Release Schedules (was Stability & change)". Archived from the original on 15 December 2018. Retrieved 27 June 2009.
Aahz; Baxter, Anthony (15 March 2001). "PEP 6 – Bug Fix Releases". Python Enhancement Proposals. Python Software Foundation. Archived from the original on 5 June 2020. Retrieved 27 June 2009.
"Python Buildbot". Python Developer's Guide. Python Software Foundation. Archived from the original on 5 June 2020. Retrieved 24 September 2011.
"Documentation Tools". Python.org. Archived from the original on 11 November 2020. Retrieved 22 March 2021.
"Whetting Your Appetite". The Python Tutorial. Python Software Foundation. Archived from the original on 26 October 2012. Retrieved 20 February 2012.
"In Python, should I use else after a return in an if block?". Stack Overflow. Stack Exchange. 17 February 2011. Archived from the original on 20 June 2019. Retrieved 6 May 2011.
Lutz, Mark (2009). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media, Inc. p. 17. ISBN 9781449379322. Archived from the original on 17 July 2017. Retrieved 9 May 2017.
Fehily, Chris (2002). Python. Peachpit Press. p. xv. ISBN 9780201748840. Archived from the original on 17 July 2017. Retrieved 9 May 2017.
Lubanovic, Bill (2014). Introducing Python. Sebastopol, CA : O'Reilly Media. p. 305. ISBN 978-1-4493-5936-2. Retrieved 31 July 2023.
Blake, Troy (18 January 2021). "TIOBE Index for January 2021". Technology News and Information by SeniorDBA. Archived from the original on 21 March 2021. Retrieved 26 February 2021.
"TIOBE Index". TIOBE. Retrieved 31 March 2025.
"Quotes about Python". Python Software Foundation. Archived from the original on 3 June 2020. Retrieved 8 January 2012.
"Organizations Using Python". Python Software Foundation. Archived from the original on 21 August 2018. Retrieved 15 January 2009.
"Python : the holy grail of programming". CERN Bulletin (31/2006). CERN Publications. 31 July 2006. Archived from the original on 15 January 2013. Retrieved 11 February 2012.
Shafer, Daniel G. (17 January 2003). "Python Streamlines Space Shuttle Mission Design". Python Software Foundation. Archived from the original on 5 June 2020. Retrieved 24 November 2008.
"Tornado: Facebook's Real-Time Web Framework for Python – Facebook for Developers". Facebook for Developers. Archived from the original on 19 February 2019. Retrieved 19 June 2018.
"What Powers Instagram: Hundreds of Instances, Dozens of Technologies". Instagram Engineering. 11 December 2016. Archived from the original on 15 June 2020. Retrieved 27 May 2019.
"How we use Python at Spotify". Spotify Labs. 20 March 2013. Archived from the original on 10 June 2020. Retrieved 25 July 2018.
Fortenberry, Tim (17 January 2003). "Industrial Light & Magic Runs on Python". Python Software Foundation. Archived from the original on 6 June 2020. Retrieved 11 February 2012.
Taft, Darryl K. (5 March 2007). "Python Slithers into Systems". eWeek.com. Ziff Davis Holdings. Archived from the original on 13 August 2021. Retrieved 24 September 2011.
GitHub – reddit-archive/reddit: historical code from reddit.com., The Reddit Archives, archived from the original on 1 June 2020, retrieved 20 March 2019
"Real time communication at scale with Elixir at Discord". 8 October 2020.
"What Programming Language is Baidu Built In?". 5 July 2018.
"Usage statistics and market share of Python for websites". 2012. Archived from the original on 13 August 2021. Retrieved 18 December 2012.
Oliphant, Travis (2007). "Python for Scientific Computing". Computing in Science and Engineering. 9 (3): 10–20. Bibcode:2007CSE.....9c..10O. CiteSeerX 10.1.1.474.6460. doi:10.1109/MCSE.2007.58. ISSN 1521-9615. S2CID 206457124. Archived from the original on 15 June 2020. Retrieved 10 April 2015.
Millman, K. Jarrod; Aivazis, Michael (2011). "Python for Scientists and Engineers". Computing in Science and Engineering. 13 (2): 9–12. Bibcode:2011CSE....13b...9M. doi:10.1109/MCSE.2011.36. Archived from the original on 19 February 2019. Retrieved 7 July 2014.
Science education with SageMath, Innovative Computing in Science Education, archived from the original on 15 June 2020, retrieved 22 April 2019
"OpenCV: OpenCV-Python Tutorials". docs.opencv.org. Archived from the original on 23 September 2020. Retrieved 14 September 2020.
Dean, Jeff; Monga, Rajat; et al. (9 November 2015). "TensorFlow: Large-scale machine learning on heterogeneous systems" (PDF). TensorFlow.org. Google Research. Archived (PDF) from the original on 20 November 2015. Retrieved 10 November 2015.
Piatetsky, Gregory. "Python eats away at R: Top Software for Analytics, Data Science, Machine Learning in 2018: Trends and Analysis". KDnuggets. Archived from the original on 15 November 2019. Retrieved 30 May 2018.
"Who is using scikit-learn? – scikit-learn 0.20.1 documentation". scikit-learn.org. Archived from the original on 6 May 2020. Retrieved 30 November 2018.
Jouppi, Norm. "Google supercharges machine learning tasks with TPU custom chip". Google Cloud Platform Blog. Archived from the original on 18 May 2016. Retrieved 19 May 2016.
De Raedt, Luc; Kimmig, Angelika (2015). "Probabilistic (logic) programming concepts". Machine Learning. 100 (1): 5–47. doi:10.1007/s10994-015-5494-z. S2CID 3166992.
"Natural Language Toolkit – NLTK 3.5b1 documentation". www.nltk.org. Archived from the original on 13 June 2020. Retrieved 10 April 2020.
Andersen, C. and Swift, T., 2023. The Janus System: a bridge to new prolog applications. In Prolog: The Next 50 Years (pp. 93–104). Cham: Springer Nature Switzerland.
"SWI-Prolog Python interface". Archived from the original on 15 March 2024. Retrieved 15 March 2024.
Tarau, P., 2023. Reflections on automation, learnability and expressiveness in logic-based programming languages. In Prolog: The Next 50 Years (pp. 359–371). Cham: Springer Nature Switzerland.
"Tkinter — Python interface to TCL/Tk". Archived from the original on 18 October 2012. Retrieved 9 June 2023.
"Python Tkinter Tutorial". 3 June 2020. Archived from the original on 9 June 2023. Retrieved 9 June 2023.
"Installers for GIMP for Windows – Frequently Asked Questions". 26 July 2013. Archived from the original on 17 July 2013. Retrieved 26 July 2013.
"jasc psp9components". Archived from the original on 19 March 2008.
"About getting started with writing geoprocessing scripts". ArcGIS Desktop Help 9.2. Environmental Systems Research Institute. 17 November 2006. Archived from the original on 5 June 2020. Retrieved 11 February 2012.
CCP porkbelly (24 August 2010). "Stackless Python 2.7". EVE Community Dev Blogs. CCP Games. Archived from the original on 11 January 2014. Retrieved 11 January 2014. "As you may know, EVE has at its core the programming language known as Stackless Python."
Caudill, Barry (20 September 2005). "Modding Sid Meier's Civilization IV". Sid Meier's Civilization IV Developer Blog. Firaxis Games. Archived from the original on 2 December 2010. "we created three levels of tools ... The next level offers Python and XML support, letting modders with more experience manipulate the game world and everything in it."
"Python Language Guide (v1.0)". Google Documents List Data API v1.0. Archived from the original on 15 July 2010.
"4.0 New Features and Fixes". LibreOffice.org. The Document Foundation. 2013. Archived from the original on 9 February 2014. Retrieved 25 February 2013.
"Python Setup and Usage". Python Software Foundation. Archived from the original on 17 June 2020. Retrieved 10 January 2020.
"What is Sugar?". Sugar Labs. Archived from the original on 9 January 2009. Retrieved 11 February 2012.
"Immunity: Knowing You're Secure". Archived from the original on 16 February 2009.
"Core Security". Core Security. Archived from the original on 9 June 2020. Retrieved 10 April 2020.
"Gotchas for Python Users". boo.codehaus.org. Codehaus Foundation. Archived from the original on 11 December 2008. Retrieved 24 November 2008.
Esterbrook, Charles. "Acknowledgements". cobra-language.com. Cobra Language. Archived from the original on 8 February 2008. Retrieved 7 April 2010.
"Proposals: iterators and generators [ES4 Wiki]". wiki.ecmascript.org. Archived from the original on 20 October 2007. Retrieved 24 November 2008.
"Frequently asked questions". Godot Engine documentation. Archived from the original on 28 April 2021. Retrieved 10 May 2021.
Kincaid, Jason (10 November 2009). "Google's Go: A New Programming Language That's Python Meets C++". TechCrunch. Archived from the original on 18 January 2010. Retrieved 29 January 2010.
Strachan, James (29 August 2003). "Groovy – the birth of a new dynamic language for the Java platform". Archived from the original on 5 April 2007. Retrieved 11 June 2007.
"Modular Docs – Why Mojo". docs.modular.com. Archived from the original on 5 May 2023. Retrieved 5 May 2023. "Mojo as a member of the Python family [..] Embracing Python massively simplifies our design efforts, because most of the syntax is already specified. [..] we decided that the right long-term goal for Mojo is to provide a superset of Python (i.e. be compatible with existing programs) and to embrace the CPython immediately for long-tail ecosystem enablement. To a Python programmer, we expect and hope that Mojo will be immediately familiar, while also providing new tools for developing systems-level code that enable you to do things that Python falls back to C and C++ for."
Spencer, Michael (4 May 2023). "What is Mojo Programming Language?". datasciencelearningcenter.substack.com. Archived from the original on 5 May 2023. Retrieved 5 May 2023.
Yegulalp, Serdar (16 January 2017). "Nim language draws from best of Python, Rust, Go, and Lisp". InfoWorld. Archived from the original on 13 October 2018. Retrieved 7 June 2020. "Nim's syntax is strongly reminiscent of Python's, as it uses indented code blocks and some of the same syntax (such as the way if/elif/then/else blocks are constructed)."
"An Interview with the Creator of Ruby". Linuxdevcenter.com. Archived from the original on 28 April 2018. Retrieved 3 December 2012.
Lattner, Chris (3 June 2014). "Chris Lattner's Homepage". Chris Lattner. Archived from the original on 22 December 2015. Retrieved 3 June 2014. "I started work on the Swift Programming Language in July of 2010. I implemented much of the basic language structure, with only a few people knowing of its existence. A few other (amazing) people started contributing in earnest late in 2011, and it became a major focus for the Apple Developer Tools group in July 2013 [...] drawing ideas from Objective-C, Rust, Haskell, Ruby, Python, C#, CLU, and far too many others to list."
Jalan, Nishant Aanjaney (10 November 2022). "Programming in Kotlin". CodeX. Retrieved 29 April 2024.
Kupries, Andreas; Fellows, Donal K. (14 September 2000). "TIP #3: TIP Format". tcl.tk. Tcl Developer Xchange. Archived from the original on 13 July 2017. Retrieved 24 November 2008.
Gustafsson, Per; Niskanen, Raimo (29 January 2007). "EEP 1: EEP Purpose and Guidelines". erlang.org. Archived from the original on 15 June 2020. Retrieved 19 April 2011.

    "Swift Evolution Process". Swift Programming Language Evolution repository on GitHub. 18 February 2020. Archived from the original on 27 April 2020. Retrieved 27 April 2020.

Sources

    "Python for Artificial Intelligence". Python Wiki. 19 July 2012. Archived from the original on 1 November 2012. Retrieved 3 December 2012.
    Paine, Jocelyn, ed. (August 2005). "AI in Python". AI Expert Newsletter. Amzi!. Archived from the original on 26 March 2012. Retrieved 11 February 2012.
    "PyAIML 0.8.5 : Python Package Index". Pypi.python.org. Retrieved 17 July 2013.
    Russell, Stuart J. & Norvig, Peter (2009). Artificial Intelligence: A Modern Approach (3rd ed.). Upper Saddle River, NJ: Prentice Hall. ISBN 978-0-13-604259-4.

Further reading

    Downey, Allen (July 2024). Think Python: How to Think Like a Computer Scientist (3rd ed.). O'Reilly Media. ISBN 978-1098155438.
    Lutz, Mark (2013). Learning Python (5th ed.). O'Reilly Media. ISBN 978-0-596-15806-4.
    Summerfield, Mark (2009). Programming in Python 3 (2nd ed.). Addison-Wesley Professional. ISBN 978-0-321-68056-3.
    Ramalho, Luciano (May 2022). Fluent Python. O'Reilly Media. ISBN 978-1-4920-5632-4.

External links
Python
at Wikipedia's sister projects

    Media from Commons
    Quotations from Wikiquote
    Textbooks from Wikibooks
    Resources from Wikiversity
    Data from Wikidata

    Official website Edit this at Wikidata
    The Python Tutorial

    vte

Python
Implementations	

    CircuitPython CLPython CPython Cython MicroPython Numba IronPython Jython Psyco PyPy Python for S60 Shed Skin Stackless Python Unladen Swallow more...

	
IDEs	

    eric IDLE Ninja-IDE PyCharm PyDev Spyder more...

Topics	

    WSGI ASGI

Designer	

    Guido van Rossum

    Software (list) Python Software Foundation Python Conference (PyCon)

    vte

Programming languages

    Comparison Timeline History

    Ada ALGOL
        Simula APL Assembly BASIC
        Visual Basic
            classic .NET C C++ C# COBOL Erlang
        Elixir Forth Fortran Go Haskell Java JavaScript Julia Kotlin Lisp Lua MATLAB ML
        Caml
            OCaml Pascal
        Object Pascal Perl
        Raku PHP Prolog Python R Ruby Rust SAS SQL Scratch Shell Smalltalk Swift more...

    Lists: Alphabetical Categorical Generational Non-English-based Category

    vte

Python web frameworks

    vte

Differentiable computing

    vte

Free and open-source software

    vte

Statistical software

    vte

Numerical-analysis software
Authority control databases Edit this at Wikidata
Categories:

    Python (programming language)Class-based programming languagesNotebook interfaceComputer science in the NetherlandsConcurrent programming languagesCross-platform free softwareCross-platform softwareDutch inventionsDynamically typed programming languagesEducational programming languagesHigh-level programming languagesInformation technology in the NetherlandsMulti-paradigm programming languagesObject-oriented programming languagesPattern matching programming languagesProgramming languagesProgramming languages created in 1991Scripting languagesText-oriented programming languagesMonty Python references


