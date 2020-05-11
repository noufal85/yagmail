try:
    import keyring
except (ImportError, NameError, RuntimeError):
    pass


def handle_password(user, password):  # pragma: no cover
    #print("hey")
    """ Handles getting the password"""
    if password is None:
        try:
            password = keyring.get_password("yagmail", user)
        except NameError as e:
            print(
                "'keyring' cannot be loaded. Try 'pip install keyring' or continue without. See https://github.com/kootenpv/yagmail"
            )
            raise e
        if password is None:
            raise ValueError("password for - {} not found".format(user))
    return password


def register(username, password):
    """ Use this to add a new gmail account to your OS' keyring so it can be used in yagmail """
    keyring.set_password("yagmail", username, password)
