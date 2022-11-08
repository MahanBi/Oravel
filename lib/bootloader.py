class GRUB:
    """
    settings set in /etc/default/grub
    """
    def __init__(self, settings: dict):
        self.setting = settings

    def __repr__(self):
        ...

    def __str__(self):
        ...

    def __call__(self, *args, **kwargs):
        return self
