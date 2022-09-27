class MethodsBase:
    base_fields = ("rpcaddr", "rpcport", "keystore", "password")
    automatic = False

    def __init__(self, **kw: dict) -> None:
        self.base_field_keys = kw.keys()
        self.set_fields(**kw)
        self.base_context = {
            k: v for k, v in kw.items() if k in self.base_fields if v != False
        }
        super(MethodsBase, self).__init__(**kw)

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v) if not isinstance(v, bool) else v)
