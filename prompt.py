from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import completer

wallet_completer = NestedCompleter.from_nested_dict(completer.words)
cursor = 'Ξ '

# create a prompt session
session = PromptSession()

user_input = session.prompt(cursor,
                            completer=wallet_completer,
                            auto_suggest=AutoSuggestFromHistory()
                           )
