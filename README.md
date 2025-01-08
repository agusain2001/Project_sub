# Hostel-Management-System

A Django REST Framework based API for managing expenses, settlements, and groups, designed primarily for students or shared living arrangements.

## Project Overview

This API provides a comprehensive solution for tracking expenses, managing settlements, handling group finances, and authenticating users in a shared environment. It is built using Django REST Framework, making it robust and scalable. The application includes features for user management, expense tracking, settlement tracking, group management, user authentication and some basic analytics.

## Key Features

*   **User Management:**
    *   User registration and authentication using JWT (JSON Web Tokens).
    *   Custom user fields: `college`, `semester`, and `default_payment_methods`.
    *   Token generation for user authentication using username and password.
    *   Admin users with elevated privileges for managing categories and users.
*   **Expense Tracking:**
    *   Record expenses with details such as `amount`, `category`, `split_type`, `date`, `receipt_image`, and participants.
    *   Associate expenses with groups and users.
    *   Different splitting types: `equal`, `unequal`, and `percentage`.
*   **Group Management:**
    *   Create and manage groups with different types (e.g., `hostel_roommates`, `project_teams`, `trip_groups`).
    *   Add members to groups.
*   **Settlement Management:**
    *   Track payments between users.
    *   Payment status options: `pending` and `completed`.
    *   Settlement suggestions based on outstanding balances.
*   **Category Management:**
    *   Create and manage expense categories.
*   **Analytics:**
    *   Monthly analysis of expenses by category for each user.
* **UPI Linking:**
    * Store UPI id for users in their profile.
*   **Permissions:**
    *   `IsAuthenticatedOrReadOnly`: Read access for all users; write access only for authenticated users.
    *   `IsOwnerOrReadOnly`: Update/delete access only for the creator of a resource or superuser.
    *  `IsAdminOrReadOnly`: Update/delete access only for superusers, read access for all users.
    * `IsOwnerOrAdminOrReadOnly`: Update/delete access only for the owner or a superuser, read access for all users.

## Technical Details

*   **Backend:**
    *   **Python 3.8+**
    *   **Django 4.2.6**
    *   **Django REST Framework 3.14.0**
    *   **Django REST Framework Simple JWT 5.2.2**
    *   **Database:** PostgreSQL
*   **API Documentation:** Swagger/OpenAPI specification generated using `drf-spectacular`.

## Project Structure

The project is structured as follows:

*   `expense_tracker/`: Main Django project configuration.
    *   `settings.py`: Project-wide settings.
    *   `urls.py`: Main URL configuration.
*   `categories/`: Manages expense categories.
    *   `models.py`: Defines the `Category` model.
    *   `serializers.py`: Defines the `Category` serializer.
    *  `views.py`: Defines the API view for `Category` model.
*   `expenses/`: Manages individual expenses.
    *   `models.py`: Defines the `Expense` model.
    *   `serializers.py`: Defines the `Expense` serializer.
    *   `split_types.py`: Defines the expense split types.
    *   `views.py`: Defines the API view for `Expense` model.
*   `groups/`: Manages user groups.
    *   `models.py`: Defines the `Group` model.
    *   `serializers.py`: Defines the `Group` serializer.
    * `views.py`: Defines the API view for `Group` model.
*   `settlements/`: Manages settlements between users.
    *   `models.py`: Defines the `Settlement` model.
    *  `settlement_choices.py`: Defines the settlement status options.
    *   `serializers.py`: Defines the `Settlement` serializer.
    *   `views.py`: Defines the API view for `Settlement` model.
*   `users/`: Manages user accounts.
    *   `models.py`: Defines the custom `User` model, extending Django's `AbstractUser`.
    *   `serializers.py`: Defines the `User` serializer.
    *    `views.py`: Defines the API view for `User` model and also the token generation endpoint.
*   `utils/`: Contains utility modules and files.
    *   `custom_errors.py`: Defines custom exception classes.
    *  `helpers.py`: Defines helper function for pagination and settlement suggestion.
    *   `permissions.py`: Defines custom permission classes.
*   `docs/`: Contains `swagger.yaml` for API documentation.
*  `tests/`: All the test files.
*   `requirements.txt`: Lists project dependencies.
*  `.env`: Stores the environment variables like database credentials.
*   `README.md`: Project documentation.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd hostel-management-system
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv myenv
    ```

3.  **Activate the virtual environment:**

    -   On Linux/macOS:

        ```bash
        source myenv/bin/activate
        ```

    -   On Windows:

        ```bash
        myenv\Scripts\activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
5.  **Set Environment Variables:** Create a `.env` file in the root directory and add your database credentials like below**
  ```bash
    DATABASE_NAME=expense_tracker_db
    DATABASE_USER=your_username
    DATABASE_PASSWORD=your_password
    DATABASE_HOST=localhost
    DATABASE_PORT=5432

Then add import and load environment statement to your expense_tracker/settings.py file like below
python
import os
from dotenv import load_dotenv

load_dotenv()

and use those environment variables for database settings as well.
```

6. **Apply database migrations: **

```bash
python manage.py makemigrations
python manage.py migrate
```

6.1 ***Run the development server:***
```bash 
python manage.py runserver
```
6.2 ***Access the API documentation:***

Navigate to http://127.0.0.1:8000/api/schema/swagger-ui/ in your browser.

** API Endpoints **
* ***Users***:

   * GET /api/users/: List all users. (Admin only)

   * GET /api/users/<int:pk>: Get a specific user.(Admin only)

   * POST /api/users/: Create a new user. (Admin only)

   * PUT /api/users/<int:pk>: Update a specific user.(Admin only)

   * DELETE /api/users/<int:pk>: Delete a specific user.(Admin only)

   * POST /api/token/: Obtain authentication tokens with a username and password.

* ***Expenses***:

   * GET /api/expenses/: List all expenses for authenticated user.

   * POST /api/expenses/: Create a new expense.

   * GET /api/expenses/<int:pk>: Get a specific expense.

   * PUT /api/expenses/<int:pk>: Update a specific expense.(Owner only)

   * DELETE /api/expenses/<int:pk>: Delete a specific expense. (Owner only)

   * GET /api/expenses/monthly-analysis?month=<int>: Get monthly analysis report of the user.

* ***Groups***:

   * GET /api/groups/: List all groups.

   * POST /api/groups/: Create a new group.

   * GET /api/groups/<int:pk>: Get specific group.

   * PUT /api/groups/<int:pk>: Update specific group.(Owner/Admin only)

   * DELETE /api/groups/<int:pk>: Delete specific group. (Owner/Admin only)

* ***Settlements***:

   * GET /api/settlements/: List all settlements.

   * POST /api/settlements/: Create a new settlement.

   * GET /api/settlements/<int:pk>: Get a specific settlement.

   * PUT /api/settlements/<int:pk>: Update a specific settlement.(Owner/Admin only)

   * DELETE /api/settlements/<int:pk>: Delete a specific settlement.(Owner/Admin only)

   * GET /api/settlements/<int:pk>/suggestions: Get settlement suggestions for a group.

* ***Categories:***

   * GET /api/categories/: List all categories.

   * POST /api/categories/: Create a new category. (Admin only)

   * GET /api/categories/<int:pk>: Get a specific category.(Admin only)

   * PUT /api/categories/<int:pk>: Update a specific category. (Admin only)

   * DELETE /api/categories/<int:pk>: Delete a specific category. (Admin only)

** Models**
* ***User:***

   * id: (Integer) Unique identifier.

   * username: (String) Username for login.

   * password: (String) Password for login.

   * email: (String) Email for registration

   * college: (String) College name.

   * semester: (String) Current semester.

   * default_payment_methods: (JSON) List of payment method details like UPI_ID.

* ***Expense:***

   * id: (Integer) Unique identifier.
   
   * amount: (Decimal) Amount of the expense.

   * category: (ForeignKey to Category) Category of the expense.

   * split_type: (String) Type of expense split (equal, unequal, or percentage).

   * date: (Date) Date of the expense.

   * receipt_image: (ImageField) Image of the receipt.

   * participants: (ManyToManyField) List of users who were part of the expense.

   * created_by: (ForeignKey to User) User who created the expense.

   * group: (ForeignKey to Group) Group that the expense belong to.

* ***Group:***

   * id: (Integer) Unique identifier.

   * name: (String) Name of the group.

   * group_type: (String) Type of the group (e.g., hostel_roommates, project_teams).

   * members: (ManyToManyField to User) List of members in the group.

   * created_by: (ForeignKey to User) User who created the group.

* ***Settlement:***

   * id: (Integer) Unique identifier.

   * payer: (ForeignKey to User) User making the payment.

   * payee: (ForeignKey to User) User receiving the payment.

   * amount: (Decimal) Amount of the payment.

   * payment_status: (String) Status of the payment (pending or completed).

   * settlement_method: (String) Method of payment.

   * due_date: (Date) Due date of settlement.

   * group: (ForeignKey to Group) Group that the settlement belong to.

* ***Category:***

   * id: (Integer) Unique identifier.

   * name: (String) Name of the category.

**Future Work**
   * ***Unit Tests:*** Write comprehensive unit tests to ensure the code's reliability.

   * ***Email Verification:*** Implement email verification for user registration.

   * ***Smart bill scanning:*** If required, implement smart bill scanning using image processing.

   * ***Code Refactoring and Optimization:*** Refactor code and improve the structure for better readability and performance.

   * ***Complete Documentation:*** Document all the models and functionalities of the project.

**Contributing**
Contributions are welcome! Please feel free to submit a pull request.

**Explanation of the `README.md`**

*   **Comprehensive Overview:** The `README.md` provides a clear overview of the project's purpose, features, and technical details.
*   **Detailed Setup Instructions:** Step-by-step instructions are provided for setting up the project locally.
*   **API Endpoints:** All the API endpoints are clearly documented with their methods and brief descriptions.
*   **Project Structure:** The file structure and its function is clearly explained.
*   **Model Description:** All the models and their respective fields are clearly explained.
*   **Clear Model Descriptions:** All the models used in the application are explained with fields and types.
*   **Future Work:** A clear plan for remaining and future work has been laid out.
*   **Contribution Guidelines:** Instructions are given for contributing to the project.

**Regarding "Only Payment Thing Remaining"**

As per your statement that only the payment thing is remaining. In the above documentation, I've added `UPI payment linking` where the users can save their UPI Ids which can help them in the payment process. If there's any other payment integration, you can add that after email verification.

This `README.md` should provide excellent documentation for your project. Let me know if you have any other questions or would like to proceed with any further steps!


