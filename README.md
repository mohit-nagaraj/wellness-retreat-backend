# Retreat Booking API
Postman documentation: https://documenter.getpostman.com/view/29989847/2sA3kaAyP6

## Overview
The Retreat Booking API is a Flask-based application that allows users to book retreats, filter retreats, paginate results, and search for specific retreats. The API supports various endpoints to manage retreats and bookings.

## Features
- Create, Read, Update, Delete (CRUD) operations for retreats
- Filter retreats by term and location
- Paginate retreat results
- Search retreats by keywords
- Book a retreat ensuring no double booking for the same user
- Comprehensive error handling

## Prerequisites
- Python 3.8 or higher
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/retreat-booking-api.git
cd retreat-booking-api
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the `.env` File
Create a `.env` file in the root directory and add the following configuration:
```
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost/dbname
```
Replace `username`, `password`, `localhost`, and `dbname` with your PostgreSQL credentials and database name.

### 5. Initialize the Database
```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Run the Application
```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Vercel Deployment
To deploy the application to Vercel, ensure you have the `vercel.json` file in the root directory:

```json
{
    "version": 2,
    "builds": [
        {
            "src": "run.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "run.py"
        }
    ]
}
```

### Deploying to Vercel
1. Install Vercel CLI:
    ```bash
    npm install -g vercel
    ```

2. Deploy the application:
    ```bash
    vercel
    ```

3. Follow the prompts to complete the deployment process.

## API Endpoints

### Get Retreats
```http
GET /retreats
```
Query Parameters:
- `filter`: Filter retreats by term (optional)
- `location`: Filter retreats by location (optional)
- `search`: Search retreats by keywords (optional)
- `page`: Page number for pagination (default: 1)
- `limit`: Number of results per page (default: 100)

### Create Booking
```http
POST /book
```
Request Body:
```json
{
    "user_id": "12345",
    "user_name": "John Doe",
    "user_email": "johndoe@example.com",
    "user_phone": "1234567890",
    "retreat_id": "67890",
    "retreat_title": "Weekend Relaxation",
    "retreat_location": "Mountain Resort",
    "retreat_price": 299.99,
    "retreat_duration": 3,
    "payment_details": "Paid via credit card",
    "booking_date": "2023-08-25T00:00:00"
}
```

### Additional Endpoints
Add other CRUD operations and their request/response structures as needed.

## Models

### Retreats
- `id`: String, primary key
- `title`: String, required
- `description`: Text
- `date`: DateTime, required
- `location`: String
- `price`: Float, required
- `type`: String
- `condition`: String
- `image`: String
- `tag`: Array of Strings
- `duration`: Integer, required

### Bookings
- `id`: Integer, primary key
- `user_id`: String, required
- `user_name`: String, required
- `user_email`: String, required
- `user_phone`: String, required
- `retreat_id`: String, foreign key to Retreats
- `retreat_title`: String, required
- `retreat_location`: String, required
- `retreat_price`: Float, required
- `retreat_duration`: Integer, required
- `payment_details`: String, required
- `booking_date`: DateTime, default to current timestamp

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Contact
For any questions or issues, please open an issue in this repository.
