# PyMotivator Bot

**PyMotivator** is a simple Python-based bot that fetches motivational quotes and sends them via WhatsApp using the Twilio API. The bot is scheduled to send a message every day at 7 AM (Asia/Kolkata timezone).

## Features
- Fetches quotes from a quote API.
- Sends WhatsApp messages via Twilio.
- Schedules messages to be sent daily at a specified time.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- A Twilio account (for sending WhatsApp messages).
- Twilio account credentials (`account_sid`, `auth_token`, and a verified phone number).

### Install the required Python packages:
```bash
pip install twilio
pip install apscheduler
pip install requests
```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amar-rakhpasre/PyMotivator.git
   cd PyMotivator
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `config.py` file**:
   In the root directory of the project, create a `config.py` file to store your Twilio credentials and the destination phone number.
   ```python
   # config.py

   account_sid = 'your_twilio_account_sid'
   auth_token = 'your_twilio_auth_token'
   phone_number = 'your_verified_whatsapp_phone_number'
   ```

5. **Export environment variables** (optional, depending on your setup):
   ```bash
   export TWILIO_ACCOUNT_SID=your_twilio_account_sid
   export TWILIO_AUTH_TOKEN=your_twilio_auth_token
   export PHONE_NUMBER=your_phone_number
   ```

## Usage

### 1. Fetch and Send WhatsApp Messages

- The main bot code is located in the `PyMotivator.py` file, which handles fetching quotes and sending them via WhatsApp.
- To run the bot and test sending a WhatsApp message, use:

   ```bash
   python3 PyMotivator.py
   ```

### 2. Twilio Connection Script

- The Twilio connection script (`twilio_conn.py`) handles connecting to Twilio's API and sending messages.
- You can test it by running:

   ```bash
   python3 twilio_conn.py
   ```

### 3. Schedule Daily WhatsApp Messages

- The `apscheduler` library is used to schedule the bot to send a WhatsApp message every day at 7 AM (Asia/Kolkata timezone). The scheduling logic is in `PyMotivator.py`.
- To start the scheduled job, just run:

   ```bash
   python3 PyMotivator.py
   ```

## Example Output

Upon running the script, you should receive a WhatsApp message with a motivational quote like this:

```
Quote: "The said truth is that it is the greatest happiness of the greatest number that is the measure of right and wrong."
Author: Jeremy Bentham
```

## Troubleshooting

1. **Twilio-related issues**: 
   Ensure your Twilio `account_sid` and `auth_token` are correct. Also, make sure the phone number is verified on your Twilio account.

2. **Scheduler not working**:
   Make sure the time zone is set correctly, and that the script continues running (it should not terminate immediately after starting).

3. **Module errors**:
   Ensure all required modules are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

## Contributing

If you'd like to contribute to PyMotivator, feel free to submit pull requests or open issues in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out to the project maintainer:
- **Amar Dharma Rakhpasre** (GitHub: [@amar-rakhpasre](https://github.com/amar-rakhpasre))

---

This README covers everything necessary to set up, run, and troubleshoot the PyMotivator bot project. If there are any additional features or changes you plan to make, you can update this README accordingly.
