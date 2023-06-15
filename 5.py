class Indenter:
    def __init__(self):
        self.indentation = 0

    def __enter__(self):
        self.indentation += 2
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indentation -= 2

    def print(self, text):
        indentation_str = " " * self.indentation
        print(f"{indentation_str}{text}")



with Indenter() as indent:
    print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the Code.")
    print("Torvalds")
