#!/usr/bin/env python
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import button_dialog
from pathlib import Path
import completer


wallet_completer = NestedCompleter.from_nested_dict(completer.words)
seed_path = str(Path.home()) + '/.wallet/seed.txt'
cursor = 'Ξ '

def main():

    """
    0. Startup Screen
        - check for seed stored in file
        - if true
            - buttons=[("Saved", "saved"), ("New, "new"), ("Import", "import")]
        - else
            - buttons=[("New, "new"), ("Import", "import")]
    """

    try:
        with open(seed_path) as f:
            seed = f.readlines()
            buttons = [("Saved", "saved"), ("New", "new"), ("Import", "import")]
            print(seed)  
    except IOError:
        buttons=[("New", "new"), ("Import", "import")]

    result = button_dialog(
        title="🌷 Tulip Wallet Cli 🌷",
        text="Initialise Seed",
        buttons=buttons
    ).run()

    print("Result = {}".format(result))

    """
    1. Main program loop
    """

if __name__ == "__main__":
    main()
