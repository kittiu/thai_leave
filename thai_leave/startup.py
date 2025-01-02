from thai_leave import monkey_patch  # <-- Important: Load monkey_patch

def boot_session(bootinfo):
    """ Fake call boot_session to load monkey_patch """
