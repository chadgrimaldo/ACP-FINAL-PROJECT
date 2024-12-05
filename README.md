# <a name="_1q9xudxbwr7s"></a>**SmartShare - Console Application**
# <a name="_hmrp6ygu7t3c"></a>**OVERVIEW**

Smartshare is a digital platform designed to empower students by providing equitable access to

essential gadgets and resources needed for academic success. With the increasing reliance on

technology for learning, SmartShare addresses the challenges many students face in acquiring

expensive educational tools that they can borrow such as laptops, tablets, scientific calculators, etc. It

fosters collaboration, resource-sharing, and equitable access to learning tools, empowering  students

to overcome barriers and excel in their education.


# <a name="_ed4xxsbm2frh"></a> **Python Concepts Used**
#### <a name="_4gskwj5j38uj"></a>**Lists**
- **Purpose**: Used to store and manage collections of users (users), borrowed items (borrowed\_items), and available gadgets (items).

- The users list stores dictionaries, each representing a user's details.
- items is a list of dictionaries, each containing details about a gadget.
- These lists allow dynamic addition, removal, and iteration of elements.
#### <a name="_7fujurh88o2t"></a>**Dictionaries**
- **Purpose**: Used for structured data storage, making it easier to associate attributes ( name, condition, availability) with a single entity.
- Users, items, and borrow records are stored as dictionaries for flexible and readable attribute management.
#### <a name="_mt9b1v5i9cdh"></a>**Functions**
- **Purpose**: Encapsulate reusable blocks of code for modular design and readability.
- **Application**:
  - Functions like register\_user, list\_items, and borrow\_item break down the program into smaller, manageable tasks.
  - Parameters and return values are used to pass and retrieve data between functions.

#### <a name="_uceew0xffix7"></a>**Control Flow**
- **Purpose**: Manage decision-making and iteration.
- **Application**:
  - **if Statements**: Used to handle conditions like checking user registration or gadget availability.

**Loops**: For iterating over lists (e.g., listing gadgets).
####
#### <a name="_633fc4v54orj"></a><a name="_xz9nvoaxl2q"></a>**List Comprehensions**
- **Purpose**: Compact and readable syntax for filtering and transforming lists.
  #### <a name="_raoau750ytbc"></a>**Error Handling**
- **Purpose**: Prevent the program from crashing due to invalid user input.
- **Application**:
  - Used to handle exceptions like invalid menu choices or item selections.
#### <a name="_c6piy5gtrdv0"></a>**Datetime Module**
- **Purpose**: Provides tools for handling dates and times.
- **Application**:
  - **datetime.now()**: Retrieves the current date and time for recording borrow and return times.
- **timedelta**: Used to calculate return dates and overdue durations.
  ### <a name="_1svzk3cudzqs"></a>**2. Python Libraries**
  #### <a name="_vnbp0zb2angy"></a>**Standard Library**
- **datetime**:
  - Handles date and time manipulation, which is critical for calculating borrowing durations and fines.

**min() Function**:

- Used in calculate\_fine to ensure fines do not exceed a maximum value.

**enumerate()**:

- Simplifies list iteration by providing both the index and the item.
  python
  Copy code

## <a name="_1uqj0382ervt"></a>**Sustainable Development Goal #4: Quality Education**
Focuses on ensuring equitable, inclusive and quality education for all. Promoting lifelong learning opportunities in which education is recognized as a key driver for reducing poverty, improving health, innovation, and advancing economic growth.
### <a name="_vv6s322xoe9a"></a>**Integration of SDG 4 into SmartShare Project**
The **SmartShare Project** contributes directly to SDG 4 by facilitating access to essential educational tools, such as electronic gadgets, that are vital for modern learning. Here's how it aligns with SDG 4:

1. **Bridging the Digital Divide**
   1. The project ensures that students and learners from underprivileged or resource-constrained backgrounds have access to necessary gadgets 
   1. This helps reduce inequalities in education by making technology more accessible to all.
1. **Enhancing Learning Opportunities**
   1. Gadgets provided through the project support online learning, research, and assignments, thereby improving educational outcomes.
   1. Students can borrow tools for specific periods, allowing them to participate in digital or technology-enhanced learning activities.
1. **Promoting Equitable Access**
   1. By offering a borrowing system, the project eliminates the financial burden of purchasing expensive devices for students who may only need them temporarily.
   1. It democratizes access to technology, ensuring that education is not hindered by economic disparities.
1. ` `**Fostering Responsibility and Shared Learning**
   1. Through the borrowing system, users develop a sense of responsibility and community sharing, aligning with the broader values of SDG 4.
   1. Encouraging responsible gadget usage ensures that more individuals can benefit from these tools over time.


### <a name="_4en2cfblk6dr"></a>**Instructions for Running the SmartShare Program**
**Ensure You Have Python Installed**
The program requires Python 3 to run. Check your Python version by executing the following command in your terminal or command prompt:

**Prepare the Program File**

- Save the program code in a .py file. For example, save it as smartshare.py.



**Run the Program**

- Open a terminal or command prompt and navigate to the directory containing smartshare.py.
- You could also use VScode or any ide as long as it runs Python 3.

**Interact with the Menu**
After running the program, you will see a menu with the following options:

=== SmartShare Menu ===

1\. Registration

2\. List of Available Gadgets

3\. Borrow a Gadget

4\. View Borrowing History

5\. Return a Gadget

6\. Exit

- Enter the number corresponding  to your desired action and follow the prompts.

- **Features Overview**
  - **Registration**: Register as a new user by entering your details containing your name, email, school, and phone number. 
  - **List of Available Gadgets**: View a list of gadgets available for borrowing.
  - **Borrow a Gadget**: Select a gadget to borrow and specify the borrowing duration.
  - **View Borrowing History**: View your borrowing  history using your email.
  - **Return a Gadget**: Return borrowed items, specify their condition, and handle any penalties.
  - **Exit**: Close the program.
- **Input Guidelines**
  - Provide valid inputs as prompted. For example:
    - Choose numbers when selecting menu options or items from the list.
    - Enter a valid email address for user identification.
    - Specify item conditions as either "New" or "Used."
- **Exit the Program**
  To exit, select option 6 in the main menu.

