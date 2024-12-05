# <a name="_1q9xudxbwr7s"></a>**SmartShare - Console Application**
# <a name="_hmrp6ygu7t3c"></a>**OVERVIEW**

Smartshare is a digital platform designed to empower students by providing equitable access to

essential gadgets and resources needed for academic success. With the increasing reliance on

technology for learning, SmartShare addresses the challenges many students face in acquiring

expensive educational tools that they can borrow such as laptops, tablets, scientific calculators, etc. It

fosters collaboration, resource-sharing, and equitable access to learning tools, empowering  students

to overcome barriers and excel in their education.


# <a name="_ed4xxsbm2frh"></a> **Python Concepts Used**
**Python Libraries:**

- **datetime**: This library is used for handling dates and times in the application, including tracking borrowing dates, return dates, and calculating overdue penalties.

  **Classes and Methods:**

- The application is structured around the SmartShare class, which encapsulates all functionality related to gadget borrowing and returning. Key methods within the class include:

- ***register\_user*()**: Allows users to register by entering their details.
- ***list\_items*()**: Displays the available gadgets for borrowing.
- ***select\_duration*()**: Lets users choose the duration of the borrowing period.
- ***borrow\_item*()**: Manages the borrowing process, including penalty notices and item availability.
- ***view\_borrow\_history*()**: Displays the user's borrowing history along with any penalties incurred.
- ***return\_item*()**: Allows users to return borrowed gadgets and calculates any overdue penalties.
- ***calculate\_penalty*()**: Calculates the penalty based on the number of overdue days.
- ***main\_menu*()**: The main interface for the user to interact with the application.

**List of Dictionaries**: Data about users and gadgets are stored in lists of dictionaries, making it easy to manage and retrieve information.

**Datetime Handling**: Dates are managed using Python’s datetime module, allowing the program to track borrowing and return dates accurately and compute overdue penalties.

**Input Validation**: The application checks for valid user inputs using loops and conditionals. If the input is invalid (e.g., a non-numeric value when a number is expected), it prompts the user to re-enter a valid input.

**Exception Handling**: The program handles potential exceptions, such as ValueError during input parsing, ensuring smooth user experience.

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


###
### <a name="_3ftggr467i6y"></a><a name="_4en2cfblk6dr"></a>**Instructions for Running the SmartShare Program**
**Ensure You Have Python Installed**
The program requires Python 3 to run. Check your Python version by executing the following command in your terminal or command prompt:

**Prepare the Program File**

- Save the program code in a .py file. For example, save it as smartshare.py.

**Run the Program**

- Open a terminal or command prompt and navigate to the directory containing smartshare.py.
- You could also use VScode or any ide as long as it runs Python 3.

**Interact with the Menu**
After running the program, you will see a menu with the following options:

===== SmartShare Menu =====

1\. Registration

2\. List of Available Gadgets

3\. Borrow a Gadget

4\. View Borrowing History

5\. Return a Gadget

6\. Exit

` `the main menu will appear with the following options:
1. ### <a name="_3dhs5qrvx9n3"></a>**Registration**
- Allows users to register their complete information, specifically their name, email, school and phone number.
##
1. ### <a name="_qcvghhv798gn"></a><a name="_r4bqdq63v01"></a>**List Available Gadgets**
   -It will Display a list of gadgets that can be borrowed depending on the user’s preference. Below are the following gadgets that they can choose from:

1. Laptop
1. Tablet
1. Scientific Calculator
1. USB Flash Drive
1. Power Bank
1. Charger
1. Printer
### <a name="_smguh95mwr1a"></a>**III.  Borrow a Gadget**
- Lets users select a gadget and borrowing duration, with penalty notifications for late returns.
- The borrowing duration will range from 1 day and the maximum duration will be 30 days.
### <a name="_4pdxjv6w2k5w"></a>**IV. View Borrowing History**
- ### <a name="_9zg4ob5qwjk1"></a> Allows users to view their past borrowing records, including penalties or how much fine they will pay, depending on how long it takes for them to return the borrowed item.
### <a name="_acwj8zxknrbx"></a>**V.Return a Gadget**
- ` `Users can return borrowed items, and any overdue penalties will be calculated.
### <a name="_eh7xmxu98oeg"></a>**VI. Exit**
- ` `Exits the program.

**Handling Errors:**

- The program will prompt the user to correct invalid inputs (ex. entering non-numeric values when a number is expected).
- If a user enters an email that is not registered or attempts to borrow an unavailable gadget, the program will display an appropriate message.

**Exit and Restart:**

- To exit the program, select the “Exit” option from the main menu.
- You can restart the program by running the script again in the terminal or any ide that you use.


