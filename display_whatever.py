class DisplayWhatever:
    NAME = "Display Whatever"
    CATEGORY = "utils"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("*", {}),  # accept anything
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "main"
    OUTPUT_NODE = True

    def main(self, value=None):
        try:
            text = str(value)
        except Exception:
            text = "[unprintable value]"

        return {"ui": {"text": (text,)}}
