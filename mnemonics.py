alphabet: str = "abcdefghijklmnopqrstuvwxyz"
buttons: str = "22233344455566677778889999"


def to_buttons(mnemonic: str) -> str:
    """Convert a mnemonic into a phone number"""
    pass


def from_buttons(button_sequence: str) -> str:
    """Convert a sequence of digits and pauses (represented by spaces) into text."""
    pass


if __name__ == "__main__":
    print("'(foo) bar-quuz' is: " + to_buttons("(foo) bar-quuz"))
    print("'3 444 222 8 444 666 66 2 777 444 33 7777 2 777 33 2 9 33 7777 666 6 33' is: " + from_buttons(
        "3 444 222 8 444 666 66 2 777 444 33 7777 2 777 33 2 9 33 7777 666 6 33"))
