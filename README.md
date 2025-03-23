# PyTkChat

PyTkChat is a simple, real-time chat application built using Python and Tkinter. It provides a basic graphical user interface for multiple clients to connect to a central server and exchange messages.

## Features

*   **Real-time Chat:**  Clients can send and receive messages in real-time.
*   **Multi-Client Support:** The server handles multiple client connections concurrently using threads.
*   **Tkinter GUI:**  A simple and easy-to-use graphical interface for the client.
*   **Username Input:**  Clients are prompted to enter a username upon connection.
*   **Error Handling:**  Includes error handling for common network issues (disconnections, connection refused).
*   **Clear Code Structure:**  Organized into separate server (`server.py`) and client (`client_gui.py`) files for maintainability.

## Requirements

*   Python 3.x
*   Tkinter (usually comes pre-installed with Python)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-github-repo-url>
    cd PyTkChat
    ```
    Replace `<your-github-repo-url>` with the actual URL of your GitHub repository.

2.  **No additional package installations are required**, as Tkinter is typically included with standard Python installations. If you *do* encounter an error about Tkinter not being found, you may need to install it for your specific operating system. Consult the Python documentation for your OS.

## Usage

1.  **Run the Server:**  Open a terminal and start the server:

    ```bash
    python server.py
    ```

2.  **Run the Client(s):** Open *separate* terminal windows (or tabs) for each client you want to run. In each terminal, start a client:

    ```bash
    python client_gui.py
    ```

    Each client will be prompted to enter a username.

3.  **Chat:** Type messages in the client's entry field and press Enter (or click "Send") to send the message. Messages from all connected clients will be displayed in the chat log.

## Running with a Client in Google Colab (Optional)

You can run the *client* in a Google Colab notebook, while the *server* runs on your local machine.

1.  **Run the Server:** Start `server.py` on your local machine.
2.  **Get your Local/Public IP:**  Find your local network IP address (if the Colab notebook and your server are on the same network) or your public IP address (if they're on different networks).
3.  **Modify `client_gui.py` (in Colab):**
    *   Copy the `client_gui.py` code into a Colab notebook cell.
    *   Change the `HOST` variable in the `if __name__ == "__main__":` block to your local/public IP address.  *Do not* use `127.0.0.1` in the Colab client.
4.  **Run the Client in Colab:** Execute the modified code cell.
5.  **Firewall:** Ensure your local machine's firewall allows incoming connections on the chosen port (default is 12345).

## Project Structure

*   `server.py`:  The server-side code.  Handles client connections and message broadcasting.
*   `client_gui.py`: The client-side code, including the Tkinter GUI.

## Contributing

Contributions are welcome!  If you find a bug or have a feature suggestion, please open an issue or submit a pull request.


