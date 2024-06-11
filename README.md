# FinanceGPT : Fullstack Chat Application with Trading Functionality

## Overview

This project is a fullstack chat application that integrates trading functionalities via the Upstox REST APIs. It uses agents from LangChain and the Mistral 7B model (deployed on Groq) to enable users to perform trading transactions using natural language prompts.

## Features

- **Real-time Chat**: Users can engage in real-time chat with the application.
- **Trading via Prompts**: Users can execute trading transactions by simply typing natural language commands.
- **Integration with Upstox**: Utilizes Upstox REST APIs for performing trading operations.
- **AI Agents**: Implements LangChain agents and the Mistral 7B model for natural language understanding and processing.

## Technologies Used

- **Frontend**: React.js, HTML, CSS
- **Backend**: Django
- **Database**: PostgreSQL
- **AI Models**: LangChain, Mistral 7B (deployed on Groq)
- **Trading API**: Upstox REST API

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js
- PostgreSQL
- Upstox API Key and Secret

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/ketanmore2002/finanacegpt.git
   cd finanace_gpt
   ```

2. **Install Backend Dependencies**
   ```sh
   cd server
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies**
   ```sh
   cd ../client
   npm install
   ```

4. **Setup Environment Variables**

   Create a `.env` file in the `server` directory with the following content:

   ```env
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_database_user
   POSTGRES_PASSWORD=your_database_password
   POSTGRES_HOST=your_database_host
   POSTGRES_PORT=your_database_port
   UPSTOX_API_KEY=your_upstox_api_key
   UPSTOX_API_SECRET=your_upstox_api_secret
   LANGCHAIN_API_KEY=your_langchain_api_key
   MISTRAL_GROQ_ENDPOINT=your_groq_endpoint
   ```

5. **Setup PostgreSQL Database**
   ```sh
   psql -U postgres
   CREATE DATABASE your_database_name;
   CREATE USER your_database_user WITH PASSWORD 'your_database_password';
   ALTER ROLE your_database_user SET client_encoding TO 'utf8';
   ALTER ROLE your_database_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_database_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
   ```

6. **Apply Django Migrations**
   ```sh
   cd ../server
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Run the Backend Server**
   ```sh
   python manage.py runserver
   ```

8. **Run the Frontend Server**
   ```sh
   cd ../client
   npm start
   ```

9. **Access the Application**
   Open your browser and navigate to `http://localhost:3000`

## Usage

### Chat Interface

1. **Log In**: Users need to log in or register to start using the application.
2. **Chat**: Use the chat interface to send messages.
3. **Trading Commands**: Type natural language commands to perform trading actions. For example:
   - "Buy 10 shares of AAPL"
   - "Sell 5 shares of TSLA"
   - "Show my portfolio"

### Example Commands

- **Buying Stocks**: "Buy 50 shares of GOOGL"
- **Selling Stocks**: "Sell 20 shares of AMZN"
- **Checking Portfolio**: "What's my portfolio?"
- **Getting Stock Prices**: "What's the current price of MSFT?"

## Architecture

### Frontend

- **React Components**: Handles user interface and interactions.
- **Redux**: Manages application state.
- **Axios**: For making HTTP requests to the backend.

### Backend

- **Django**: Handles API requests and responses.
- **Django ORM**: Manages PostgreSQL interactions.
- **Upstox API Integration**: Facilitates trading operations.
- **LangChain and Mistral 7B**: Processes natural language commands.

### AI Integration

- **LangChain Agents**: Interpret and manage user intents.
- **Mistral 7B Model (Deployed on Groq)**: Enhances natural language understanding for complex queries.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Upstox](https://upstox.com) for their comprehensive trading APIs.
- [LangChain](https://langchain.com) for their robust language processing capabilities.
- [Mistral AI](https://mistral.ai) for providing the Mistral 7B model.
- [Groq](https://groq.com) for hosting and deploying the Mistral 7B model.

---

Feel free to reach out if you have any questions or need further assistance!

**Happy Trading!**
___


## UI Images 

![](https://github.com/ketanmore2002/finanacegpt/blob/main/finance_gpt/image1.png?raw=true)

![](https://github.com/ketanmore2002/finanacegpt/blob/main/finance_gpt/image2.png?raw=true)

![](https://github.com/ketanmore2002/finanacegpt/blob/main/finance_gpt/image3.png?raw=true)

![](https://github.com/ketanmore2002/finanacegpt/blob/main/finance_gpt/image4.png?raw=true)
