from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Create a new Document
doc = Document()

# Add title
title = doc.add_heading('Software Requirements Specification', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add subtitle
subtitle = doc.add_paragraph('Ask Holmes Application')
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add version info
version = doc.add_paragraph('Version 1.0')
version.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add section break for title page (to allow vertical centering)
doc.add_section()

# Set vertical alignment to center for the first section (title page)
first_section = doc.sections[0]
sectPr = first_section._sectPr
vAlign = OxmlElement('w:vAlign')
vAlign.set(qn('w:val'), 'center')
sectPr.append(vAlign)

# ============================================
# 1. INTRODUCTION
# ============================================
doc.add_heading('1. Introduction', level=1)

# 1.1 Purpose
doc.add_heading('1.1 Purpose', level=2)
doc.add_paragraph(
    'This Software Requirements Specification (SRS) document describes the functional and '
    'non-functional requirements for the Ask Holmes application. The purpose of this document '
    'is to provide a comprehensive overview of the system requirements, intended audience, '
    'and scope of the application. This document serves as a reference for developers, testers, '
    'and stakeholders involved in the development and deployment of the Ask Holmes application.'
)

# 1.2 Document Conventions
doc.add_heading('1.2 Document Conventions', level=2)
doc.add_paragraph(
    'This document follows standard SRS conventions. Requirements are identified using unique '
    'identifiers with the following prefixes:'
)
doc.add_paragraph('FR: Functional Requirements', style='List Bullet')
doc.add_paragraph('NFR: Non-Functional Requirements', style='List Bullet')
doc.add_paragraph('UX: User Experience Requirements', style='List Bullet')

# 1.3 Intended Audience
doc.add_heading('1.3 Intended Audience', level=2)
doc.add_paragraph('This document is intended for the following audiences:')
doc.add_paragraph('Developers: To understand the technical requirements and implement the system accordingly.', style='List Bullet')
doc.add_paragraph('Testers: To develop test cases and validate the system against the specified requirements.', style='List Bullet')
doc.add_paragraph('Project Managers: To track project progress and ensure requirements are being met.', style='List Bullet')
doc.add_paragraph('Stakeholders: To review and approve the system requirements before development begins.', style='List Bullet')

# 1.4 Product Scope
doc.add_heading('1.4 Product Scope', level=2)
doc.add_paragraph(
    'Ask Holmes is a web-based Retrieval-Augmented Generation (RAG) application that serves as '
    'an intelligent knowledge base for Sherlock Holmes literature. The system enables users to '
    'interact with classic Sherlock Holmes texts through a modern question-and-answer interface.'
)
doc.add_paragraph('The application provides the following core capabilities:')

doc.add_paragraph(
    'Question Management: Users can create, view, edit, and delete questions about Sherlock Holmes '
    'literature. Each question is securely associated with the authenticated user, ensuring data '
    'privacy and isolation.',
    style='List Bullet'
)
doc.add_paragraph(
    'AI-Powered Answers: The application leverages advanced AI technology to generate accurate '
    'answers by searching through indexed Sherlock Holmes books. Using semantic search and '
    'large language models, the system retrieves relevant passages and synthesizes comprehensive '
    'responses grounded in the source material.',
    style='List Bullet'
)
doc.add_paragraph(
    'Trusted Book Sources: Answers are derived exclusively from indexed Sherlock Holmes documents, '
    'ensuring authenticity and reliability. Users can trust that responses are based on the actual '
    'canon rather than fabricated information.',
    style='List Bullet'
)
doc.add_paragraph(
    'Manual Answer Entry: Users have the flexibility to provide their own answers to questions, '
    'edit AI-generated responses, or maintain a personal knowledge base of Sherlock Holmes facts.',
    style='List Bullet'
)

# 1.5 Product Overview
doc.add_heading('1.5 Product Overview', level=2)
doc.add_paragraph(
    'Ask Holmes addresses the need for an intelligent, user-friendly interface to explore and '
    'understand Sherlock Holmes literature. Traditional search methods often fail to provide '
    'contextual answers to complex questions about characters, plots, and themes. Ask Holmes '
    'solves this problem by combining modern AI techniques with classic literature.'
)

doc.add_paragraph('Key Features:')
doc.add_paragraph('Create questions through an intuitive modal-based interface', style='List Bullet')
doc.add_paragraph('View all personal questions in an organized list format', style='List Bullet')
doc.add_paragraph('Edit existing questions and answers at any time', style='List Bullet')
doc.add_paragraph('Delete questions that are no longer needed', style='List Bullet')
doc.add_paragraph('Request AI-generated answers using the "Ask Documents" feature', style='List Bullet')
doc.add_paragraph('Answers are sourced from trusted, indexed Sherlock Holmes books', style='List Bullet')
doc.add_paragraph('User data is isolated and secure through authentication', style='List Bullet')

# 1.6 References
doc.add_heading('1.6 References', level=2)
doc.add_paragraph('The following references were used in the development of this SRS:')
doc.add_paragraph('IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications', style='List Bullet')
doc.add_paragraph('Project Scope Document: Ask Holmes Application Scope', style='List Bullet')
doc.add_paragraph('Technical Architecture Document: System Design and Components', style='List Bullet')

# 1.7 Definitions, Acronyms, and Abbreviations
doc.add_heading('1.7 Definitions, Acronyms, and Abbreviations', level=2)
doc.add_paragraph(
    'This section provides definitions for terms, acronyms, and abbreviations used throughout '
    'this document to ensure clarity and consistent understanding.'
)

# Acronyms subsection
doc.add_heading('1.7.1 Acronyms', level=3)

doc.add_paragraph('AI - Artificial Intelligence: The simulation of human intelligence processes by computer systems, including learning, reasoning, and self-correction.')
doc.add_paragraph('API - Application Programming Interface: A set of protocols and tools that allows different software applications to communicate with each other.')
doc.add_paragraph('ARIA - Accessible Rich Internet Applications: A set of attributes that define ways to make web content more accessible to people with disabilities.')
doc.add_paragraph('CORS - Cross-Origin Resource Sharing: A security mechanism that allows or restricts web applications running at one origin to access resources from a different origin.')
doc.add_paragraph('CPU - Central Processing Unit: The primary component of a computer that performs most of the processing inside the computer.')
doc.add_paragraph('CRUD - Create, Read, Update, Delete: The four basic operations of persistent storage in database applications.')
doc.add_paragraph('CSS - Cascading Style Sheets: A stylesheet language used to describe the presentation and visual formatting of HTML documents.')
doc.add_paragraph('DOM - Document Object Model: A programming interface for HTML documents that represents the page structure as a tree of objects.')
doc.add_paragraph('E2E - End-to-End: A testing methodology that tests the complete flow of an application from start to finish.')
doc.add_paragraph('GPU - Graphics Processing Unit: A specialized processor designed to accelerate graphics rendering and parallel processing tasks.')
doc.add_paragraph('HTML - HyperText Markup Language: The standard markup language for creating web pages and web applications.')
doc.add_paragraph('HTTP - HyperText Transfer Protocol: The foundation protocol used for transmitting data over the World Wide Web.')
doc.add_paragraph('HTTPS - HyperText Transfer Protocol Secure: An encrypted version of HTTP that provides secure communication over a computer network.')
doc.add_paragraph('IEEE - Institute of Electrical and Electronics Engineers: A professional association that develops standards for the electronics and computing industry.')
doc.add_paragraph('JSON - JavaScript Object Notation: A lightweight data interchange format that is easy for humans to read and write and easy for machines to parse.')
doc.add_paragraph('JSX - JavaScript XML: A syntax extension for JavaScript used in React that allows writing HTML-like code within JavaScript.')
doc.add_paragraph('JWT - JSON Web Token: A compact, URL-safe means of representing claims to be transferred between two parties for authentication.')
doc.add_paragraph('LLM - Large Language Model: An AI model trained on vast amounts of text data capable of understanding and generating human-like text.')
doc.add_paragraph('MFA - Multi-Factor Authentication: A security system that requires multiple methods of verification from independent categories of credentials.')
doc.add_paragraph('NLP - Natural Language Processing: A branch of AI that helps computers understand, interpret, and manipulate human language.')
doc.add_paragraph('NPM - Node Package Manager: A package manager for JavaScript that allows developers to share and reuse code packages.')
doc.add_paragraph('ORM - Object-Relational Mapping: A programming technique for converting data between incompatible type systems in object-oriented programming languages.')
doc.add_paragraph('PDF - Portable Document Format: A file format developed by Adobe to present documents independent of application software, hardware, and operating systems.')
doc.add_paragraph('PIP - Pip Installs Packages: The standard package manager for Python used to install and manage software packages.')
doc.add_paragraph('PWA - Progressive Web Application: A type of web application that uses modern web technologies to deliver app-like experiences.')
doc.add_paragraph('RAG - Retrieval-Augmented Generation: An AI framework that combines information retrieval with text generation to produce contextually relevant responses.')
doc.add_paragraph('RAM - Random Access Memory: A type of computer memory that can be read and changed in any order, used to store working data.')
doc.add_paragraph('REST - Representational State Transfer: An architectural style for designing networked applications using stateless client-server communication.')
doc.add_paragraph('SDK - Software Development Kit: A collection of software development tools in one installable package used to develop applications.')
doc.add_paragraph('SHA - Secure Hash Algorithm: A family of cryptographic hash functions used to verify data integrity.')
doc.add_paragraph('SPA - Single Page Application: A web application that dynamically rewrites the current page rather than loading entire new pages from the server.')
doc.add_paragraph('SQL - Structured Query Language: A domain-specific language used for managing and manipulating relational databases.')
doc.add_paragraph('SRS - Software Requirements Specification: A document that describes what the software will do and how it is expected to perform.')
doc.add_paragraph('SSL - Secure Sockets Layer: A cryptographic protocol designed to provide secure communication over a computer network.')
doc.add_paragraph('TLS - Transport Layer Security: A cryptographic protocol that provides secure communication over a network, successor to SSL.')
doc.add_paragraph('UI - User Interface: The visual elements through which users interact with a software application.')
doc.add_paragraph('URL - Uniform Resource Locator: The address used to access resources on the internet.')
doc.add_paragraph('UTF-8 - Unicode Transformation Format 8-bit: A variable-width character encoding capable of encoding all valid Unicode code points.')
doc.add_paragraph('UUID - Universally Unique Identifier: A 128-bit identifier used to uniquely identify information in computer systems.')
doc.add_paragraph('UX - User Experience: The overall experience of a person using a product, especially in terms of how easy or pleasing it is to use.')
doc.add_paragraph('WSGI - Web Server Gateway Interface: A specification for a universal interface between web servers and Python web applications.')
doc.add_paragraph('XSS - Cross-Site Scripting: A security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users.')

# Definitions subsection
doc.add_heading('1.7.2 Definitions', level=3)

doc.add_paragraph('Anthropic: An AI safety company that develops large language models, including the Claude family of AI assistants used in this application.')
doc.add_paragraph('Authentication: The process of verifying the identity of a user, typically through credentials such as email addresses or passwords.')
doc.add_paragraph('Authorization: The process of determining what permissions an authenticated user has to access specific resources or perform certain actions.')
doc.add_paragraph('Backend: The server-side portion of a web application that handles data processing, business logic, and database operations.')
doc.add_paragraph('Blueprint: In Flask, a way to organize a group of related views and other code, allowing modular application development.')
doc.add_paragraph('Chunk: A segment of text extracted from a document, typically 500 characters with overlap, used for efficient retrieval and processing.')
doc.add_paragraph('Claude: A family of large language models developed by Anthropic, with Claude Haiku being the fast and cost-effective variant used in this application.')
doc.add_paragraph('Component: In React, a reusable piece of UI that encapsulates its own structure, style, and behavior.')
doc.add_paragraph('Context API: A React feature that provides a way to pass data through the component tree without having to pass props manually at every level.')
doc.add_paragraph('Cosine Similarity: A mathematical measure of similarity between two vectors, used to find semantically similar text chunks.')
doc.add_paragraph('Docker: A platform for developing, shipping, and running applications in isolated containers.')
doc.add_paragraph('Embedding: A numerical representation of text as a vector in high-dimensional space, capturing semantic meaning for similarity comparisons.')
doc.add_paragraph('Endpoint: A specific URL path in an API that accepts requests and returns responses for a particular resource or operation.')
doc.add_paragraph('Flask: A lightweight Python web framework used for building web applications and RESTful APIs.')
doc.add_paragraph('Frontend: The client-side portion of a web application that users interact with directly, typically running in a web browser.')
doc.add_paragraph('Gunicorn: A Python WSGI HTTP server commonly used to run Python web applications in production environments.')
doc.add_paragraph('Hook: In React, a function that lets you use state and other React features in functional components.')
doc.add_paragraph('Indexing: The process of extracting text from documents, generating embeddings, and storing them in a database for efficient retrieval.')
doc.add_paragraph('IVFFlat: An index type in pgvector that uses inverted file indexing for approximate nearest neighbor search.')
doc.add_paragraph('Modal: A dialog box or popup window that appears on top of the main content, requiring user interaction before returning to the main view.')
doc.add_paragraph('Nginx: A high-performance web server and reverse proxy server commonly used to serve static files and proxy requests to backend applications.')
doc.add_paragraph('Node.js: A JavaScript runtime built on Chrome\'s V8 JavaScript engine, used for building server-side applications.')
doc.add_paragraph('pgvector: A PostgreSQL extension that adds support for vector similarity search, enabling semantic search capabilities.')
doc.add_paragraph('PostgreSQL: An open-source relational database management system known for reliability, feature robustness, and extensibility.')
doc.add_paragraph('Props: In React, read-only properties passed from parent components to child components to configure their behavior and display.')
doc.add_paragraph('PyPDF2: A Python library used for extracting text, merging, splitting, and manipulating PDF files.')
doc.add_paragraph('Query: A request for data or information from a database, or in RAG context, a user\'s question submitted for answer generation.')
doc.add_paragraph('React: A JavaScript library for building user interfaces, particularly single-page applications, developed by Facebook.')
doc.add_paragraph('Semantic Search: A search technique that understands the contextual meaning of terms to find relevant results beyond exact keyword matching.')
doc.add_paragraph('Sentence Transformers: A Python library for computing dense vector representations of sentences and paragraphs.')
doc.add_paragraph('SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping library for database operations.')
doc.add_paragraph('State: In React, an object that holds data that may change over the lifetime of a component, triggering re-renders when updated.')
doc.add_paragraph('Toast: A brief notification message that appears temporarily on the screen to provide feedback about an operation.')
doc.add_paragraph('Token: In LLM context, a unit of text (word, subword, or character) that the model processes; used for billing and context limits.')
doc.add_paragraph('Vector: A mathematical representation of data as a list of numbers, used in this application for semantic similarity comparisons.')
doc.add_paragraph('Vector Database: A database optimized for storing and querying high-dimensional vector embeddings for similarity search.')
doc.add_paragraph('Viewport: The visible area of a web page in the browser window, which varies based on the device and screen size.')

# Technical Terms subsection
doc.add_heading('1.7.3 Technical Terms', level=3)

doc.add_paragraph('all-MiniLM-L6-v2: A sentence transformer model that produces 384-dimensional embeddings, balancing performance and efficiency.')
doc.add_paragraph('Connection Pooling: A technique of maintaining a cache of database connections that can be reused for future requests.')
doc.add_paragraph('CRUD Operations: The four basic database operations: Create (insert new records), Read (retrieve records), Update (modify records), Delete (remove records).')
doc.add_paragraph('Data Isolation: A security principle ensuring that each user can only access their own data and cannot view or modify other users\' data.')
doc.add_paragraph('Dependency Injection: A design pattern where dependencies are provided to a component rather than created by the component itself.')
doc.add_paragraph('Environment Variable: A dynamic value stored outside the application code that can affect the behavior of running processes.')
doc.add_paragraph('Factory Pattern: A design pattern that provides an interface for creating objects without specifying their concrete classes.')
doc.add_paragraph('Foreign Key: A field in a database table that references the primary key of another table, establishing a relationship between tables.')
doc.add_paragraph('Horizontal Scaling: Adding more machines or instances to distribute load, as opposed to vertical scaling which adds more power to existing machines.')
doc.add_paragraph('Idempotent: An operation that produces the same result regardless of how many times it is executed.')
doc.add_paragraph('Middleware: Software that acts as a bridge between an operating system or database and applications, handling requests and responses.')
doc.add_paragraph('Primary Key: A unique identifier for each record in a database table, ensuring no duplicate entries.')
doc.add_paragraph('Rate Limiting: A technique used to control the number of requests a client can make to an API within a specified time period.')
doc.add_paragraph('Reverse Proxy: A server that sits in front of web servers and forwards client requests to those servers.')
doc.add_paragraph('Service Layer: An architectural pattern that defines an application\'s boundary with a layer of services that establishes business logic.')
doc.add_paragraph('Singleton Pattern: A design pattern that restricts the instantiation of a class to a single instance.')
doc.add_paragraph('Stateless: A system design where no client context is stored on the server between requests; each request contains all information needed to process it.')
doc.add_paragraph('Three-Tier Architecture: A software architecture pattern that separates an application into three logical layers: presentation, application, and data.')
doc.add_paragraph('Timeout: A specified period after which an operation is automatically terminated if not completed.')
doc.add_paragraph('Timestamp: A sequence of characters representing the date and time at which a certain event occurred.')

# ============================================
# 2. PROJECT REQUIREMENTS
# ============================================
doc.add_heading('2. Project Requirements', level=1)
doc.add_paragraph(
    'This chapter defines the detailed functional and non-functional requirements for the '
    'Ask Holmes application. Each requirement is assigned a unique identifier for traceability '
    'and testing purposes.'
)

# ============================================
# 2.1 FUNCTIONAL REQUIREMENTS
# ============================================
doc.add_heading('2.1 Functional Requirements', level=2)
doc.add_paragraph(
    'Functional requirements describe the specific behaviors, features, and functions that the '
    'Ask Holmes application must provide. These requirements are organized by functional area.'
)

# 2.1.1 User Authentication Requirements
doc.add_heading('2.1.1 User Authentication Requirements', level=3)

doc.add_paragraph('FR-AUTH-001: User Registration')
doc.add_paragraph('Description: The system shall allow new users to register by providing a valid email address.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User enters email address in the registration form', style='List Bullet')
doc.add_paragraph('2. System validates email format (contains @ and valid domain)', style='List Bullet')
doc.add_paragraph('3. System checks if email is not already registered', style='List Bullet')
doc.add_paragraph('4. System creates new user account with unique UUID', style='List Bullet')
doc.add_paragraph('5. System displays success message upon successful registration', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-AUTH-002: User Login')
doc.add_paragraph('Description: The system shall allow registered users to log in using their email address.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User enters registered email address', style='List Bullet')
doc.add_paragraph('2. System validates email exists in database', style='List Bullet')
doc.add_paragraph('3. System authenticates user and creates session', style='List Bullet')
doc.add_paragraph('4. System stores user ID in browser local storage', style='List Bullet')
doc.add_paragraph('5. System redirects user to home page', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-AUTH-003: User Logout')
doc.add_paragraph('Description: The system shall allow authenticated users to log out of the application.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User clicks logout button in header', style='List Bullet')
doc.add_paragraph('2. System clears user session from local storage', style='List Bullet')
doc.add_paragraph('3. System redirects user to login page', style='List Bullet')
doc.add_paragraph('4. System prevents access to protected pages without re-authentication', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-AUTH-004: Session Persistence')
doc.add_paragraph('Description: The system shall maintain user session across browser refreshes and new tabs.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User ID is stored in browser local storage upon login', style='List Bullet')
doc.add_paragraph('2. Application checks local storage on page load', style='List Bullet')
doc.add_paragraph('3. If valid user ID exists, user remains authenticated', style='List Bullet')
doc.add_paragraph('4. User can open multiple tabs without re-authenticating', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

# 2.1.2 Question Management Requirements
doc.add_heading('2.1.2 Question Management Requirements', level=3)

doc.add_paragraph('FR-Q-001: Create Question')
doc.add_paragraph('Description: The system shall allow authenticated users to create new questions through a modal interface.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User clicks "Add Question" button on home page', style='List Bullet')
doc.add_paragraph('2. Modal dialog opens with question input form', style='List Bullet')
doc.add_paragraph('3. User enters question text (required field)', style='List Bullet')
doc.add_paragraph('4. User optionally enters answer text', style='List Bullet')
doc.add_paragraph('5. User clicks "Save" button to submit', style='List Bullet')
doc.add_paragraph('6. System validates question is not empty', style='List Bullet')
doc.add_paragraph('7. System saves question with user ID and timestamp', style='List Bullet')
doc.add_paragraph('8. Modal closes and question appears in list', style='List Bullet')
doc.add_paragraph('9. Success toast notification is displayed', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-Q-002: View Questions List')
doc.add_paragraph('Description: The system shall display all questions belonging to the authenticated user.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Home page displays list of user\'s questions', style='List Bullet')
doc.add_paragraph('2. Questions are sorted by creation date (newest first)', style='List Bullet')
doc.add_paragraph('3. Each question shows question text and answer preview', style='List Bullet')
doc.add_paragraph('4. Questions without answers show "No answer yet" indicator', style='List Bullet')
doc.add_paragraph('5. Only questions belonging to current user are displayed', style='List Bullet')
doc.add_paragraph('6. Empty state message shown when no questions exist', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-Q-003: Edit Question')
doc.add_paragraph('Description: The system shall allow users to edit their existing questions.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User clicks edit option from question menu', style='List Bullet')
doc.add_paragraph('2. Modal opens pre-populated with existing question and answer', style='List Bullet')
doc.add_paragraph('3. User modifies question text and/or answer', style='List Bullet')
doc.add_paragraph('4. User clicks "Save" to submit changes', style='List Bullet')
doc.add_paragraph('5. System validates question is not empty', style='List Bullet')
doc.add_paragraph('6. System updates question with new updated_at timestamp', style='List Bullet')
doc.add_paragraph('7. Modal closes and list reflects changes', style='List Bullet')
doc.add_paragraph('8. Success toast notification is displayed', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-Q-004: Delete Question')
doc.add_paragraph('Description: The system shall allow users to permanently delete their questions.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User clicks delete option from question menu', style='List Bullet')
doc.add_paragraph('2. Confirmation dialog appears with warning message', style='List Bullet')
doc.add_paragraph('3. User confirms deletion by clicking "Delete" button', style='List Bullet')
doc.add_paragraph('4. System permanently removes question and associated answer', style='List Bullet')
doc.add_paragraph('5. Question is removed from the displayed list', style='List Bullet')
doc.add_paragraph('6. Success toast notification is displayed', style='List Bullet')
doc.add_paragraph('7. User can cancel deletion by clicking "Cancel" or pressing Escape', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-Q-005: Question Validation')
doc.add_paragraph('Description: The system shall validate question input before saving.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Question text is required and cannot be empty', style='List Bullet')
doc.add_paragraph('2. Question must contain at least one non-whitespace character', style='List Bullet')
doc.add_paragraph('3. Leading and trailing whitespace is trimmed', style='List Bullet')
doc.add_paragraph('4. Answer field is optional (can be empty)', style='List Bullet')
doc.add_paragraph('5. Validation error message displayed for invalid input', style='List Bullet')
doc.add_paragraph('6. Save button disabled when form is invalid', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

# 2.1.3 Answer Management Requirements
doc.add_heading('2.1.3 Answer Management Requirements', level=3)

doc.add_paragraph('FR-A-001: Manual Answer Entry')
doc.add_paragraph('Description: The system shall allow users to manually enter answers to their questions.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Answer textarea is available in question creation/edit modal', style='List Bullet')
doc.add_paragraph('2. User can enter free-form text as answer', style='List Bullet')
doc.add_paragraph('3. Answer is saved with the question', style='List Bullet')
doc.add_paragraph('4. Empty answer is stored as null in database', style='List Bullet')
doc.add_paragraph('5. Answer can be added to questions that previously had none', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-A-002: AI Answer Generation')
doc.add_paragraph('Description: The system shall generate AI-powered answers using the RAG pipeline.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. "Ask Documents" button is visible in question form', style='List Bullet')
doc.add_paragraph('2. Button is disabled when question field is empty', style='List Bullet')
doc.add_paragraph('3. Clicking button triggers RAG query with question text', style='List Bullet')
doc.add_paragraph('4. Loading indicator shown during answer generation', style='List Bullet')
doc.add_paragraph('5. Generated answer is populated in answer textarea', style='List Bullet')
doc.add_paragraph('6. User can edit generated answer before saving', style='List Bullet')
doc.add_paragraph('7. Error message displayed if generation fails', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-A-003: Answer Editing')
doc.add_paragraph('Description: The system shall allow users to edit both manual and AI-generated answers.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Existing answers are editable in the edit modal', style='List Bullet')
doc.add_paragraph('2. AI-generated answers can be modified before saving', style='List Bullet')
doc.add_paragraph('3. Answers can be cleared (set to empty)', style='List Bullet')
doc.add_paragraph('4. Changes are saved when user clicks "Save"', style='List Bullet')
doc.add_paragraph('5. Updated timestamp reflects modification time', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('FR-A-004: Answer Regeneration')
doc.add_paragraph('Description: The system shall allow users to regenerate AI answers.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. "Ask Documents" button can be clicked multiple times', style='List Bullet')
doc.add_paragraph('2. Each click generates a new answer based on current question', style='List Bullet')
doc.add_paragraph('3. New answer replaces previous content in textarea', style='List Bullet')
doc.add_paragraph('4. Saved answers are not affected until user clicks "Save"', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# 2.1.4 RAG Pipeline Requirements
doc.add_heading('2.1.4 RAG Pipeline Requirements', level=3)

doc.add_paragraph('FR-RAG-001: Document Upload')
doc.add_paragraph('Description: The system shall allow uploading PDF documents for indexing.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. File upload button accepts PDF files only', style='List Bullet')
doc.add_paragraph('2. Selected file is uploaded to server books folder', style='List Bullet')
doc.add_paragraph('3. Upload progress indicator is displayed', style='List Bullet')
doc.add_paragraph('4. Success message shown upon completion', style='List Bullet')
doc.add_paragraph('5. Error message shown for invalid file types', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('FR-RAG-002: Document Indexing')
doc.add_paragraph('Description: The system shall process and index uploaded PDF documents.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. System extracts text content from PDF files', style='List Bullet')
doc.add_paragraph('2. Text is split into chunks of 500 characters with 50-character overlap', style='List Bullet')
doc.add_paragraph('3. Each chunk is converted to 384-dimensional vector embedding', style='List Bullet')
doc.add_paragraph('4. Chunks and embeddings are stored in database', style='List Bullet')
doc.add_paragraph('5. Document metadata (filename, hash, chunk count) is recorded', style='List Bullet')
doc.add_paragraph('6. Duplicate documents are detected via file hash', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-RAG-003: Semantic Search')
doc.add_paragraph('Description: The system shall perform semantic similarity search on indexed documents.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. User question is converted to vector embedding', style='List Bullet')
doc.add_paragraph('2. System searches for most similar document chunks', style='List Bullet')
doc.add_paragraph('3. Top 3 most relevant chunks are retrieved', style='List Bullet')
doc.add_paragraph('4. Cosine similarity is used for matching', style='List Bullet')
doc.add_paragraph('5. Search completes within acceptable time limit', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-RAG-004: Answer Generation')
doc.add_paragraph('Description: The system shall generate answers using retrieved context and LLM.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Retrieved chunks are assembled as context', style='List Bullet')
doc.add_paragraph('2. Question and context are sent to Claude Haiku LLM', style='List Bullet')
doc.add_paragraph('3. LLM generates natural language answer', style='List Bullet')
doc.add_paragraph('4. Answer is grounded in the provided context', style='List Bullet')
doc.add_paragraph('5. Response is returned within 60-second timeout', style='List Bullet')
doc.add_paragraph('6. Error handling for API failures', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-RAG-005: Document Management')
doc.add_paragraph('Description: The system shall allow viewing and deleting indexed documents.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. List of indexed documents is viewable', style='List Bullet')
doc.add_paragraph('2. Document details show filename and chunk count', style='List Bullet')
doc.add_paragraph('3. Documents can be deleted from the index', style='List Bullet')
doc.add_paragraph('4. Deleting document removes all associated chunks', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# 2.1.5 User Interface Requirements
doc.add_heading('2.1.5 User Interface Requirements', level=3)

doc.add_paragraph('FR-UI-001: Responsive Layout')
doc.add_paragraph('Description: The system shall provide a responsive layout for desktop and tablet devices.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Layout adapts to screen sizes 1024px and above', style='List Bullet')
doc.add_paragraph('2. All features are accessible on desktop browsers', style='List Bullet')
doc.add_paragraph('3. Content is readable without horizontal scrolling', style='List Bullet')
doc.add_paragraph('4. Interactive elements are appropriately sized', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('FR-UI-002: Modal Dialogs')
doc.add_paragraph('Description: The system shall use modal dialogs for question creation and editing.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Modal opens centered on screen with backdrop overlay', style='List Bullet')
doc.add_paragraph('2. Modal can be closed by clicking X button', style='List Bullet')
doc.add_paragraph('3. Modal can be closed by pressing Escape key', style='List Bullet')
doc.add_paragraph('4. Modal can be closed by clicking backdrop', style='List Bullet')
doc.add_paragraph('5. Focus is trapped within modal when open', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('FR-UI-003: Toast Notifications')
doc.add_paragraph('Description: The system shall display toast notifications for user feedback.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Success messages shown for successful operations', style='List Bullet')
doc.add_paragraph('2. Error messages shown for failed operations', style='List Bullet')
doc.add_paragraph('3. Toasts appear briefly and auto-dismiss', style='List Bullet')
doc.add_paragraph('4. Toasts are positioned consistently on screen', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

doc.add_paragraph('FR-UI-004: Loading States')
doc.add_paragraph('Description: The system shall display loading indicators during async operations.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Loading spinner shown while fetching questions', style='List Bullet')
doc.add_paragraph('2. Loading indicator shown during AI answer generation', style='List Bullet')
doc.add_paragraph('3. Buttons are disabled during loading states', style='List Bullet')
doc.add_paragraph('4. Loading states prevent duplicate submissions', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('FR-UI-005: Error Handling')
doc.add_paragraph('Description: The system shall gracefully handle and display errors.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Network errors display appropriate message', style='List Bullet')
doc.add_paragraph('2. Validation errors show inline feedback', style='List Bullet')
doc.add_paragraph('3. API errors are caught and displayed to user', style='List Bullet')
doc.add_paragraph('4. Application does not crash on errors', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

# 2.1.6 Data Management Requirements
doc.add_heading('2.1.6 Data Management Requirements', level=3)

doc.add_paragraph('FR-DATA-001: Data Isolation')
doc.add_paragraph('Description: The system shall ensure users can only access their own data.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Questions are associated with user ID on creation', style='List Bullet')
doc.add_paragraph('2. API endpoints filter data by authenticated user', style='List Bullet')
doc.add_paragraph('3. Attempts to access other users\' data return 403 error', style='List Bullet')
doc.add_paragraph('4. User ID is validated on all protected endpoints', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-DATA-002: Data Persistence')
doc.add_paragraph('Description: The system shall persist all user data to the database.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Questions are stored in PostgreSQL database', style='List Bullet')
doc.add_paragraph('2. Data survives application restarts', style='List Bullet')
doc.add_paragraph('3. Timestamps are recorded for all records', style='List Bullet')
doc.add_paragraph('4. UUIDs are used for primary keys', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('FR-DATA-003: Cascade Deletion')
doc.add_paragraph('Description: The system shall properly handle related data when deleting records.', style='List Bullet')
doc.add_paragraph('Acceptance Criteria:', style='List Bullet')
doc.add_paragraph('1. Deleting a user removes all associated questions', style='List Bullet')
doc.add_paragraph('2. Deleting a document removes all associated chunks', style='List Bullet')
doc.add_paragraph('3. No orphaned records remain after deletion', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

# ============================================
# 2.2 NON-FUNCTIONAL REQUIREMENTS
# ============================================
doc.add_heading('2.2 Non-Functional Requirements', level=2)
doc.add_paragraph(
    'Non-functional requirements define the quality attributes, constraints, and characteristics '
    'that the Ask Holmes application must exhibit. These requirements address performance, '
    'security, usability, and other system qualities.'
)

# 2.2.1 Performance Requirements
doc.add_heading('2.2.1 Performance Requirements', level=3)

doc.add_paragraph('NFR-PERF-001: API Response Time')
doc.add_paragraph('Description: The system shall respond to API requests within acceptable time limits.', style='List Bullet')
doc.add_paragraph('Requirement: CRUD operations shall complete within 2 seconds under normal load.', style='List Bullet')
doc.add_paragraph('Measurement: Server response time measured from request receipt to response sent.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-PERF-002: RAG Query Response Time')
doc.add_paragraph('Description: The system shall generate AI answers within acceptable time limits.', style='List Bullet')
doc.add_paragraph('Requirement: RAG answer generation shall complete within 60 seconds.', style='List Bullet')
doc.add_paragraph('Measurement: Time from query submission to answer receipt.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-PERF-003: Page Load Time')
doc.add_paragraph('Description: The system shall load pages within acceptable time limits.', style='List Bullet')
doc.add_paragraph('Requirement: Initial page load shall complete within 3 seconds on broadband connection.', style='List Bullet')
doc.add_paragraph('Measurement: Time from navigation to fully rendered page.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-PERF-004: Concurrent Users')
doc.add_paragraph('Description: The system shall support multiple simultaneous users.', style='List Bullet')
doc.add_paragraph('Requirement: System shall support 100 concurrent users under normal operation.', style='List Bullet')
doc.add_paragraph('Maximum Capacity: System shall handle up to 500 concurrent users at peak load.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-PERF-005: Database Query Performance')
doc.add_paragraph('Description: The system shall execute database queries efficiently.', style='List Bullet')
doc.add_paragraph('Requirement: Question list queries shall complete within 500ms.', style='List Bullet')
doc.add_paragraph('Requirement: Vector similarity search shall complete within 2 seconds.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

# 2.2.2 Security Requirements
doc.add_heading('2.2.2 Security Requirements', level=3)

doc.add_paragraph('NFR-SEC-001: Data Isolation')
doc.add_paragraph('Description: The system shall enforce strict data isolation between users.', style='List Bullet')
doc.add_paragraph('Requirement: Users shall only access their own questions and answers.', style='List Bullet')
doc.add_paragraph('Implementation: Server-side validation of user ownership on all requests.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-SEC-002: Input Validation')
doc.add_paragraph('Description: The system shall validate and sanitize all user inputs.', style='List Bullet')
doc.add_paragraph('Requirement: All inputs shall be validated for type, length, and format.', style='List Bullet')
doc.add_paragraph('Requirement: Input sanitization shall prevent XSS attacks.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-SEC-003: SQL Injection Prevention')
doc.add_paragraph('Description: The system shall prevent SQL injection attacks.', style='List Bullet')
doc.add_paragraph('Requirement: All database queries shall use parameterized statements via ORM.', style='List Bullet')
doc.add_paragraph('Implementation: SQLAlchemy ORM with bound parameters.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-SEC-004: Secure Communication')
doc.add_paragraph('Description: The system shall encrypt all network communications.', style='List Bullet')
doc.add_paragraph('Requirement: All client-server communication shall use HTTPS/TLS 1.2+.', style='List Bullet')
doc.add_paragraph('Requirement: API keys shall never be exposed to client-side code.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-SEC-005: API Key Protection')
doc.add_paragraph('Description: The system shall securely manage API credentials.', style='List Bullet')
doc.add_paragraph('Requirement: Anthropic API keys shall be stored as environment variables.', style='List Bullet')
doc.add_paragraph('Requirement: API keys shall not be committed to version control.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-SEC-006: Error Message Security')
doc.add_paragraph('Description: The system shall not expose sensitive information in error messages.', style='List Bullet')
doc.add_paragraph('Requirement: Error messages shall not reveal system internals or stack traces to users.', style='List Bullet')
doc.add_paragraph('Requirement: Detailed errors shall only be logged server-side.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

# 2.2.3 Reliability Requirements
doc.add_heading('2.2.3 Reliability Requirements', level=3)

doc.add_paragraph('NFR-REL-001: Data Persistence')
doc.add_paragraph('Description: The system shall reliably persist all user data.', style='List Bullet')
doc.add_paragraph('Requirement: Data shall survive application restarts and server reboots.', style='List Bullet')
doc.add_paragraph('Implementation: PostgreSQL database with ACID compliance.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-REL-002: Error Recovery')
doc.add_paragraph('Description: The system shall gracefully handle errors and recover when possible.', style='List Bullet')
doc.add_paragraph('Requirement: Application shall not crash due to user input errors.', style='List Bullet')
doc.add_paragraph('Requirement: Network failures shall display appropriate messages without data loss.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-REL-003: External Service Failure')
doc.add_paragraph('Description: The system shall handle external service failures gracefully.', style='List Bullet')
doc.add_paragraph('Requirement: Anthropic API failures shall display user-friendly error messages.', style='List Bullet')
doc.add_paragraph('Requirement: Core functionality (CRUD) shall work without external services.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-REL-004: Data Integrity')
doc.add_paragraph('Description: The system shall maintain data integrity at all times.', style='List Bullet')
doc.add_paragraph('Requirement: Database operations shall be atomic (all-or-nothing).', style='List Bullet')
doc.add_paragraph('Requirement: Foreign key constraints shall prevent orphaned records.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

# 2.2.4 Usability Requirements
doc.add_heading('2.2.4 Usability Requirements', level=3)

doc.add_paragraph('NFR-USA-001: Intuitive Interface')
doc.add_paragraph('Description: The system shall provide an intuitive and easy-to-use interface.', style='List Bullet')
doc.add_paragraph('Requirement: New users shall be able to create a question within 2 minutes without training.', style='List Bullet')
doc.add_paragraph('Requirement: Primary actions shall be discoverable without documentation.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-USA-002: Consistent Design')
doc.add_paragraph('Description: The system shall maintain consistent design patterns throughout.', style='List Bullet')
doc.add_paragraph('Requirement: UI elements shall follow consistent styling and behavior.', style='List Bullet')
doc.add_paragraph('Requirement: Navigation patterns shall be predictable across pages.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-USA-003: Feedback')
doc.add_paragraph('Description: The system shall provide clear feedback for all user actions.', style='List Bullet')
doc.add_paragraph('Requirement: Success and error states shall be clearly communicated.', style='List Bullet')
doc.add_paragraph('Requirement: Loading states shall indicate ongoing operations.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-USA-004: Error Messages')
doc.add_paragraph('Description: The system shall display helpful error messages.', style='List Bullet')
doc.add_paragraph('Requirement: Error messages shall explain what went wrong.', style='List Bullet')
doc.add_paragraph('Requirement: Error messages shall suggest corrective actions when possible.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# 2.2.5 Accessibility Requirements
doc.add_heading('2.2.5 Accessibility Requirements', level=3)

doc.add_paragraph('NFR-ACC-001: Keyboard Navigation')
doc.add_paragraph('Description: The system shall support keyboard navigation.', style='List Bullet')
doc.add_paragraph('Requirement: All interactive elements shall be accessible via keyboard.', style='List Bullet')
doc.add_paragraph('Requirement: Tab order shall follow logical reading order.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-ACC-002: Screen Reader Support')
doc.add_paragraph('Description: The system shall be compatible with screen readers.', style='List Bullet')
doc.add_paragraph('Requirement: Interactive elements shall have appropriate ARIA labels.', style='List Bullet')
doc.add_paragraph('Requirement: Dynamic content changes shall be announced.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

doc.add_paragraph('NFR-ACC-003: Color Contrast')
doc.add_paragraph('Description: The system shall maintain sufficient color contrast.', style='List Bullet')
doc.add_paragraph('Requirement: Text shall have minimum 4.5:1 contrast ratio against background.', style='List Bullet')
doc.add_paragraph('Requirement: Interactive elements shall be distinguishable without color alone.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

doc.add_paragraph('NFR-ACC-004: Focus Indicators')
doc.add_paragraph('Description: The system shall provide visible focus indicators.', style='List Bullet')
doc.add_paragraph('Requirement: Focused elements shall have visible outline or highlight.', style='List Bullet')
doc.add_paragraph('Requirement: Focus state shall not rely on color alone.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# 2.2.6 Maintainability Requirements
doc.add_heading('2.2.6 Maintainability Requirements', level=3)

doc.add_paragraph('NFR-MAINT-001: Code Organization')
doc.add_paragraph('Description: The system shall follow established code organization patterns.', style='List Bullet')
doc.add_paragraph('Requirement: Backend shall use service layer pattern for business logic.', style='List Bullet')
doc.add_paragraph('Requirement: Frontend shall use component-based architecture.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-MAINT-002: Separation of Concerns')
doc.add_paragraph('Description: The system shall maintain clear separation of concerns.', style='List Bullet')
doc.add_paragraph('Requirement: Presentation, business logic, and data access shall be separated.', style='List Bullet')
doc.add_paragraph('Requirement: API routes shall delegate to service layer.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-MAINT-003: Configuration Management')
doc.add_paragraph('Description: The system shall externalize configuration.', style='List Bullet')
doc.add_paragraph('Requirement: Environment-specific values shall be configurable via environment variables.', style='List Bullet')
doc.add_paragraph('Requirement: No hardcoded credentials or environment-specific values in code.', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

# 2.2.7 Scalability Requirements
doc.add_heading('2.2.7 Scalability Requirements', level=3)

doc.add_paragraph('NFR-SCALE-001: Horizontal Scalability')
doc.add_paragraph('Description: The system shall support horizontal scaling.', style='List Bullet')
doc.add_paragraph('Requirement: Application shall be stateless to allow multiple instances.', style='List Bullet')
doc.add_paragraph('Requirement: Session data shall be stored externally (database/local storage).', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

doc.add_paragraph('NFR-SCALE-002: Database Scalability')
doc.add_paragraph('Description: The system shall use scalable database patterns.', style='List Bullet')
doc.add_paragraph('Requirement: Database queries shall use proper indexing.', style='List Bullet')
doc.add_paragraph('Requirement: Connection pooling shall be implemented.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-SCALE-003: Document Volume')
doc.add_paragraph('Description: The system shall handle growing document volumes.', style='List Bullet')
doc.add_paragraph('Requirement: Vector search shall remain performant with up to 100,000 chunks.', style='List Bullet')
doc.add_paragraph('Requirement: IVFFlat index shall be used for efficient similarity search.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# 2.2.8 Compatibility Requirements
doc.add_heading('2.2.8 Compatibility Requirements', level=3)

doc.add_paragraph('NFR-COMPAT-001: Browser Compatibility')
doc.add_paragraph('Description: The system shall support modern web browsers.', style='List Bullet')
doc.add_paragraph('Supported Browsers:', style='List Bullet')
doc.add_paragraph('- Google Chrome 100+', style='List Bullet')
doc.add_paragraph('- Mozilla Firefox 100+', style='List Bullet')
doc.add_paragraph('- Microsoft Edge 100+', style='List Bullet')
doc.add_paragraph('- Apple Safari 15+', style='List Bullet')
doc.add_paragraph('Priority: High', style='List Bullet')

doc.add_paragraph('NFR-COMPAT-002: Screen Resolution')
doc.add_paragraph('Description: The system shall support standard screen resolutions.', style='List Bullet')
doc.add_paragraph('Requirement: Minimum supported resolution shall be 1024x768 pixels.', style='List Bullet')
doc.add_paragraph('Requirement: Layout shall be optimized for desktop and tablet viewports.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-COMPAT-003: JavaScript Requirement')
doc.add_paragraph('Description: The system shall require JavaScript for full functionality.', style='List Bullet')
doc.add_paragraph('Requirement: Application requires JavaScript to be enabled in browser.', style='List Bullet')
doc.add_paragraph('Requirement: Graceful message displayed if JavaScript is disabled.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# 2.2.9 Deployment Requirements
doc.add_heading('2.2.9 Deployment Requirements', level=3)

doc.add_paragraph('NFR-DEPLOY-001: Containerization')
doc.add_paragraph('Description: The system shall support containerized deployment.', style='List Bullet')
doc.add_paragraph('Requirement: Application shall be deployable via Docker containers.', style='List Bullet')
doc.add_paragraph('Requirement: Docker Compose shall orchestrate multi-container setup.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-DEPLOY-002: Environment Configuration')
doc.add_paragraph('Description: The system shall support multiple deployment environments.', style='List Bullet')
doc.add_paragraph('Requirement: Configuration shall be managed via environment variables.', style='List Bullet')
doc.add_paragraph('Requirement: Same container image shall work in different environments.', style='List Bullet')
doc.add_paragraph('Priority: Medium', style='List Bullet')

doc.add_paragraph('NFR-DEPLOY-003: Database Migration')
doc.add_paragraph('Description: The system shall support database schema management.', style='List Bullet')
doc.add_paragraph('Requirement: Database schema shall be initialized via SQL scripts.', style='List Bullet')
doc.add_paragraph('Requirement: Schema changes shall be versioned and repeatable.', style='List Bullet')
doc.add_paragraph('Priority: Low', style='List Bullet')

# ============================================
# 3. USE CASE DIAGRAM
# ============================================
doc.add_heading('3. Use Case Diagram', level=1)
doc.add_paragraph(
    'This chapter presents the Use Case Diagram for the Ask Holmes application, illustrating '
    'the interactions between actors and the system. The diagram identifies all primary and '
    'secondary actors, use cases organized by functional packages, and the relationships '
    'between them.'
)

# 3.1 Actors
doc.add_heading('3.1 Actors', level=2)
doc.add_paragraph(
    'The following actors interact with the Ask Holmes application:'
)

doc.add_paragraph('Actor 1: User (Primary Actor)')
doc.add_paragraph('Type: Human', style='List Bullet')
doc.add_paragraph('Description: A registered user of the Ask Holmes application who can create, view, edit, and delete questions, as well as request AI-generated answers from indexed Sherlock Holmes literature.', style='List Bullet')
doc.add_paragraph('Goals: Manage personal Q&A knowledge base, obtain accurate answers about Sherlock Holmes literature.', style='List Bullet')
doc.add_paragraph('Characteristics: Low to moderate technical expertise, familiar with web applications.', style='List Bullet')

doc.add_paragraph('Actor 2: Administrator (Primary Actor)')
doc.add_paragraph('Type: Human', style='List Bullet')
doc.add_paragraph('Description: A system administrator who has all User capabilities plus the ability to upload, index, and manage PDF documents that serve as the knowledge base for the RAG system.', style='List Bullet')
doc.add_paragraph('Goals: Maintain the document repository, ensure indexed content is accurate and up-to-date.', style='List Bullet')
doc.add_paragraph('Characteristics: Moderate to high technical expertise, understands document management.', style='List Bullet')
doc.add_paragraph('Relationship: Inherits from User (specialization)', style='List Bullet')

doc.add_paragraph('Actor 3: Claude API (Secondary Actor)')
doc.add_paragraph('Type: External System', style='List Bullet')
doc.add_paragraph('Description: Anthropic\'s Claude Haiku large language model API that generates natural language answers based on retrieved document context.', style='List Bullet')
doc.add_paragraph('Goals: Provide accurate, contextual answers grounded in the source material.', style='List Bullet')
doc.add_paragraph('Interface: HTTPS REST API', style='List Bullet')

doc.add_paragraph('Actor 4: Embedding Model (Secondary Actor)')
doc.add_paragraph('Type: External System', style='List Bullet')
doc.add_paragraph('Description: Sentence Transformers all-MiniLM-L6-v2 model that generates 384-dimensional vector embeddings for semantic similarity search.', style='List Bullet')
doc.add_paragraph('Goals: Convert text to numerical representations for similarity matching.', style='List Bullet')
doc.add_paragraph('Interface: Local Python library', style='List Bullet')

# 3.2 Use Cases by Package
doc.add_heading('3.2 Use Cases by Package', level=2)

# 3.2.1 Authentication Use Cases
doc.add_heading('3.2.1 Authentication Package', level=3)

doc.add_paragraph('UC-AUTH-001: Register Account')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows a new user to create an account by providing a valid email address.', style='List Bullet')
doc.add_paragraph('Preconditions: User is not logged in, email is not already registered.', style='List Bullet')
doc.add_paragraph('Postconditions: New user account created with unique UUID, user is logged in.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User navigates to registration page', style='List Bullet')
doc.add_paragraph('2. User enters email address', style='List Bullet')
doc.add_paragraph('3. System validates email format', style='List Bullet')
doc.add_paragraph('4. System checks email availability', style='List Bullet')
doc.add_paragraph('5. System creates new user record', style='List Bullet')
doc.add_paragraph('6. System logs user in automatically', style='List Bullet')
doc.add_paragraph('7. System redirects to home page', style='List Bullet')
doc.add_paragraph('Includes: Validate Email Format, Check Email Availability', style='List Bullet')

doc.add_paragraph('UC-AUTH-002: Login')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows a registered user to authenticate and access the application.', style='List Bullet')
doc.add_paragraph('Preconditions: User has a registered account, user is not logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: User is authenticated, session is created.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User navigates to login page', style='List Bullet')
doc.add_paragraph('2. User enters registered email address', style='List Bullet')
doc.add_paragraph('3. System validates email exists in database', style='List Bullet')
doc.add_paragraph('4. System creates user session', style='List Bullet')
doc.add_paragraph('5. System stores user ID in local storage', style='List Bullet')
doc.add_paragraph('6. System redirects to home page', style='List Bullet')
doc.add_paragraph('Includes: Maintain Session', style='List Bullet')

doc.add_paragraph('UC-AUTH-003: Logout')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows an authenticated user to end their session and log out.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: User session is terminated, user is redirected to login page.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User clicks logout button', style='List Bullet')
doc.add_paragraph('2. System clears session from local storage', style='List Bullet')
doc.add_paragraph('3. System redirects to login page', style='List Bullet')

doc.add_paragraph('UC-AUTH-004: Maintain Session')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Maintains user authentication state across page refreshes and browser tabs.', style='List Bullet')
doc.add_paragraph('Preconditions: User has previously logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: User remains authenticated if session is valid.', style='List Bullet')

# 3.2.2 Question Management Use Cases
doc.add_heading('3.2.2 Question Management Package', level=3)

doc.add_paragraph('UC-Q-001: Create Question')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows user to create a new question with optional answer.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: New question is saved to database, question appears in list.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User clicks "Add Question" button', style='List Bullet')
doc.add_paragraph('2. System opens modal dialog', style='List Bullet')
doc.add_paragraph('3. User enters question text (required)', style='List Bullet')
doc.add_paragraph('4. User optionally enters answer text', style='List Bullet')
doc.add_paragraph('5. User clicks "Save" button', style='List Bullet')
doc.add_paragraph('6. System validates question is not empty', style='List Bullet')
doc.add_paragraph('7. System saves question with user ID and timestamp', style='List Bullet')
doc.add_paragraph('8. System closes modal and refreshes list', style='List Bullet')
doc.add_paragraph('9. System displays success toast', style='List Bullet')
doc.add_paragraph('Includes: Open Modal Dialog, Validate Question Input, Display Toast Notification', style='List Bullet')

doc.add_paragraph('UC-Q-002: View Questions List')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Displays all questions belonging to the authenticated user.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: User\'s questions are displayed in sorted order.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User navigates to home page', style='List Bullet')
doc.add_paragraph('2. System fetches questions for current user', style='List Bullet')
doc.add_paragraph('3. System sorts questions by creation date (newest first)', style='List Bullet')
doc.add_paragraph('4. System displays questions with answer previews', style='List Bullet')
doc.add_paragraph('Includes: Display Empty State (when no questions exist)', style='List Bullet')

doc.add_paragraph('UC-Q-003: Edit Question')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows user to modify an existing question and/or answer.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in, question exists, question belongs to user.', style='List Bullet')
doc.add_paragraph('Postconditions: Question is updated with new values and timestamp.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User clicks edit option from question menu', style='List Bullet')
doc.add_paragraph('2. System opens modal with pre-populated data', style='List Bullet')
doc.add_paragraph('3. User modifies question text and/or answer', style='List Bullet')
doc.add_paragraph('4. User clicks "Save" button', style='List Bullet')
doc.add_paragraph('5. System validates and updates question', style='List Bullet')
doc.add_paragraph('6. System closes modal and refreshes list', style='List Bullet')
doc.add_paragraph('Includes: Open Modal Dialog, Validate Question Input, Display Toast Notification', style='List Bullet')

doc.add_paragraph('UC-Q-004: Delete Question')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows user to permanently remove a question.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in, question exists, question belongs to user.', style='List Bullet')
doc.add_paragraph('Postconditions: Question and associated answer are permanently deleted.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User clicks delete option from question menu', style='List Bullet')
doc.add_paragraph('2. System displays confirmation dialog', style='List Bullet')
doc.add_paragraph('3. User confirms deletion', style='List Bullet')
doc.add_paragraph('4. System deletes question from database', style='List Bullet')
doc.add_paragraph('5. System removes question from list', style='List Bullet')
doc.add_paragraph('6. System displays success toast', style='List Bullet')
doc.add_paragraph('Includes: Confirm Deletion, Display Toast Notification', style='List Bullet')

# 3.2.3 Answer Management Use Cases
doc.add_heading('3.2.3 Answer Management Package', level=3)

doc.add_paragraph('UC-A-001: Enter Manual Answer')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows user to manually type an answer to a question.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in, question form is open.', style='List Bullet')
doc.add_paragraph('Postconditions: Answer is saved with the question.', style='List Bullet')

doc.add_paragraph('UC-A-002: Request AI Answer')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Requests an AI-generated answer using the RAG pipeline.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in, question text is entered, documents are indexed.', style='List Bullet')
doc.add_paragraph('Postconditions: AI-generated answer is displayed in answer field.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. User enters question text', style='List Bullet')
doc.add_paragraph('2. User clicks "Ask Documents" button', style='List Bullet')
doc.add_paragraph('3. System displays loading indicator', style='List Bullet')
doc.add_paragraph('4. System triggers RAG pipeline', style='List Bullet')
doc.add_paragraph('5. System receives generated answer', style='List Bullet')
doc.add_paragraph('6. System populates answer in textarea', style='List Bullet')
doc.add_paragraph('Includes: Generate Answer from Documents, Show Loading Indicator', style='List Bullet')
doc.add_paragraph('Extends: Display Error Message (on failure)', style='List Bullet')

doc.add_paragraph('UC-A-003: Edit Answer')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows user to modify an existing answer (manual or AI-generated).', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in, answer exists.', style='List Bullet')
doc.add_paragraph('Postconditions: Answer is updated.', style='List Bullet')

doc.add_paragraph('UC-A-004: Regenerate AI Answer')
doc.add_paragraph('Actor: User', style='List Bullet')
doc.add_paragraph('Description: Allows user to request a new AI-generated answer.', style='List Bullet')
doc.add_paragraph('Preconditions: User is logged in, question text is entered.', style='List Bullet')
doc.add_paragraph('Postconditions: New answer replaces previous content in textarea.', style='List Bullet')
doc.add_paragraph('Includes: Generate Answer from Documents', style='List Bullet')

# 3.2.4 RAG Pipeline Use Cases
doc.add_heading('3.2.4 RAG Pipeline Package', level=3)

doc.add_paragraph('UC-RAG-001: Generate Answer from Documents')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Core RAG process that generates answers from indexed documents.', style='List Bullet')
doc.add_paragraph('Preconditions: Documents are indexed, question is provided.', style='List Bullet')
doc.add_paragraph('Postconditions: Generated answer is returned.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. System creates embedding for user question', style='List Bullet')
doc.add_paragraph('2. System searches for similar document chunks', style='List Bullet')
doc.add_paragraph('3. System retrieves top 3 matching chunks', style='List Bullet')
doc.add_paragraph('4. System assembles context from chunks', style='List Bullet')
doc.add_paragraph('5. System sends question and context to Claude API', style='List Bullet')
doc.add_paragraph('6. Claude generates natural language answer', style='List Bullet')
doc.add_paragraph('7. System returns answer to caller', style='List Bullet')
doc.add_paragraph('Includes: Create Query Embedding, Search Similar Chunks, Assemble Context, Generate LLM Response', style='List Bullet')
doc.add_paragraph('Extends: Handle Generation Error (on failure)', style='List Bullet')

doc.add_paragraph('UC-RAG-002: Search Similar Chunks')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Performs vector similarity search on indexed document chunks.', style='List Bullet')
doc.add_paragraph('Preconditions: Query embedding is created, chunks are indexed.', style='List Bullet')
doc.add_paragraph('Postconditions: Top matching chunks are returned with similarity scores.', style='List Bullet')

doc.add_paragraph('UC-RAG-003: Create Query Embedding')
doc.add_paragraph('Actor: Embedding Model', style='List Bullet')
doc.add_paragraph('Description: Converts question text to 384-dimensional vector embedding.', style='List Bullet')
doc.add_paragraph('Preconditions: Question text is provided.', style='List Bullet')
doc.add_paragraph('Postconditions: Embedding vector is returned.', style='List Bullet')

doc.add_paragraph('UC-RAG-004: Generate LLM Response')
doc.add_paragraph('Actor: Claude API', style='List Bullet')
doc.add_paragraph('Description: Generates natural language answer using Claude Haiku.', style='List Bullet')
doc.add_paragraph('Preconditions: Question and context are provided.', style='List Bullet')
doc.add_paragraph('Postconditions: Generated answer is returned.', style='List Bullet')

# 3.2.5 Document Management Use Cases
doc.add_heading('3.2.5 Document Management Package', level=3)

doc.add_paragraph('UC-DOC-001: Upload PDF Document')
doc.add_paragraph('Actor: Administrator', style='List Bullet')
doc.add_paragraph('Description: Uploads a PDF file to the server for indexing.', style='List Bullet')
doc.add_paragraph('Preconditions: Admin is logged in, file is valid PDF.', style='List Bullet')
doc.add_paragraph('Postconditions: PDF is stored in books folder.', style='List Bullet')
doc.add_paragraph('Includes: Detect Duplicate Document', style='List Bullet')

doc.add_paragraph('UC-DOC-002: Index Document')
doc.add_paragraph('Actor: Administrator', style='List Bullet')
doc.add_paragraph('Description: Processes and indexes a PDF document for RAG search.', style='List Bullet')
doc.add_paragraph('Preconditions: PDF is uploaded, admin is logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: Document is indexed with embeddings stored.', style='List Bullet')
doc.add_paragraph('Main Flow:', style='List Bullet')
doc.add_paragraph('1. Admin triggers indexing', style='List Bullet')
doc.add_paragraph('2. System extracts text from PDF', style='List Bullet')
doc.add_paragraph('3. System splits text into chunks (500 chars, 50 overlap)', style='List Bullet')
doc.add_paragraph('4. System generates embedding for each chunk', style='List Bullet')
doc.add_paragraph('5. System stores chunks and embeddings in database', style='List Bullet')
doc.add_paragraph('6. System records document metadata', style='List Bullet')
doc.add_paragraph('Includes: Extract Text, Split Chunks, Generate Embeddings, Store Metadata', style='List Bullet')

doc.add_paragraph('UC-DOC-003: View Indexed Documents')
doc.add_paragraph('Actor: Administrator', style='List Bullet')
doc.add_paragraph('Description: Displays list of all indexed documents with metadata.', style='List Bullet')
doc.add_paragraph('Preconditions: Admin is logged in.', style='List Bullet')
doc.add_paragraph('Postconditions: Document list is displayed.', style='List Bullet')

doc.add_paragraph('UC-DOC-004: Delete Indexed Document')
doc.add_paragraph('Actor: Administrator', style='List Bullet')
doc.add_paragraph('Description: Removes a document and its chunks from the index.', style='List Bullet')
doc.add_paragraph('Preconditions: Admin is logged in, document exists.', style='List Bullet')
doc.add_paragraph('Postconditions: Document and all associated chunks are deleted.', style='List Bullet')

# 3.2.6 User Interface Use Cases
doc.add_heading('3.2.6 User Interface Package', level=3)

doc.add_paragraph('UC-UI-001: Open Modal Dialog')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Opens a modal dialog for user interaction with focus trapping.', style='List Bullet')

doc.add_paragraph('UC-UI-002: Close Modal Dialog')
doc.add_paragraph('Actor: User/System', style='List Bullet')
doc.add_paragraph('Description: Closes modal via X button, backdrop click, or Escape key.', style='List Bullet')

doc.add_paragraph('UC-UI-003: Display Toast Notification')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Shows temporary success or error notification that auto-dismisses.', style='List Bullet')

doc.add_paragraph('UC-UI-004: Show Loading Indicator')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Displays loading state and disables interactive elements during async operations.', style='List Bullet')

doc.add_paragraph('UC-UI-005: Display Error Message')
doc.add_paragraph('Actor: System', style='List Bullet')
doc.add_paragraph('Description: Shows error feedback via toast or inline message.', style='List Bullet')

# 3.3 Relationships Summary
doc.add_heading('3.3 Relationships Summary', level=2)

doc.add_paragraph('Include Relationships (required behavior):')
doc.add_paragraph('Register Account includes Validate Email Format, Check Email Availability', style='List Bullet')
doc.add_paragraph('Login includes Maintain Session', style='List Bullet')
doc.add_paragraph('Create Question includes Open Modal, Validate Question, Display Toast', style='List Bullet')
doc.add_paragraph('Edit Question includes Open Modal, Validate Question, Display Toast', style='List Bullet')
doc.add_paragraph('Delete Question includes Confirm Deletion, Display Toast', style='List Bullet')
doc.add_paragraph('Request AI Answer includes Generate Answer from Documents, Show Loading', style='List Bullet')
doc.add_paragraph('Generate Answer includes Query Embedding, Search Chunks, Assemble Context, LLM Response', style='List Bullet')
doc.add_paragraph('Index Document includes Extract Text, Split Chunks, Generate Embeddings, Store Metadata', style='List Bullet')
doc.add_paragraph('Upload PDF includes Detect Duplicate', style='List Bullet')

doc.add_paragraph('Extend Relationships (optional behavior):')
doc.add_paragraph('Handle Generation Error extends Generate Answer from Documents', style='List Bullet')
doc.add_paragraph('Display Error Message extends Request AI Answer', style='List Bullet')

doc.add_paragraph('Generalization Relationships (inheritance):')
doc.add_paragraph('Administrator inherits from User (has all user capabilities plus admin functions)', style='List Bullet')

# 3.4 PlantUML Diagram Code
doc.add_heading('3.4 PlantUML Diagram Code', level=2)
doc.add_paragraph(
    'The following PlantUML code can be used to generate a visual representation of the '
    'Use Case Diagram. This code can be rendered using PlantUML online editor, VS Code '
    'PlantUML extension, or any compatible tool.'
)

doc.add_paragraph('File location: diagrams/use_case_diagram.puml')

# Add Use Case Diagram Image
doc.add_picture('diagrams/use_case_diagram.png', width=Inches(6))

# Figure Description
fig_para = doc.add_paragraph()
fig_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
fig_run = fig_para.add_run('Figure 1: Use Case Diagram for Ask Holmes Application')
fig_run.italic = True

# ============================================
# 4. ACTIVITY DIAGRAM - QUESTIONS CRUD
# ============================================
doc.add_heading('4. Activity Diagram - Questions CRUD Operations', level=1)

doc.add_paragraph(
    'This chapter presents the activity diagrams for the basic CRUD (Create, Read, Update, Delete) '
    'operations on questions within the Ask Holmes application. These diagrams illustrate the flow '
    'of activities between the User and the System for each operation.'
)

# 4.1 Create Question
doc.add_heading('4.1 Create Question', level=2)

doc.add_paragraph('Actors: User, System')
doc.add_paragraph('Precondition: User is authenticated and on the Questions page')
doc.add_paragraph('Postcondition: New question is created and displayed in the list')

doc.add_paragraph('Flow of Activities:')
doc.add_paragraph('1. User clicks "New Question" button', style='List Number')
doc.add_paragraph('2. System opens Create Question Modal with empty form', style='List Number')
doc.add_paragraph('3. User enters question title', style='List Number')
doc.add_paragraph('4. User enters question content', style='List Number')
doc.add_paragraph('5. User clicks "Save" button', style='List Number')
doc.add_paragraph('6. System validates input', style='List Number')
doc.add_paragraph('7. If valid: System sends POST request to /api/questions', style='List Number')
doc.add_paragraph('8. System creates question in database with timestamp', style='List Number')
doc.add_paragraph('9. System closes modal and displays success toast', style='List Number')
doc.add_paragraph('10. System refreshes questions list', style='List Number')

doc.add_paragraph('Alternative Flow (Invalid Input):')
doc.add_paragraph('6a. System displays validation error message', style='List Bullet')
doc.add_paragraph('6b. System highlights invalid fields', style='List Bullet')
doc.add_paragraph('6c. User corrects input errors and returns to step 5', style='List Bullet')

# 4.2 Read Questions (View List)
doc.add_heading('4.2 Read Questions (View List)', level=2)

doc.add_paragraph('Actors: User, System')
doc.add_paragraph('Precondition: User is authenticated')
doc.add_paragraph('Postcondition: Questions list is displayed')

doc.add_paragraph('Flow of Activities:')
doc.add_paragraph('1. User navigates to Questions page', style='List Number')
doc.add_paragraph('2. System sends GET request to /api/questions', style='List Number')
doc.add_paragraph('3. System fetches user questions from database', style='List Number')
doc.add_paragraph('4. If questions exist: System renders questions list with cards', style='List Number')
doc.add_paragraph('5. Each card displays title, preview, and date', style='List Number')

doc.add_paragraph('Alternative Flow (No Questions):')
doc.add_paragraph('4a. System displays empty state message', style='List Bullet')
doc.add_paragraph('4b. System shows "Create your first question" prompt', style='List Bullet')

# 4.3 Read Question (View Details)
doc.add_heading('4.3 Read Question (View Details)', level=2)

doc.add_paragraph('Actors: User, System')
doc.add_paragraph('Precondition: User is on Questions list page')
doc.add_paragraph('Postcondition: Question details are displayed with answer section')

doc.add_paragraph('Flow of Activities:')
doc.add_paragraph('1. User clicks on question card', style='List Number')
doc.add_paragraph('2. System sends GET request to /api/questions/{id}', style='List Number')
doc.add_paragraph('3. System fetches question details and associated answer', style='List Number')
doc.add_paragraph('4. System navigates to Question Details page', style='List Number')
doc.add_paragraph('5. System displays question title and content', style='List Number')
doc.add_paragraph('6. If answer exists: System displays answer with Edit/Clear buttons', style='List Number')

doc.add_paragraph('Alternative Flow (No Answer):')
doc.add_paragraph('6a. System displays empty answer section', style='List Bullet')
doc.add_paragraph('6b. System shows "Enter Answer" and "Ask Holmes" buttons', style='List Bullet')

# 4.4 Update Question
doc.add_heading('4.4 Update Question', level=2)

doc.add_paragraph('Actors: User, System')
doc.add_paragraph('Precondition: User is viewing a question they own')
doc.add_paragraph('Postcondition: Question is updated with new content')

doc.add_paragraph('Flow of Activities:')
doc.add_paragraph('1. User clicks "Edit" button on question', style='List Number')
doc.add_paragraph('2. System opens Edit Question Modal', style='List Number')
doc.add_paragraph('3. System populates form with existing question data', style='List Number')
doc.add_paragraph('4. User modifies question title and/or content', style='List Number')
doc.add_paragraph('5. User clicks "Save Changes" button', style='List Number')
doc.add_paragraph('6. System validates input', style='List Number')
doc.add_paragraph('7. If valid: System sends PUT request to /api/questions/{id}', style='List Number')
doc.add_paragraph('8. System updates question and modified timestamp', style='List Number')
doc.add_paragraph('9. System closes modal and displays success toast', style='List Number')
doc.add_paragraph('10. System refreshes question display', style='List Number')

doc.add_paragraph('Alternative Flow (Invalid Input):')
doc.add_paragraph('6a. System displays validation error message', style='List Bullet')
doc.add_paragraph('6b. System highlights invalid fields', style='List Bullet')
doc.add_paragraph('6c. User corrects input errors and returns to step 5', style='List Bullet')

# 4.5 Delete Question
doc.add_heading('4.5 Delete Question', level=2)

doc.add_paragraph('Actors: User, System')
doc.add_paragraph('Precondition: User is viewing a question they own')
doc.add_paragraph('Postcondition: Question and associated answer are deleted')

doc.add_paragraph('Flow of Activities:')
doc.add_paragraph('1. User clicks "Delete" button on question', style='List Number')
doc.add_paragraph('2. System opens confirmation dialog', style='List Number')
doc.add_paragraph('3. System displays "Are you sure?" message', style='List Number')
doc.add_paragraph('4. User clicks "Confirm Delete" button', style='List Number')
doc.add_paragraph('5. System sends DELETE request to /api/questions/{id}', style='List Number')
doc.add_paragraph('6. System deletes question and associated answer from database', style='List Number')
doc.add_paragraph('7. System closes dialog and displays success toast', style='List Number')
doc.add_paragraph('8. System removes question from list', style='List Number')
doc.add_paragraph('9. System navigates to Questions list page', style='List Number')

doc.add_paragraph('Alternative Flow (Cancel Deletion):')
doc.add_paragraph('4a. User clicks "Cancel" button', style='List Bullet')
doc.add_paragraph('4b. System closes confirmation dialog', style='List Bullet')
doc.add_paragraph('4c. System returns to previous state', style='List Bullet')

# 4.6 PlantUML Diagram Code
doc.add_heading('4.6 PlantUML Diagram Code', level=2)
doc.add_paragraph(
    'The following PlantUML code can be used to generate a visual representation of the '
    'Activity Diagram. This code can be rendered using PlantUML online editor, VS Code '
    'PlantUML extension, or any compatible tool.'
)

doc.add_paragraph('File location: diagrams/activity_diagram_questions_crud.puml')

# Add Activity Diagram Image
doc.add_picture('diagrams/activity_diagram.png', width=Inches(6))

# Figure Description
fig_para2 = doc.add_paragraph()
fig_para2.alignment = WD_ALIGN_PARAGRAPH.CENTER
fig_run2 = fig_para2.add_run('Figure 2: Activity Diagram for Questions CRUD Operations')
fig_run2.italic = True

# ============================================
# 5. SEQUENCE DIAGRAM - QUESTIONS CRUD
# ============================================
doc.add_heading('5. Sequence Diagram - Questions CRUD Operations', level=1)

doc.add_paragraph(
    'This chapter presents the sequence diagrams for the basic CRUD (Create, Read, Update, Delete) '
    'operations on questions within the Ask Holmes application. These diagrams illustrate the '
    'interactions between the User, React Frontend, Flask API Backend, and PostgreSQL Database '
    'over time for each operation.'
)

# 5.1 Participants
doc.add_heading('5.1 Participants', level=2)

doc.add_paragraph('User: The actor initiating all operations', style='List Bullet')
doc.add_paragraph('React Frontend: The client-side user interface handling user interactions and state management', style='List Bullet')
doc.add_paragraph('Flask API: The backend server processing requests and business logic', style='List Bullet')
doc.add_paragraph('PostgreSQL: The database storing questions and answers data', style='List Bullet')

# 5.2 Create Question Sequence
doc.add_heading('5.2 Create Question Sequence', level=2)

doc.add_paragraph('1. User clicks New Question button', style='List Number')
doc.add_paragraph('2. Frontend opens CreateQuestionModal and displays empty form', style='List Number')
doc.add_paragraph('3. User enters title and content, clicks Save', style='List Number')
doc.add_paragraph('4. Frontend validates input', style='List Number')
doc.add_paragraph('5. Frontend sends POST /api/questions to Backend', style='List Number')
doc.add_paragraph('6. Backend validates request and gets current user from session', style='List Number')
doc.add_paragraph('7. Backend inserts question into Database', style='List Number')
doc.add_paragraph('8. Database returns new question ID', style='List Number')
doc.add_paragraph('9. Backend returns 201 Created to Frontend', style='List Number')
doc.add_paragraph('10. Frontend closes modal, updates state, displays success toast', style='List Number')

# 5.3 Read Questions Sequence
doc.add_heading('5.3 Read Questions (List) Sequence', level=2)

doc.add_paragraph('1. User navigates to Questions page', style='List Number')
doc.add_paragraph('2. Frontend sends GET /api/questions to Backend', style='List Number')
doc.add_paragraph('3. Backend gets current user from session', style='List Number')
doc.add_paragraph('4. Backend queries Database for user questions', style='List Number')
doc.add_paragraph('5. Database returns questions array', style='List Number')
doc.add_paragraph('6. Backend returns 200 OK with questions list', style='List Number')
doc.add_paragraph('7. Frontend renders questions list or empty state', style='List Number')

# 5.4 Read Question Details Sequence
doc.add_heading('5.4 Read Question (Details) Sequence', level=2)

doc.add_paragraph('1. User clicks on question card', style='List Number')
doc.add_paragraph('2. Frontend sends GET /api/questions/id to Backend', style='List Number')
doc.add_paragraph('3. Backend gets current user and queries question from Database', style='List Number')
doc.add_paragraph('4. Backend queries associated answer from Database', style='List Number')
doc.add_paragraph('5. Backend returns 200 OK with question and answer data', style='List Number')
doc.add_paragraph('6. Frontend navigates to details page and displays content', style='List Number')

# 5.5 Update Question Sequence
doc.add_heading('5.5 Update Question Sequence', level=2)

doc.add_paragraph('1. User clicks Edit button', style='List Number')
doc.add_paragraph('2. Frontend opens EditQuestionModal with existing data', style='List Number')
doc.add_paragraph('3. User modifies title/content and clicks Save Changes', style='List Number')
doc.add_paragraph('4. Frontend validates input', style='List Number')
doc.add_paragraph('5. Frontend sends PUT /api/questions/id to Backend', style='List Number')
doc.add_paragraph('6. Backend validates and verifies ownership in Database', style='List Number')
doc.add_paragraph('7. Backend updates question in Database', style='List Number')
doc.add_paragraph('8. Backend returns 200 OK with updated question', style='List Number')
doc.add_paragraph('9. Frontend closes modal, updates state, displays success toast', style='List Number')

# 5.6 Delete Question Sequence
doc.add_heading('5.6 Delete Question Sequence', level=2)

doc.add_paragraph('1. User clicks Delete button', style='List Number')
doc.add_paragraph('2. Frontend opens confirmation dialog', style='List Number')
doc.add_paragraph('3. User clicks Confirm Delete', style='List Number')
doc.add_paragraph('4. Frontend sends DELETE /api/questions/id to Backend', style='List Number')
doc.add_paragraph('5. Backend verifies ownership in Database', style='List Number')
doc.add_paragraph('6. Backend deletes associated answer from Database', style='List Number')
doc.add_paragraph('7. Backend deletes question from Database', style='List Number')
doc.add_paragraph('8. Backend returns 200 OK', style='List Number')
doc.add_paragraph('9. Frontend closes dialog, removes from state, displays success toast', style='List Number')
doc.add_paragraph('10. Frontend navigates to questions list', style='List Number')

# 5.7 Diagram
doc.add_heading('5.7 Sequence Diagram', level=2)

doc.add_paragraph('File location: diagrams/sequence_diagram_questions_crud.puml')

# Add Sequence Diagram Image
doc.add_picture('diagrams/sequence_diagram.png', width=Inches(4.2))

# Figure Description
fig_para3 = doc.add_paragraph()
fig_para3.alignment = WD_ALIGN_PARAGRAPH.CENTER
fig_run3 = fig_para3.add_run('Figure 3: Sequence Diagram for Questions CRUD Operations')
fig_run3.italic = True

# Save the document
doc.save('SRS_Ask_Holmes.docx')

print("SRS document created successfully: SRS_Ask_Holmes.docx")
