# banking-service
Simple python project covering oops, dictionaries, lamabda and unit test

In the context of the `BankingSystem` interface, the operations at the interface layer define the core functionalities that any implementing class must provide. These operations are essentially method signatures that outline the expected behavior without providing the actual implementation. Here are the operations defined in the `BankingSystem` interface and their purposes:

1. **`create_account`**:
    ```python
    def create_account(self, timestamp: int, account_id: str, amount: int = 0) -> bool:
        pass
    ```
    - **Purpose**: This method is intended to create a new account in the banking system.
    - **Parameters**:
        - `timestamp`: An integer representing the time at which the account is created.
        - `account_id`: A string that uniquely identifies the account.
        - `amount`: An optional integer representing the opening balance of the account (default is 0).
    - **Return Value**: A boolean indicating whether the account creation was successful (`True`) or not (`False`).

2. **`transfer`**:
    ```python
    def transfer(self, timestamp: int, source_account_id: str, destination_account_id: str, amount: int) -> int | None:
        pass
    ```
    - **Purpose**: This method is intended to transfer a specified amount of money from one account to another.
    - **Parameters**:
        - `timestamp`: An integer representing the time at which the transfer is made.
        - `source_account_id`: A string that uniquely identifies the source account from which the money will be transferred.
        - `destination_account_id`: A string that uniquely identifies the destination account to which the money will be transferred.
        - `amount`: An integer representing the amount of money to be transferred.
    - **Return Value**: An integer representing the new balance of the source account after the transfer, or `None` if the transfer was unsuccessful (e.g., due to insufficient funds or invalid account IDs).

These operations define the essential actions that a banking system must support, such as creating accounts and transferring funds between accounts. The actual implementation of these methods will be provided by a class that implements the `BankingSystem` interface, such as `BankingSystemImpl`.
