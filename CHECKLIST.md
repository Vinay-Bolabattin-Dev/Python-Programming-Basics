# Python Revision Checklist
# [x] = revised / [ ]= not yet 

## Phase 1: Logic & Flow 
- [x] If / Elif / Else
- [x] Nested Conditionals
- [x] For Loops
- [x] While Loops
- [x] Nested Loop & pattern printing and also using user inputs to print 
- [x] continue & break 
- [x] Range()

## Phase 2: Data Storage
- [x] string 
- [x] set 
- [x] Lists & Tuples
- [x] Dictionaries (Key-Value)

## phase 3: Function & methods 
- [x] types of  functions
- [x] Recurstions

________________________________________________________________________
========================================================================
## Phase 4: OOPs (The Final Boss)
- [x] Classes & Objects
- [x] The __init__ & self (Constructor)
- [x] __del__ Distructor
- [x] class and instance attributes
- [x] Inheritance 
    ## its types 
    - [x] single Inheritance
    - [x] multilevel Inheritance
    - [x] multiple Inheritance
    - [x] mro method (Method Resolution Order)
    - [x] Hierarchical Inheritance
    - [x] Hybrid Inheritance
- [x] Encapsulation
    ## Access Modifiers 
    - [x]Public
    - [x]privte
    - [x]protected
    - [x] Getter & Setter
- [x] polymorphism 
- [x] abstraction 

=============================================================================

## Phase 5: file i/o in python
- [x] writing 
- [x] reading 
- [x] append 
- [x] deleting  
- [x] Serching 

## Phase 6 : Exception Handling 
- [x] try 
- [x] except
- [x] else
- [x] finally 
- [x] file safety
- [x] raise

## Phase 7: Methods
- [x] static method (Decorator)
- [x] method overriding / super()
- [x] method overloading 
- [x] del Keyword (Memory claen up)
- [x] @classmethod and @staticmethod
-----------------------------------------------------------------------
## Advance Phase: 
- [x] Advance Exception handling
- [x] OOP Polish (Dunder methods & @property)
   - [x] twin printing method ( __str__ & __repr__)
   - [x] math &operator magic method (__add__ / __sub__)
   - [x] lifecycle magic method ( __len__ )
- [x] Advance file handling 
   - [x] writing  (.json files ) using  json.dump()
   - [x] reading  (.json files ) using json.load()
   - [x] Binary file handling 
- [x] Modules & Packages (Importing code)


======================================================================================================
======================================================================================================
            JSON (Java script object Notation )
______________________________________________________________________________________________________    
# 📊 Python Dictionaries & JSON Learning Roadmap

A structured tracking module for mastering data keys, nesting, and web serialization formats.

---

## 📂 PHASE 1: Dictionary Mechanics
- [x] Initialize module (`dictionary_notes.py`)
- [x] Core Syntax: Constructing `{key: value}` maps
- [x] Data Retrieval: Reading values safely via explicit keys
- [x] State Manipulation: Adding new pairs & updating existing values
- [x] Data Eviction: Removing records using `del` and `.pop()`

## ⚙️ PHASE 2: Core Methods & Traversal
- [x] Crash Prevention: Fetching values safely using `.get()`
- [x] Data Extraction: Isolating `.keys()`, `.values()`, and `.items()`
- [x] Iteration Flow: Scanning data records using structured `for` loops
- [x] Data Hierarchies: Designing nested structures (Objects inside Objects)

## 🌐 PHASE 3: The JSON Pipeline (API Ready)
- [x] Data Mapping: Comparing Python Dict structures vs Raw JSON strings
- [x] Deserialization: Parsing incoming strings into Dicts using `json.loads()`
- [x] Serialization: Converting Dicts into transportable strings using `json.dumps()`
- [x] File I/O: Reading and writing directly to external `.json` files

======================================================================================================
======================================================================================================
             NETWORK I/O & LIVE APIs (The Connected System)
______________________________________________________________________________________________________    
- [x] Simulation Mechanics: Handling status codes via Mock Response objects
- [x] Dependency Management: Installing third-party modules safely via `pip`
- [x] The Living Connection: Making live `requests.get()` calls to real web URLs
- [x] Parsing the Web: Decoding remote JSON payloads into active Python memory
- [x] Local Caching: Writing network-fetched JSON data directly into persistent storage files

========================================================================================================
##       WEB BACKEND & SQL DATABASE (The Data-Driven Server)
========================================================================================================

## Phase : Web Architecture & HTTP Essentials 

- [x] Initialize backend environment (backend_notes.py)
- [x] The Client-Server Model: Understanding how apps and browsers request data from a server
- [x] HTTP Methods: Mastering the core actions (GET, POST, PUT, DELETE)
- [x] HTTP Status Codes: Decoding responses (200 OK, 201 Created, 404 Not Found, 500 Server Error)
---------------------------------------------------------------------------------------------------------


## Phase : SQL & Database Foundations (From Scratch)
- [x] Database Basics: Understanding tables, columns, rows, and Primary Keys
- [x] SQL Basics (CRUD): Writing raw queries to create data (INSERT), read data (SELECT), update data (UPDATE), and delete data (DELETE)
- [x] Filtering Data: Using WHERE, AND/OR, and sorting results using ORDER BY
- [x] The Wildcard LIKE Operator (Pattern Matching)
--------------------------------------------------------------------------------------------------------

## Phase : Connecting Python to SQL (The Final Bridge)  
- [ ] The Database Driver: Using Python's built-in sqlite3 module to run SQL commands from your script
- [ ] The Full Cycle: Building a Python application that takes user input, stores it permanently in an SQL database, and reads it back out