**# Django Book Store

[![GitHub stars](https://img.shields.io/github/stars/anasnashat/Book-store)](https://github.com/anasnashat/Book-store/stargazers)
[![GitHub license](https://img.shields.io/github/license/anasnashat/Book-store)](https://github.com/anasnashat/Book-store/blob/master/LICENSE)

Django Book Store is a web application built with Django, a high-level Python web framework, that allows users to browse and purchase books online. The application integrates with Stripe and PayPal for secure payment processing.

[Live Demo](https://anas-books-store-django.up.railway.app/)

![Django Book Store](https://img001.prntscr.com/file/img001/LGGsdLKhSN-XOws4iXKgzQ.png)

## Features

- Book Listings: Books are displayed with details such as title, author, description, price, and cover image.
- Search and Filtering: Users can search for books by title, author, or genre, and filter the results based on various criteria.
- Shopping Cart: Users can add books to their shopping cart and review the items before proceeding to checkout.
- Secure Payment Processing: The application integrates with both Stripe and PayPal to ensure secure payment transactions.
- Order Management: Users can view their order history and track the status of their orders.
- Admin Interface: Administrators have access to an admin interface to manage books, user accounts, and orders.
- Sales Reports: Generate visual reports of book sales using charts in the admin panel.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/anasnashat/Book-store.git
   ```
2. Change to the project directory:
    ``` shell
   cd Book-store
   ```
3. Create and activate a virtual environment:

 ```shell
    pip install pipenv
    pipenv shell
```
4. Install the required dependencies:
 ```shell
  pipenv install -r requirements.txt
```
5. Set up the database:
 ```shell
  python manage.py migrate
```

6. Create a superuser account:

```shell
    python manage.py createsuperuser
```
## Configure Stripe and PayPal API credentials:
- Stripe:
    - Sign up for a Stripe account at https://stripe.com.
    - Obtain your Stripe API keys.
    - Update the settings.py file with your Stripe API keys:
    ``` python
    STRIPE_PUBLIC_KEY = 'your-stripe-public-key'
    STRIPE_SECRET_KEY = 'your-stripe-secret-key'
  ```
  - PayPal:
      - Sign up for a PayPal Business account at https://www.paypal.com.
      - Obtain your PayPal API credentials.
      - Update the settings.py file with your PayPal API credentials:
      ``` python
      PAYPAL_CLIENT_ID = 'your-paypal-client-id'
      PAYPAL_SECRET_KEY = 'your-paypal-secret-key'
    ```
## Run the development server:
  ``` shell
  python manage.py runserver
```
Open your web browser and visit http://localhost:8000 to access the application.

## Usage:
    Browse the book catalog and click on a book to view its details.
    Use the search bar to find specific books by title, author, or genre.
    Add books to the shopping cart by clicking the "Add to Cart" button.
    Review the items in your cart and click "Checkout" to proceed to the payment page.
    Enter your payment details and complete the transaction using either Stripe or PayPal.
    View your order history and track the status of your orders.
    Access the admin panel by visiting http://localhost:8000/admin and log in with your superuser account.
    Generate sales reports with charts in the admin panel to analyze book sales data.

## Contributing

Contributions to Django Book Store are welcome! If you encounter any bugs, have feature requests, or want to contribute improvements, please open an issue or submit a pull request to the [GitHub repository](https://github.com/your-username/django-book-store).

We appreciate your help in making the Django Book Store better!

## Issue Tracker

If you find any bugs or have feature requests, please create an issue on the [issue tracker](https://github.com/your-username/django-book-store/issues). We'll do our best to address them as soon as possible.

## Pull Requests

We welcome pull requests with bug fixes, feature enhancements, or any other improvements. Follow these steps to submit a pull request:

1. Fork the repository and create your branch from `main`.
2. Make the necessary changes and ensure that the tests pass.
3. Write tests, if applicable, to cover the changes you made.
4. Commit your changes and push them to your forked repository.
5. Open a pull request in the main repository, describing the changes you made and providing any relevant information or context.

We'll review your pull request and provide feedback. Thank you for your contribution!

## Code Style

Please follow the existing code style and conventions used in the project to maintain consistency.

## License

By contributing to the Django Book Store project, you agree that your contributions will be licensed under the [MIT License](LICENSE).**




    




