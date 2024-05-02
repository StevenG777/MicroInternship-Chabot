Intents = [
        {
            "intent": "greetings with name",
            "patterns": [
                "(hi there|hi|hola|hello there|hello|hya there|hya|good morning|good afternoon|good evening|hey), I am (\w*)\W?",
                "(hi there|hi|hola|hello there|hello|hya there|hya|good morning|good afternoon|good evening|hey), my name is (\w*)\W?"
            ],
            "responses": [
                "Hello %2! thanks for checking in", 
                "Hello %2! How can I assist you today?",
                "Hi %2! How can I help you?",
                "Hi there! How can I help you?",
                "Hey %2! What can I do for you?"
            ]
        },
        {
            "intent": "greeting",
            "patterns": ["(hi there|hi|hola|hello there|hello|hya there|hya|good morning|good afternoon|good evening|hey)\W?"],
            "responses": [
                "Hello! thanks for checking in", 
                "Hello! How can I assist you today?",
                "Hi there! How can I help you?",
                "Hey! What can I do for you?"
            ]
        },
        {
            "intent": "goodbye",
            "patterns": ["(bye|good bye|see you later|farewell|take care)\W?"],
            "responses": [
                "Have a nice time, welcome back again", 
                "Bye bye",
                "Goodbye! Feel free to ask for course recommendations anytime.",
                "See you later! If you need more help, just let me know.",
                "Farewell! Don't hesitate to return if you have more questions."
            ]
        },
        {
            "intent": "thanks",
            "patterns": [
                "(thanks|thanks a lot|thanks for your help|thanks for helping me|awesome, thanks)\W?",
                "(thank you so much|thank you|thankyou|ty|tysm)\W?",
                "(okay|that's helpful|wow|great)\W?"
            ],
            "responses": [
                "Happy to help!", 
                "Any time!",
                "You're welcome",
                "You're welcome. If you have any more questions, feel free to ask!", 
                "My pleasure",
                "Anytime!",
                "Glad I could assist you!",
                "No problem, happy to help!"
            ]
        },
        {
            "intent": "identity",
            "patterns": [
                "(what's your name|who are you|what are you|tell me about yourself|can you introduce yourself)\W?"],
            "responses": [
                "I'm the UC Merced Computer Science Course Recommendation Chatbot. My purpose is to help you find suitable courses for your academic journey.",
                "I'm your friendly UC Merced Computer Science Course Recommendation Chatbot. Feel free to ask me anything related to courses!",
                "I'm the UC Merced Computer Science Course Recommendation Chatbot. You can ask me about computer science courses available at UC Merced."
            ]
        },
        {
            "intent": "data science recommendation",
            "patterns": [
                "I (aspire|want|want to pursue) to (be a|become a|work as a) (data scientist|data analyst|data engineer|machine learning researcher|machine learning scientist|machine learning engineer|ML engineer|AI engineer)\W?",
                "I (aspire|want|want to pursue) (work with|be working in|work in) (data science|machine learning|AI|artificial intelligence|data engineering|data related) in (the)? (industry|field)\W?",
                "I (aspire|want) to learn (about)? (data science|data analysis|data engineering|machine learning|ML|AI|artificial intelligence)\W?",
                "I (aspire|want) to (take|register|be recommended to take) (data science|data analysis|data engineering|machine learning|ML|AI|artificial intelligence) courses\W?",
                "I (aspire|want) to (improve|enhance|learn|advance|boost|hone|increase|gain|develop) (my)? (data science|data analytics|data engineering|AI|ML|artificial intelligence|machine learning|data) skills"
            ],
            "responses": [
                """
To equip you with the necessary skills and knowledge, I highly recommend considering the following courses:

- CSE 100: Algorithm Design and Analysis:
    Understanding algorithms and their efficiency is fundamental in data science. This course will provide you with essential tools such as algorithm complexity analysis, divide and conquer, dynamic programming, and greedy algorithms, which are crucial for solving complex data-related problems efficiently.
                
- CSE 111: Database Systems:
    Data is at the heart of data science, and having a strong grasp of database systems is imperative. This course will teach you the principles of database design and operation, SQL database language, query optimization, and transaction processing—skills essential for working with large datasets.
                
- CSE 175: Introduction to Artificial Intelligence:
    Data science often involves building intelligent systems to analyze and interpret data. This course provides a comprehensive overview of AI concepts and methods, including machine learning, knowledge representation, reasoning, and planning, preparing you to create intelligent solutions for real-world problems.
                
- CSE 176: Introduction to Machine Learning: 
    Machine learning lies at the core of data science, enabling computers to learn from data and make predictions or decisions. This course covers a wide range of machine learning techniques, including supervised learning, unsupervised learning, and reinforcement learning, equipping you with essential skills for building predictive models and extracting insights from data.
                
- CSE 177: Database Systems Implementation: 
    Understanding the internals of database management systems is crucial for optimizing data retrieval and manipulation—a key aspect of data science. This course will provide you with hands-on experience in building a database execution engine, enhancing your understanding of database systems' inner workings.
                
- CSE 185: Introduction to Computer Vision: 
    As data scientists, you'll often work with visual data, making knowledge of computer vision techniques highly valuable. This course introduces fundamental image processing and pattern recognition techniques, empowering you to extract meaningful information from images and videos.
                """
            ]
        },
        {
            "intent": "software engineering recommendation",
            "patterns": [
                "I (aspire|want|want to pursue) to (be a|become a|work as a) (software engineer|software developer|mobile app developer)\W?",
                "I (aspire|want|want to pursue) (work with|be working in|work in) (software engineering|software development|mobile development) in (the)? (industry|field)\W?",
                "I (aspire|want) to learn (about)? (software development|mobile app development|software engineer)\W?",
                "I (aspire|want) to (take|register|be recommended to take) (software engineering|software development|mobile development) courses\W?",
                "I (aspire|want) to (improve|enhance|learn|advance|boost|hone|increase|gain|develop) (my)? (software engineering|software development|mobile development) skills"
            ],
            "responses": [
                """
To equip you with the necessary skills and knowledge, I highly recommend considering the following courses:
                
- CSE 030: Data Structures:
    This course focuses on the fundamental building blocks of computer science, covering data structures such as linked lists, stacks, queues, trees, hash tables, and graphs, along with algorithms for searching and sorting.

- CSE 100: Algorithm Design and Analysis:
    Students learn about designing and analyzing computer algorithms, including concepts like algorithm complexity, divide and conquer, dynamic programming, and greedy algorithms. Major algorithms and data structures for searching, sorting, and graph problems are also covered.

- CSE 108: Full Stack Web Development
    Explores topics related to both front end and backend web development including web security, scalable architecture, web frameworks, databases, and object relational mappers

- CSE 111: Database Systems:
    This course covers principles of database design and operation, including relational data models, SQL, active databases, query optimization, transaction processing, user-defined functions, and data warehousing.

 - CSE 120: Software Engineering:
    Students work on projects to learn modern software engineering techniques, focusing on design methodology, project management, and creating reliable, efficient, reusable, and maintainable software systems.

- CSE 150: Operating Systems:
    Concepts of computer operating systems are covered, including concurrency, memory management, file systems, multitasking, performance analysis, and security.

- CSE 162: Mobile Computing:
    Introduces basic concepts of mobile cloud computing, including different types of mobile devices, communication technologies, context-aware computing, and programming on mobile devices.

- CSE 165: Introduction to Object-Oriented Programming:
    This course covers essential object-oriented programming concepts such as classes, objects, methods, interfaces, inheritance, encapsulation, and polymorphism.

- CSE 168: Distributed Software Systems: 
    Students learn about the foundations and practical designs of distributed software systems, covering concepts like consistency, availability, scalability, programming models for distributed computing, distributed storage systems, and the convergence of HPC, Big Data, AI, and Cloud Computing with modern distributed systems.
                """
            ]
        },
        {
            "intent": "other",
            "patterns": [".*"],
            "responses": ["Sorry, I didn't understand you", "Please give me more info", "Not sure I understand that"]
        }
    ]