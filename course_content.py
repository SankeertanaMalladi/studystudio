"""Built-in course catalog and original learning content."""
RAW = {
    "python": {
        "title": "Python Programming", "category": "Programming", "icon": "Py", "level": "Beginner to intermediate", "weeks": 6,
        "description": "Build practical Python skills, from clear syntax and control flow to reusable functions and data structures.",
        "resources": [
            ("The Python Tutorial", "Documentation", "Official guide to Python syntax and core concepts.", "https://docs.python.org/3/tutorial/"),
            ("Python for beginners", "Learning path", "Official starting points and learning resources.", "https://www.python.org/about/gettingstarted/"),
            ("Python video lessons", "Video", "Browse lessons on Python fundamentals and beginner projects.", "https://www.youtube.com/results?search_query=python+programming+beginner+course"),
        ],
        "cards": [
            ("What is a Python list?", "An ordered, mutable collection that can hold values of different types."),
            ("What does return do?", "It sends a result back from a function to its caller."),
            ("When should you use a dictionary?", "When values should be retrieved using unique keys."),
            ("What is an exception?", "An event that interrupts normal program flow and can be handled."),
        ],
        "questions": [
            ("Types", "Which type stores an ordered, changeable sequence?", "list", "tuple", "set", "bool", "Lists preserve order and can be changed after creation."),
            ("Control flow", "What values does range(4) produce?", "0, 1, 2, 3", "1, 2, 3, 4", "0, 1, 2, 3, 4", "Only 4", "The stop value is excluded and the default start is zero."),
            ("Functions", "Which keyword sends a value back from a function?", "return", "yield", "break", "pass", "return ends the function call and provides its result."),
            ("Dictionaries", "How do you retrieve the value for key name in user?", "user['name']", "user.name", "user(name)", "user->name", "Square-bracket key lookup retrieves a dictionary value."),
        ],
    },
    "javascript": {
        "title": "JavaScript Essentials", "category": "Programming", "icon": "JS", "level": "Beginner to intermediate", "weeks": 5,
        "description": "Learn the language of the web: values, functions, arrays, asynchronous code, and browser interaction.",
        "resources": [
            ("MDN JavaScript Guide", "Documentation", "Language features and practical JavaScript concepts.", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"),
            ("MDN JavaScript learning", "Learning path", "Structured lessons and challenges for new developers.", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting"),
            ("JavaScript video lessons", "Video", "Browse modern JavaScript courses and examples.", "https://www.youtube.com/results?search_query=javascript+fundamentals+beginner+course"),
        ],
        "cards": [
            ("What is the DOM?", "A programming representation of a web page that scripts can inspect and change."),
            ("What does const prevent?", "Reassignment of the variable binding."),
            ("What does array map() return?", "A new array containing the result of a function applied to each item."),
            ("What is a Promise?", "An object representing the eventual result or failure of asynchronous work."),
        ],
        "questions": [
            ("Variables", "Which declaration prevents reassignment of its binding?", "const", "let", "var", "static", "const bindings cannot be reassigned."),
            ("Equality", "What does === compare?", "Value and type", "Only value after coercion", "Only object identity", "Whether a variable exists", "Strict equality compares without type coercion."),
            ("Arrays", "What does array.map() return?", "A new transformed array", "The first matching item", "The original array sorted", "A boolean", "map creates a new array from callback return values."),
            ("Async", "What does await do inside an async function?", "Waits for a promise to settle and returns its value", "Creates a new thread", "Stops all browser code", "Repeats the function", "await pauses that async function until the promise settles."),
        ],
    },
    "web-development": {
        "title": "Web Development", "category": "Design & web", "icon": "Web", "level": "Beginner", "weeks": 7,
        "description": "Create accessible, responsive websites using semantic HTML, modern CSS, and interactive JavaScript.",
        "resources": [
            ("MDN Learn Web Development", "Learning path", "A structured curriculum for web development foundations.", "https://developer.mozilla.org/en-US/docs/Learn_web_development"),
            ("MDN Core modules", "Documentation", "Learn HTML, CSS, accessibility, and browser scripting.", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core"),
            ("Build a website: video lessons", "Video", "Browse guided HTML, CSS, and frontend project lessons.", "https://www.youtube.com/results?search_query=build+a+website+HTML+CSS+beginner+course"),
        ],
        "cards": [
            ("What is semantic HTML?", "Markup that describes the meaning and role of page content."),
            ("What is CSS Grid for?", "Building two-dimensional layouts with rows and columns."),
            ("What is responsive design?", "Layouts that adapt to screen size and user context."),
            ("Why write image alt text?", "To convey an image's purpose to people who cannot see it."),
        ],
        "questions": [
            ("HTML", "Which element marks the primary unique content of a page?", "<main>", "<div>", "<aside>", "<footer>", "main identifies the dominant content of the document."),
            ("Accessibility", "What should useful alt text communicate?", "The image's purpose or meaningful content", "The image file path", "Every pixel's color", "Its CSS dimensions", "Alt text should provide equivalent information in context."),
            ("CSS layout", "Which CSS tool is designed for two-dimensional layouts?", "CSS Grid", "Float", "Text transform", "Outline", "Grid controls rows and columns."),
            ("Responsive design", "What can a CSS media query respond to?", "Viewport and device conditions", "A server database", "A form password", "An HTML title", "Media queries apply styles under conditions such as viewport width."),
        ],
    },
    "java": {
        "title": "Java Foundations", "category": "Programming", "icon": "Ja", "level": "Beginner to intermediate", "weeks": 6,
        "description": "Learn Java language basics, object-oriented design, collections, and the Java runtime.",
        "resources": [
            ("Dev.java learning paths", "Learning path", "Official tutorials for Java language basics, collections, and the JVM.", "https://dev.java/learn/"),
            ("Java documentation", "Documentation", "Official Java platform and API documentation.", "https://docs.oracle.com/en/java/"),
            ("Java video lessons", "Video", "Browse Java fundamentals and beginner project tutorials.", "https://www.youtube.com/results?search_query=java+programming+beginner+course"),
        ],
        "cards": [
            ("What is the JVM?", "The Java Virtual Machine executes Java bytecode in a runtime environment."),
            ("What is encapsulation?", "Keeping state with its behavior while controlling access."),
            ("What does static mean on a method?", "The method belongs to its class rather than an object instance."),
            ("What is a Java List?", "An ordered collection that allows indexed access and duplicates."),
        ],
        "questions": [
            ("Runtime", "What executes Java bytecode?", "The Java Virtual Machine", "The editor", "The package manager", "The source compiler alone", "The JVM loads and executes compiled bytecode."),
            ("Types", "Which Java type stores true or false?", "boolean", "int", "char", "String", "boolean is Java's primitive logical type."),
            ("OOP", "What is a key idea behind encapsulation?", "Control access to state through a defined interface", "Sort every collection", "Run code only at compile time", "Convert Java to HTML", "Encapsulation protects internal state behind a public interface."),
            ("Collections", "Which collection is ordered and allows duplicates?", "List", "Set", "Map key set", "Optional", "List preserves order and may contain repeated values."),
        ],
    },
    "sql": {
        "title": "SQL & Databases", "category": "Data", "icon": "SQL", "level": "Beginner", "weeks": 4,
        "description": "Query relational data, combine tables, summarize results, and understand database design.",
        "resources": [
            ("SQLBolt interactive lessons", "Practice", "Short interactive lessons and SQL exercises.", "https://sqlbolt.com/"),
            ("PostgreSQL tutorial", "Documentation", "A practical introduction to relational databases and SQL.", "https://www.postgresql.org/docs/current/tutorial.html"),
            ("SQL video lessons", "Video", "Browse lessons on SELECT, filtering, joins, and aggregation.", "https://www.youtube.com/results?search_query=SQL+beginner+course+SELECT+JOIN"),
        ],
        "cards": [
            ("What does SELECT do?", "Chooses columns or expressions to return from a query."),
            ("What is a primary key?", "A column or group of columns that uniquely identifies a row."),
            ("What does INNER JOIN return?", "Rows whose join values match in both inputs."),
            ("What is GROUP BY for?", "Grouping rows so aggregates can calculate a result per group."),
        ],
        "questions": [
            ("Filtering", "Which clause filters rows before grouping?", "WHERE", "HAVING", "ORDER BY", "LIMIT", "WHERE filters source rows before aggregation."),
            ("Keys", "What is the purpose of a primary key?", "Uniquely identify each row", "Sort rows alphabetically", "Store only text", "Connect to a server", "A primary key uniquely identifies a row."),
            ("Joins", "What does INNER JOIN return?", "Rows matching in both joined inputs", "Every row from the left input", "Only NULL rows", "A random row", "INNER JOIN keeps rows whose join condition matches."),
            ("Aggregation", "Which clause groups rows for aggregate calculations?", "GROUP BY", "WHERE", "VALUES", "UPDATE", "GROUP BY forms groups for functions such as COUNT and AVG."),
        ],
    },
    "data-science": {
        "title": "Data Science", "category": "Data", "icon": "DS", "level": "Beginner", "weeks": 7,
        "description": "Turn data into evidence-based insights with cleaning, exploration, visualization, and clear communication.",
        "resources": [
            ("pandas getting started", "Documentation", "Official tutorials for tabular data, plotting, and summaries.", "https://pandas.pydata.org/docs/getting_started/"),
            ("Kaggle data visualization", "Practice", "Guided exercises for exploring data and communicating patterns.", "https://www.kaggle.com/learn/data-visualization"),
            ("Data analysis video lessons", "Video", "Browse project-based lessons using pandas and visualization.", "https://www.youtube.com/results?search_query=data+analysis+with+python+pandas+beginner"),
        ],
        "cards": [
            ("What is exploratory data analysis?", "Using summaries and visuals to understand quality, patterns, and relationships."),
            ("What is a median?", "The middle value of ordered observations."),
            ("What makes a chart useful?", "It makes a comparison easy to see and labels units and context."),
            ("What is data leakage?", "Information unavailable at prediction time enters training or evaluation."),
        ],
        "questions": [
            ("Exploration", "What is a useful goal of exploratory data analysis?", "Understand distributions, data quality, and patterns", "Prove a preferred conclusion", "Replace all data collection", "Guarantee a causal effect", "EDA helps reveal structure and issues before modeling."),
            ("Statistics", "What is the median of an ordered set?", "Its middle value", "Always its most frequent value", "Its largest value", "Its total divided by two", "The median is the central observation or midpoint of two central values."),
            ("Visualization", "What helps readers interpret a chart correctly?", "Clear labels and context", "A 3D effect by default", "No units", "Every variable at once", "Labels and context make the visual easier to interpret."),
            ("Modeling", "What is data leakage?", "Using information unavailable at prediction time", "Removing duplicate rows", "Normalizing a feature", "Saving a chart", "Leakage can make evaluation unrealistically optimistic."),
        ],
    },
    "machine-learning": {
        "title": "Machine Learning", "category": "AI", "icon": "ML", "level": "Beginner to intermediate", "weeks": 8,
        "description": "Understand supervised learning, model evaluation, feature preparation, and reliable experiments.",
        "resources": [
            ("Google Machine Learning Crash Course", "Learning path", "Practical modules, visualizations, and exercises for core ML concepts.", "https://developers.google.com/machine-learning/crash-course"),
            ("scikit-learn user guide", "Documentation", "Guidance for preprocessing, model selection, and evaluation.", "https://scikit-learn.org/stable/user_guide.html"),
            ("Machine learning video lessons", "Video", "Browse visual introductions to supervised learning and evaluation.", "https://www.youtube.com/results?search_query=machine+learning+basics+beginner+course"),
        ],
        "cards": [
            ("What is supervised learning?", "Learning from input examples paired with known target labels or values."),
            ("Why split training and test data?", "To estimate how a model performs on data it did not train on."),
            ("What is overfitting?", "Learning training-specific detail that performs poorly on new examples."),
            ("What does precision measure?", "Among predicted positives, the fraction that are truly positive."),
        ],
        "questions": [
            ("Learning types", "What does supervised learning use during training?", "Examples paired with target values", "Only unlabeled images", "No training data", "A list of passwords", "Supervised learning uses known targets for training examples."),
            ("Evaluation", "Why hold out test data?", "Estimate performance on unseen examples", "Increase training data after each epoch", "Select labels manually", "Remove all model errors", "A held-out set provides an independent performance estimate."),
            ("Generalization", "What is overfitting?", "Learning training detail that does not generalize", "Having too few features by definition", "A missing target column", "A calibrated model", "Overfit models perform worse on new data than training data suggests."),
            ("Metrics", "Precision is the fraction of predicted positives that are:", "Actually positive", "Actually negative", "Missing from the test set", "Sorted by time", "Precision equals true positives divided by predicted positives."),
        ],
    },
    "dsa": {
        "title": "Data Structures & Algorithms", "category": "Computer science", "icon": "DSA", "level": "Beginner to intermediate", "weeks": 8,
        "description": "Choose useful data structures, reason about runtime, and practice algorithmic problem-solving.",
        "resources": [
            ("VisuAlgo", "Interactive", "Visual animations for common data structures and algorithms.", "https://visualgo.net/en"),
            ("MIT Introduction to Algorithms", "Course", "Lecture materials and assignments on algorithmic problem-solving.", "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/"),
            ("Algorithms video lessons", "Video", "Browse visual explanations and worked coding problems.", "https://www.youtube.com/results?search_query=data+structures+algorithms+beginner+course"),
        ],
        "cards": [
            ("What does Big O describe?", "How resource use grows with input size, ignoring constant factors."),
            ("What is a stack?", "A last-in, first-out collection with push and pop operations."),
            ("When can binary search be used?", "When the search space is ordered and can safely be halved."),
            ("What is a hash table useful for?", "Fast average-case lookup by key."),
        ],
        "questions": [
            ("Complexity", "What does Big O notation describe?", "How resource use grows with input size", "Exact running time in seconds", "Number of code comments", "Number of files", "Big O expresses asymptotic growth."),
            ("Stacks", "Which principle describes a stack?", "Last in, first out", "First in, first out", "Random access only", "Smallest value first", "The most recently pushed item is removed first."),
            ("Searching", "What condition does binary search require?", "The elements are ordered", "Every value is unique", "The length is prime", "All values are positive", "Ordering lets binary search discard half the range."),
            ("Hashing", "What is a hash table commonly used for?", "Associating keys with values for fast average lookup", "Always sorting items", "Compressing images", "Depth-first graph traversal", "Hash tables use key-derived locations for efficient lookup."),
        ],
    },
}


def _build_course(course_id, raw):
    title, category, icon, level, weeks, description, resources, cards, questions = (
        raw["title"], raw["category"], raw["icon"], raw["level"], raw["weeks"],
        raw["description"], raw["resources"], raw["cards"], raw["questions"]
    )
    built_questions = []
    for topic, prompt, answer, wrong_a, wrong_b, wrong_c, explanation in questions:
        options = [answer, wrong_a, wrong_b, wrong_c]
        shift = len(prompt) % 4
        options = options[shift:] + options[:shift]
        built_questions.append({
            "topic": topic, "question": prompt, "choices": options,
            "answer": options.index(answer), "explanation": explanation,
        })
    return {
        "id": course_id, "title": title, "category": category, "icon": icon,
        "level": level, "weeks": weeks, "description": description,
        "resources": [
            {"title": name, "kind": kind, "description": desc, "url": url}
            for name, kind, desc, url in resources
        ],
        "cards": [{"front": front, "back": back} for front, back in cards],
        "questions": built_questions,
    }


COURSES = {course_id: _build_course(course_id, raw) for course_id, raw in RAW.items()}


def get_courses():
    return COURSES


def get_course(course_id):
    return COURSES.get(course_id)

def _append_question(course_id, topic, prompt, answer, wrong_a, wrong_b, wrong_c, explanation):
    choices = [answer, wrong_a, wrong_b, wrong_c]
    shift = len(prompt) % 4
    choices = choices[shift:] + choices[:shift]
    COURSES[course_id]["questions"].append({
        "topic": topic, "question": prompt, "choices": choices,
        "answer": choices.index(answer), "explanation": explanation,
    })


_append_question("python", "Files", "Which keyword ensures a file is closed after a with block?", "with", "close", "finally", "open", "The with statement manages the file context and closes it when the block ends.")
_append_question("python", "Exceptions", "Which block runs whether or not an exception occurred?", "finally", "except", "raise", "assert", "A finally block is used for cleanup that should always run.")
_append_question("javascript", "DOM", "Which method selects the first element matching a CSS selector?", "querySelector()", "getElementByName()", "selectCSS()", "findNode()", "querySelector returns the first matching element.")
_append_question("javascript", "Functions", "Which syntax is a valid arrow function?", "(x) => x * 2", "function => (x * 2)", "def (x): x * 2", "fn(x) { x * 2 }", "The arrow separates parameters from the function body.")
_append_question("web-development", "Forms", "Which attribute links a label to an input?", "for", "href", "target", "action", "The label for attribute should match the input id.")
_append_question("web-development", "Box model", "Which order goes from the inside of a CSS box outward?", "Content, padding, border, margin", "Margin, content, border, padding", "Border, margin, content, padding", "Content, border, margin, padding", "The content is surrounded by padding, border, then margin.")
_append_question("java", "Methods", "What does static mean on a Java method?", "It belongs to the class", "It can never return a value", "It is private automatically", "It runs only during compilation", "A static member is associated with the class itself.")
_append_question("java", "Exceptions", "Which keyword handles an exception after a try block?", "catch", "throws", "throwable", "final", "A catch block handles matching exceptions.")
_append_question("sql", "NULL", "How should SQL test whether a value is NULL?", "IS NULL", "= NULL", "== NULL", "IN NULL", "SQL uses IS NULL because NULL represents an unknown value.")
_append_question("sql", "Aggregation", "Which clause filters groups after aggregation?", "HAVING", "WHERE", "FROM", "INSERT", "HAVING applies conditions to grouped results.")
_append_question("data-science", "Pandas", "What does DataFrame.describe() provide for numeric columns?", "Summary statistics", "A trained model", "A database join", "A sorted index only", "describe reports count, mean, standard deviation, and quartiles.")
_append_question("data-science", "Statistics", "What does the mean represent?", "The sum divided by the number of observations", "The middle ordered value", "The most frequent category", "The largest observation", "The arithmetic mean is the total divided by the count.")
_append_question("machine-learning", "Features", "What is a feature in a prediction task?", "An input variable used to make predictions", "The final score only", "The target label", "A chart title", "Features are input variables from which a model learns patterns.")
_append_question("machine-learning", "Validation", "What is a validation set commonly used for?", "Comparing models or tuning choices before final testing", "Replacing all training examples", "Encoding the deployed target", "Measuring network speed", "Validation supports model selection while the test set remains held out.")
_append_question("dsa", "Graphs", "How does breadth-first search typically explore a graph?", "Neighbors in increasing distance layers", "One path to its end before others", "Nodes sorted by label only", "Only nodes in cycles", "BFS uses a queue to explore layer by layer.")
_append_question("dsa", "Sorting", "What is merge sort's typical time complexity?", "O(n log n)", "O(1)", "O(log n)", "O(n squared) in every case", "Merge sort divides and merges the input, giving n log n work.")

# Additional tracks
_NEW_RAW = {
    "react": {
        "title": "React Fundamentals", "category": "Web development", "icon": "Re", "level": "Beginner to intermediate", "weeks": 5,
        "description": "Build interactive interfaces with components, props, state, and modern React patterns.",
        "resources": [
            ("React Learn", "Documentation", "Official, hands-on introduction to components and interactive UI.", "https://react.dev/learn"),
            ("React Quick Start", "Learning path", "Build your first React components and learn the core workflow.", "https://react.dev/learn/installation"),
            ("React video lessons", "Video", "Browse project-based React lessons for new developers.", "https://www.youtube.com/results?search_query=React+beginner+course+components+hooks"),
        ],
        "cards": [
            ("What is a React component?", "A reusable piece of UI, usually written as a JavaScript function that returns markup."),
            ("What are props?", "Read-only inputs passed from a parent component to a child."),
            ("What is state?", "Component data that can change over time and trigger a re-render."),
            ("Why use a key in a rendered list?", "It helps React identify which items changed, moved, or were removed."),
        ],
        "questions": [
            ("Components", "What does a React component typically return?", "UI markup", "A database table", "A CSS file only", "A browser window", "Components describe the UI to render."),
            ("Props", "How should a child component treat props?", "As read-only inputs", "As global variables to overwrite", "As browser cookies", "As CSS selectors", "Props are passed into a component and should not be mutated."),
            ("State", "What happens when component state changes?", "React can render the component again", "The browser always restarts", "The source file is rewritten", "The component is deleted", "State updates tell React that the UI may need to reflect new data."),
            ("Lists", "Why provide stable keys when rendering a list?", "To help React track items between renders", "To encrypt the list", "To sort items alphabetically", "To style every item identically", "Keys help React match list items as the collection changes."),
        ],
    },
    "cpp": {
        "title": "C++ Programming", "category": "Programming", "icon": "C++", "level": "Beginner to intermediate", "weeks": 7,
        "description": "Learn compiled programming with C++, covering types, functions, references, classes, and resource ownership.",
        "resources": [
            ("Learn C++", "Learning path", "Structured tutorials for modern C++ language fundamentals.", "https://www.learncpp.com/"),
            ("cppreference", "Documentation", "Reference for the C++ language and standard library.", "https://en.cppreference.com/w/"),
            ("C++ video lessons", "Video", "Browse beginner courses and practical C++ examples.", "https://www.youtube.com/results?search_query=C%2B%2B+programming+beginner+course"),
        ],
        "cards": [
            ("What is a C++ reference?", "An alias for an existing object, bound at initialization."),
            ("What does const express?", "That an object or view should not be modified through that name."),
            ("What is RAII?", "Managing resource lifetime through object construction and destruction."),
            ("What does a vector provide?", "A dynamically sized sequence with contiguous storage."),
        ],
        "questions": [
            ("Types", "Which standard C++ container is a dynamically sized sequence?", "std::vector", "std::tuple", "std::array only", "std::exception", "vector grows as elements are added and stores them contiguously."),
            ("References", "What is a reference in C++?", "An alias for an existing object", "A dynamically allocated array", "A namespace", "A compiler warning", "A reference refers to an existing object."),
            ("Const correctness", "What does const on an object generally communicate?", "It should not be modified through that name", "It is stored on the internet", "It can only be an integer", "It is automatically deleted", "const restricts modification through that access path."),
            ("Resource safety", "What is the core idea of RAII?", "Tie resource lifetime to object lifetime", "Allocate every object globally", "Avoid using destructors", "Store source code in a vector", "RAII uses construction and destruction to manage resources reliably."),
        ],
    },
    "git-github": {
        "title": "Git & GitHub", "category": "Developer tools", "icon": "Git", "level": "Beginner", "weeks": 3,
        "description": "Track changes, create branches, collaborate safely, and understand the everyday Git workflow.",
        "resources": [
            ("Pro Git book", "Documentation", "The complete Git book, available online for free.", "https://git-scm.com/book/en/v2"),
            ("GitHub Skills", "Practice", "Interactive exercises for repositories, branches, and collaboration.", "https://skills.github.com/"),
            ("Git video lessons", "Video", "Browse concise Git and GitHub workflow tutorials.", "https://www.youtube.com/results?search_query=Git+and+GitHub+beginner+tutorial"),
        ],
        "cards": [
            ("What does git commit do?", "Records staged changes as a new snapshot in the local repository."),
            ("What is a branch?", "An independent line of development with its own commit history pointer."),
            ("What does git pull do?", "Fetches remote changes and integrates them into the current branch."),
            ("What is a pull request?", "A proposal to review and merge changes into another branch on a hosting service."),
        ],
        "questions": [
            ("Snapshots", "Which command records staged changes in local history?", "git commit", "git status", "git clone", "git init", "git commit creates a new repository snapshot from staged changes."),
            ("Branches", "What is a Git branch best understood as?", "A movable pointer to a line of commits", "A copy of the entire computer", "A remote password", "A compressed archive", "Branches let work progress independently from other lines of development."),
            ("Remote workflow", "What does git fetch do?", "Downloads remote references and objects without merging them", "Deletes the current branch", "Creates a new GitHub account", "Stages every file", "fetch updates remote-tracking information without integrating it into the current branch."),
            ("Collaboration", "What is a pull request used for?", "Reviewing proposed changes before merging", "Replacing a local commit message", "Creating a programming language", "Encrypting a folder", "Pull requests provide a collaborative review and merge workflow."),
        ],
    },
    "cybersecurity": {
        "title": "Cybersecurity Basics", "category": "Security", "icon": "Sec", "level": "Beginner", "weeks": 5,
        "description": "Build practical awareness of authentication, access control, secure web design, and common application risks.",
        "resources": [
            ("OWASP Top 10: 2025", "Reference", "Current awareness guide to common web application security risks.", "https://top10.owasp.org/2025/"),
            ("OWASP Developer Guide", "Learning path", "Practical foundations for building and reviewing safer software.", "https://devguide.owasp.org/"),
            ("Cybersecurity video lessons", "Video", "Browse introductory application security and threat modeling lessons.", "https://www.youtube.com/results?search_query=application+security+beginner+course+OWASP"),
        ],
        "cards": [
            ("What is least privilege?", "Give each person or service only the access needed for its task."),
            ("What is phishing?", "A deceptive attempt to obtain information or prompt unsafe actions."),
            ("Why hash passwords?", "To store a one-way derived value instead of the original password."),
            ("What is input validation?", "Checking that incoming data matches expected rules before processing it."),
        ],
        "questions": [
            ("Access control", "What does the principle of least privilege recommend?", "Grant only the access needed for the task", "Give every user administrator access", "Share one account with everyone", "Disable access reviews", "Limiting permissions reduces the impact of mistakes or compromised accounts."),
            ("Authentication", "Why should passwords be stored as salted hashes?", "To avoid storing recoverable plain-text passwords", "To make passwords visible to support staff", "To reuse passwords across sites", "To shorten usernames", "A suitable password hash makes recovering the original value difficult."),
            ("Web security", "What is a common defense against SQL injection?", "Use parameterized queries", "Concatenate raw input into SQL", "Hide the submit button", "Rename the database", "Parameters keep user input separate from SQL syntax."),
            ("Threats", "What is phishing?", "A deceptive message designed to steal information or trigger an unsafe action", "A database backup strategy", "A type of encryption key", "A harmless browser theme", "Phishing uses impersonation or urgency to manipulate a target."),
        ],
    },
    "cloud-fundamentals": {
        "title": "Cloud Computing", "category": "Cloud", "icon": "Cl", "level": "Beginner", "weeks": 5,
        "description": "Understand cloud service models, regions, shared responsibility, and the building blocks of cloud applications.",
        "resources": [
            ("AWS Skill Builder", "Learning path", "Official digital training and cloud learning resources from AWS.", "https://skillbuilder.aws/"),
            ("Google Cloud training", "Learning path", "Courses and hands-on labs for cloud concepts and services.", "https://cloud.google.com/learn/training"),
            ("Cloud computing video lessons", "Video", "Browse introductions to cloud architecture and service models.", "https://www.youtube.com/results?search_query=cloud+computing+fundamentals+beginner+course"),
        ],
        "cards": [
            ("What is elasticity in cloud computing?", "The ability to scale resources up or down as demand changes."),
            ("What does IaaS provide?", "On-demand infrastructure such as compute, networking, and storage."),
            ("What is a cloud region?", "A geographic area containing one or more cloud data center locations."),
            ("What is shared responsibility?", "The provider and customer each handle defined parts of security and operations."),
        ],
        "questions": [
            ("Service models", "What does Infrastructure as a Service commonly provide?", "On-demand compute, networking, and storage", "Only a finished email application", "A programming language", "A spreadsheet formula", "IaaS offers configurable infrastructure resources."),
            ("Scaling", "What does elasticity mean for cloud resources?", "Resources can adjust as demand changes", "Every resource is permanently fixed", "All data is public", "The application needs no security", "Elasticity allows capacity to expand or contract with workload needs."),
            ("Geography", "What is a cloud region?", "A geographic area with cloud infrastructure locations", "A user password", "A single application feature", "A virtual machine image format", "Providers group data center locations into geographic regions."),
            ("Security", "What does shared responsibility mean?", "Provider and customer each own specific security duties", "The provider handles every customer setting", "The customer owns provider hardware", "Security is optional", "Cloud security duties are divided based on service and configuration."),
        ],
    },
    "statistics": {
        "title": "Statistics & Probability", "category": "Mathematics", "icon": "Σ", "level": "Beginner", "weeks": 6,
        "description": "Make sense of data with distributions, averages, probability, sampling, and careful interpretation.",
        "resources": [
            ("Khan Academy statistics", "Learning path", "Lessons and practice on descriptive statistics and probability.", "https://www.khanacademy.org/math/statistics-probability"),
            ("OpenStax Introductory Statistics", "Textbook", "A free textbook with examples, explanations, and exercises.", "https://openstax.org/details/books/introductory-statistics-2e"),
            ("Statistics video lessons", "Video", "Browse visual explanations of probability and core statistics.", "https://www.youtube.com/results?search_query=statistics+and+probability+beginner+course"),
        ],
        "cards": [
            ("What does standard deviation describe?", "How spread out observations are around their mean."),
            ("What is a sample?", "A subset of a population selected for observation or analysis."),
            ("What does correlation measure?", "The strength and direction of association between variables."),
            ("What is a probability?", "A number from zero to one describing the likelihood of an event."),
        ],
        "questions": [
            ("Center", "Which measure is most affected by extreme values?", "Mean", "Median", "Mode", "Interquartile range", "The mean uses every value directly, so extremes can move it substantially."),
            ("Spread", "What does standard deviation summarize?", "Typical spread around the mean", "The largest observation only", "The number of categories", "The sample's first value", "Standard deviation measures variability around the mean."),
            ("Probability", "What is the probability of an impossible event?", "0", "0.5", "1", "It depends on the sample size", "An impossible event has probability zero."),
            ("Interpretation", "If two variables are correlated, what can you conclude?", "They are associated, but causation is not established", "One definitely causes the other", "They must have identical values", "The data contains no uncertainty", "Correlation alone does not establish a causal relationship."),
        ],
    },
    "ui-ux-design": {
        "title": "UI & UX Design", "category": "Design", "icon": "UX", "level": "Beginner", "weeks": 5,
        "description": "Design clear digital experiences through user research, hierarchy, prototyping, and iterative usability feedback.",
        "resources": [
            ("Figma design and prototype help", "Documentation", "Guides for creating, prototyping, and collaborating on designs.", "https://help.figma.com/hc/en-us/categories/360002042553-Design-and-prototype"),
            ("Nielsen Norman Group usability heuristics", "Reference", "Ten widely used principles for evaluating interface usability.", "https://www.nngroup.com/articles/ten-usability-heuristics/"),
            ("UI and UX design video lessons", "Video", "Browse introductory tutorials on wireframes, visual hierarchy, and prototypes.", "https://www.youtube.com/results?search_query=UI+UX+design+beginner+course+wireframing"),
        ],
        "cards": [
            ("What is a wireframe?", "A simplified layout showing structure and content priority before visual polish."),
            ("What is usability testing?", "Watching representative users attempt tasks to find interaction problems."),
            ("What is visual hierarchy?", "The arrangement of elements to guide attention by importance."),
            ("Why prototype an interface?", "To explore and test interactions before committing to a finished build."),
        ],
        "questions": [
            ("Research", "What is the main purpose of usability testing?", "Find where people struggle with real tasks", "Prove a design is perfect", "Choose brand colors by vote", "Measure server speed", "Usability testing reveals obstacles in a design through observed tasks."),
            ("Structure", "What does a wireframe focus on?", "Page structure and content priority", "Final animation timing only", "Database indexing", "Production deployment", "Wireframes communicate layout before detailed visual styling."),
            ("Hierarchy", "What is visual hierarchy used for?", "Guide attention to information by importance", "Hide every secondary action", "Make all elements identical", "Replace user research", "Hierarchy helps people scan and understand an interface."),
            ("Prototyping", "Why create an interactive prototype?", "Explore flows and gather feedback before implementation", "Store customer passwords", "Guarantee every user will agree", "Replace accessibility review", "Prototypes make interaction ideas testable early."),
        ],
    },
    "excel-analytics": {
        "title": "Excel for Data Analysis", "category": "Productivity", "icon": "XL", "level": "Beginner to intermediate", "weeks": 4,
        "description": "Organize data, write useful formulas, summarize with pivot tables, and present findings clearly.",
        "resources": [
            ("Microsoft Learn: Excel training", "Learning path", "Microsoft training modules for Excel and data analytics.", "https://learn.microsoft.com/en-us/training/browse/?products=office-excel"),
            ("Excel help and learning", "Documentation", "Official help articles, formula guidance, and learning material.", "https://support.microsoft.com/excel"),
            ("Excel analytics video lessons", "Video", "Browse lessons on formulas, tables, charts, and pivot tables.", "https://www.youtube.com/results?search_query=Excel+data+analysis+beginner+course+pivot+tables"),
        ],
        "cards": [
            ("What is a spreadsheet formula?", "An expression beginning with = that calculates a value."),
            ("What does a pivot table do?", "Groups and summarizes data interactively by fields."),
            ("Why turn a range into a table?", "Tables expand with new rows and make structured references easier."),
            ("What does an absolute cell reference look like?", "A reference with dollar signs, such as $A$1, that stays fixed when copied."),
        ],
        "questions": [
            ("Formulas", "What character begins a formula in Excel?", "=", "+", "#", "@", "Excel formulas begin with an equals sign."),
            ("References", "Which reference remains fixed when copied across rows and columns?", "$A$1", "A1", "A$1 only", "A:A only", "Dollar signs make both the column and row absolute."),
            ("Summaries", "What is a pivot table designed to do?", "Group and summarize data by selected fields", "Write application code", "Encrypt a workbook", "Change the operating system", "Pivot tables summarize and reorganize tabular data."),
            ("Data quality", "Why use a filter on a table?", "Show rows matching selected criteria", "Delete all hidden data", "Change formulas to values", "Create a password", "Filters temporarily limit which records are displayed."),
        ],
    },
}


for _course_id, _raw_course in _NEW_RAW.items():
    COURSES[_course_id] = _build_course(_course_id, _raw_course)


_append_question("react", "Events", "How should a React click event handler be passed?", "As a function, such as onClick={handleClick}", "As a quoted function call, onClick='handleClick()'", "As a CSS class", "As an HTML comment", "Passing a function lets React call it when the event occurs.")
_append_question("react", "State", "Which hook is commonly used for local component state?", "useState", "useRoute", "useFetchNow", "useClass", "useState adds state to a function component.")
_append_question("cpp", "Compilation", "What does a compiler do with C++ source code?", "Translates it into a form the target platform can execute", "Runs the program one line at a time in a browser", "Creates a Git branch", "Designs the user interface", "A compiler translates source into object code or an executable.")
_append_question("cpp", "Memory", "What does a smart pointer help manage?", "Ownership and lifetime of a dynamically allocated object", "CSS layout", "A database transaction", "A network domain name", "Smart pointers express ownership and automatically manage object lifetime.")
_append_question("git-github", "Staging", "What does git add do?", "Stages selected changes for the next commit", "Uploads a commit to every remote", "Creates a new repository account", "Deletes all untracked files", "git add places chosen changes in the staging area.")
_append_question("git-github", "History", "What does git status show?", "The current branch and working tree changes", "The source code of every remote", "A list of installed compilers", "The website's traffic", "git status summarizes staged, unstaged, and untracked changes.")
_append_question("cybersecurity", "Web security", "What does output encoding help prevent?", "Untrusted text being interpreted as executable markup or script", "Every network outage", "Weak wireless signal", "A forgotten file name", "Context-aware encoding helps keep data from being treated as code.")
_append_question("cybersecurity", "Updates", "Why install security updates promptly?", "They can fix known vulnerabilities", "They guarantee zero future incidents", "They remove the need for backups", "They make passwords public", "Updates often address weaknesses that attackers already know about.")
_append_question("cloud-fundamentals", "Storage", "What is object storage commonly suited for?", "Large unstructured files addressed as objects", "CPU instructions", "A local keyboard layout", "Sorting source code", "Object storage is used for files such as images, backups, and media.")
_append_question("cloud-fundamentals", "Availability", "What does high availability aim to provide?", "Service access with minimal interruption", "Unlimited free compute", "No need for monitoring", "A single point of failure", "High availability designs reduce downtime through redundancy and recovery.")
_append_question("statistics", "Sampling", "Why use random sampling?", "To give population members a known chance of selection", "To ensure every sample is identical", "To eliminate all uncertainty", "To prove a hypothesis true", "Random sampling can reduce selection bias when designed appropriately.")
_append_question("statistics", "Correlation", "What range can a Pearson correlation coefficient take?", "From -1 to 1", "From 0 to 100", "From negative infinity to infinity", "Only 0 or 1", "The coefficient describes linear association on a scale from -1 through 1.")
_append_question("ui-ux-design", "Accessibility", "What is a benefit of clear keyboard focus indicators?", "Keyboard users can see which control is active", "It makes page text larger automatically", "It hides interactive controls", "It replaces labels", "A visible focus state supports navigation without a mouse.")
_append_question("ui-ux-design", "Iteration", "What should a designer do after usability feedback?", "Use evidence to refine and retest the design", "Ignore repeated issues", "Add every requested feature immediately", "Remove all navigation", "Iterative design uses feedback to improve and validate solutions.")
_append_question("excel-analytics", "Functions", "Which Excel function counts numeric cells in a range?", "COUNT", "SUMTEXT", "AVERAGEIFALL", "ROWVALUE", "COUNT returns the number of cells containing numbers.")
_append_question("excel-analytics", "Charts", "Which chart is usually suitable for comparing values across categories?", "Bar or column chart", "A 3D map for every dataset", "A single-cell formula", "A password dialog", "Bars or columns make category comparisons straightforward.")
