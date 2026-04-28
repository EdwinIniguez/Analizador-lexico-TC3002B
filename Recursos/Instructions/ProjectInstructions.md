# Compiler’s Project - Lexical Analysis Phase

## I. Introduction

The evaluation of this challenge’s phase is constituted by two parts. The first part is the evaluation of the
functioning software, whose weight is 50% of the total evaluation. The other 50% will be formed by the
quality correctness of the written report. The evaluation metrics for each part are shown in the following
sections. For the evaluation of the functionality of the software, there will be an individual one-to-one
session with each student, in which an oral exam will be applied to the student, and it will be applied as a
multiplier of the total evaluation grade.

Table #1 provides a summary of how the evaluation is formed for the project. Specific evaluation
metrics for each part of the evaluation are provided in the following pages of this document.
The compiler’s lexical requirements for the challenge’s goal are described on Section II. The project’s
outcomes, i.e., the scanner outputs, the report’s deliverables, and the implementation restrictions for the
scanner software are presented on Section III. Section IV describes the Software evaluation metrics. Section
V describes the Oral Exam part of the evaluation as well as its components. Finally, Section VI presents the
contents’s structure and evaluation metrics for the written report.

| Evaluation     | Weight |
|----------------|--------|
| Software       | 50%    |
| Written Report | 50%    |
| Oral Exam      | x 100% |
*Table #1: Evaluation Summary*

---

## II. Triton Lexical Specification

The lexical analyzer or scanner is the first phase of the translation process of a compiler for any given
programming language. The main purpose of the lexical phase is to identify the tokens or valid member
strings of the programming language, in the order in which they appear in the source file. Another important
task of the scanner is to construct the preliminary version of the symbol table for all kind of tokens, which
will later be used by the syntax, semantics, and intermediate code generator phases.

For the challenge of our Learning Unit, you will implement a scanner using the lex tool to recognize the
lexemes of the Triton GPU kernel. Triton is a Python-like domain-specific language (DSL) for writing
GPU kernels. Developed by OpenAI, Triton allows developers to write high-performance GPU code using
familiar Python syntax with specialized tensor operations.

The team will have to generate the informal lexical specification for the Triton GPU kernel language as
approved by the leader of the leaning Unit, Dr. Salvador Hinojosa. Once the team obtains Dr. Hinojosa’s
approval of your informal lexical specification then you will proceed to develop all the activities asked for
the development of this part of the challenge.

The scanner must be able to identify all the necessary lexemes that conform the approved informal lexical
specification of the Triton GPU kernel language. Therefore, as first step, a description of such set of
lexemes must be generated and justified, in order to construct the Scanner. The following considerations
shall be observed:
a) Include only the necessary keywords and special symbols to accomplish the goal.
b) Disregard any unnecessary lexeme from the original language.
c) Generate the corresponding error messages.

---

## III. SCANNER Output:
The Scanner shall provide the following outputs:
1. Sequence of Tokens in the structure as was seen in class.
2. The required Symbol Table for those tokens that require it.

### b) Deliverables:
The project must include the following deliverables:
1. The approved informal description of the lexemes required to achieve the goal.
2. The regular expression for each kind of token.
3. The automata that recognize the required lexemes.
4. Tokens and their identification (Token ID).
5. Transition Table.
6. Symbol Tables for the required tokens.
7. Implementation of the Scanner using UNIX-lex.
8. Example of the Scanner Outputs.

### c) RESTRICTIONS:
1. The scanner MUST be implemented using lex as seen in class.
2. The scanner CAN NOT be implemented by using any kind of APIs native to the programming language used to develop the project.
3. REGEX libraries can be used for more complex uses cases thar involves regular expressions.
4. You CAN NOT use Python's built-in ast module

---

## IV. Written Report

Once all the previous problem’s features are being clearly and concisely formulated and stated as seen during lectures, the following
step is to implement the development of the software system project process model. All development process models include in one
way or another the following phases: Analysis, Design, Implementation, Testing, and Deployment. The development of the scanner
should be based on the IEEE-830 standard.

The structure of report for the scanner must include the following sections:

### 1. Introduction
#### 1.1.- Summary
Brief description of the contents of this report.
#### 1.2.- Notation
Give a brief description of finite state machines, regular expressions, and transition tables:
- Explain about the model used for the development of the analysis and design phases.
- Justification regarding the selected model.
- Explanation and justification of the programming language used for the implementation, in this case the lex tool.

### 2. Analysis
The analysis model it’s a bridge between the system level description that describes overall system’s functionalities and the
system design. The primary focus of this model is on the whats not the hows. What I/O the system manipulates (data), what
functions the system must perform, what are the behaviors that the system exhibit, what interfaces are defined, and what
constraints apply. The analysis model shall achieve three primary objectives: 1) describe what the customer requires, 2)
establish the basis for the creation of the software system design, and 3) define a set of requirements that can be validated
(tested) once the software system is built.

In this section, the student shall describe the requirements of the system which are represented by the eight deliverables for
the scanner. It must include all the steps that are required to generate the complete set of formal specifications for them. It must
include a concise and precise explanation of every step of the process, by making clear “what is required to do” and “why”.

In summary, this section shall provide a brief description and explanation of the lexical components required to achieve the
goal. It shall include the informal lexical description of the language, and the formal specification in the form of regular
expression for each kind of token. You must describe all the considerations taken in order to develop these models. Be sure to
explain every regular expression and how they comply with the Lexical Definition of the challenge’s goal.

### 3. Design
Design and development represent the process of turning the specification (analysis model) into reality (the product). It’s an
iterative process through which the requirements are translated into a “blueprint” of “how” to construct the system.

There are several characteristics that represent a good design:
- The design must implement all the explicit requirements contained in the analysis model.
- The design must be a readable and understandable guide for the developers and testers.
- The design must provide a complete “picture” of the system, addressing the data, functional, and behavioral domains from
an implementation perspective.
- A design should exhibit an architecture that depicts its modularity, that is, it must show how the system is subdivided into
subsystems, how the different requirements are assigned to these subsystems, and which system functionalities are attached
to hardware and which to software.

The design MUST be conformed by a complete and consistent set of design diagrams (state and flow diagrams, module
diagrams, etc). Pseudo code MUST be used to complement state and flow diagrams.

Furthermore, the design model MUST BE TRACEABLE TO THE ANALYSIS MODEL, that is, for every functional
requirement specified during analysis, the design model shall explicitly describe “how” this requirement will be implemented.
Therefore, the design model becomes the blueprints of how the software system will be implemented. It must be a self
sufficient, complete, accurate, consistent, traceable, and maintainable document, whose purpose is to guide and tell the
programmer how to develop the code.

The implementation MUST be completely based on the design, and traceable to it. The “acid test” for the design is to
consider that if you deliver your design to a completely different developer team, each member of the new team will be able to
understand your document and use it to generate the code with out further interaction with you.

In summary, in this section, the student shall generate a precise DFA that recognize all the tokens enumerated in the analysis
phase, and provide the most efficient Transition Table. The design must include the Token IDs. In addition, it shall provide an
algorithmic description as well as the data structures required to implement the main components of the scanner, i.e., how the
Symbol Tables are implemented.

### 4. Implementation
In this section, a complete printout of the lex file for the scanner must be provided, completely explaining each code element
of the three sections that constituite the lex file in comprehensive and coherent narrrative:
a) Definion Section.
b) Rules Section.
c) User Code Section

### 5. Verification and Validation
The student must present a Test model. The test model consists of the set of test cases that are developed during the test case
design.

During and after the implementation process, the system being developed must be checked to ensure that it meets its
specification and delivers the functionality expected by the customer. Verification and Validation (V&V) is the name given to
these checking processes. V&V starts with requirements reviews and continues through design reviews and hardware and code
inspections up to product testing.

Verification and validation is not the same thing, verification deals with “are we building the product right?” while
validation deals with “are we building the right product?” Verification involves checking that the system conforms to its
specification. The developer must check that it meets its specified functional and non-functional requirements. However,
validation aims to ensure that the system meets the expectation of the customer. The ultimate goal of the V&V process is to
establish confidence that the system is good enough for its intended use.

In order to perform the V&V, the developer must implement a Test Case Design phase. The test cases are part of system and
component testing where the developer designs the test cases (inputs and predicted outputs) that test the system. The goal of this
phase is to create a set of test cases that are effective in discovering hardware and software defects and showing that the system
meets its requirements. To design a test case, the developer must select a particular feature of the system or component that is to
be tested. Then, the developer must select a set of inputs that execute that feature, document the corresponding outputs, and
check that the actual and expected outputs are the same.

Provide your own set of test files and their expected results. Your implementation MUST pass your test files as well as the
professor’s test cases. Be sure to include snapshots of the Scanner’s output for your test cases, together with the corresponding
explanation.

### 6. References
Any information that is used to develop this document must be listed on a standard bibliography format.

With respect to bibliography, the IEEE Reference Style must be used. This style incorporates common practices of
bibliographic references of the scientific and technical fields. This style uses numeric references enclosed on square brackets
inserted into the text, whenever the writer needs to link the text to a bibliography entry. The bibliography list must include all the
references used on the text. The general structure of an input on the bibliography list is the following:
- Author or authors, begins with the first name followed by the last.
- Title: Every main word starts with a capital letter and all are italic. If the source is not a book or an article, a description of
the source must be included.
- Publisher information: editor and year.
- Page numbers:

In case of articles from scientific journals, the name of the author is followed by the title of the article. The title of the article
must be enclosed between quotation marks. Following, the complete name of the journal must be written in italics. Immediately,
the volume number as well as the issue number must be included. Finally, the date enclosed in parenthesis, and followed by
colon and the pages numbers.

Example of a book entry to the bibliography list:
1. Noam Chomsky and Morris Halle, The Sound Pattern of English, (Prentice Hall, 1968), 77-81

Example of a journal article entry to the bibliography list:
2. Keith A. Nelson, R.J Swayne Millar, and Michael D. Fayer, “Optical Generation of Tunable Ultrasonic Waves”,
Journal of Applied Physics 53, no 2 (February 1982): 11-29.

Example of internet references entries to the bibliography list:
3. William J. Mitchel, City of Bits: Space, Place, and the Infobahn [book on-line] (Cambridge, Mass: MIT press,
1995, accessed 29 September 1995); available from http://www-
mitpress.mit.edu:80/city_of_Bits/Pulling_Glass/Index.html; Internet.
4. Joanne C. Baker and Richard W. Hunstead, “Revealing the effects of Orientation in Composite Quasar Spectra”,
Astrophysical Journal 452, 20 October 1995 [journal on-line]; available from
http://www.aas.org/ApJ/v452n2/5309/5309.html; Internet; accessed 29 September 1995.

Example of lecture notes references entry to the bibliography list:
5. R. Castelló, Class Lecture, Topic: “Chapter 2 – Lexical Analysis.” TC3048, School of Engineering and Science,
ITESM, Chihuahua, Chih, April, 2020.

Example of text’s citation/reference:
TEXT:
_________________________________________________________________________________________________
The hardest single part of building a software system is deciding precisely what to build. No other part of the conceptual
work is as difficult as establishing the detailed technical requirements. No other part of the work so cripples the resulting
system if done wrong. No other part is as difficult to rectify later. [2]
_________________________________________________________________________________________________
Bibliography:
1. Noam Chomsky and Morris Halle, The Sound Pattern of English, (Prentice Hall, 1968), 77-81
2. Frederick P. Brooks, Jr. The Mythical Man-Month, Addison Wesley, 1995.
________________________________________________________________________________________________

You can find the complete IEEE Reference Style guide, in the following web pages:
- http://libraryguides.vu.edu.au/ieeereferencing/home
- https://ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf