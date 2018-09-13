NAME = "script.py"

BODY = """ print 
'owl-stretching time'"""

try:
    compile(BODY, NAME, "exec")
except SyntaxError, v:
    print("syntax error:", v, "in", NAME)

print ("-" * 20)

BODY = """
print 'the  ant,an introduction'
"""
code = compile(BODY, "<script>", "exec")
print code
exec code

print('-' * 20)

import sys, string


class CodeGeneratorBackend:
    """Simple code generator"""

    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        self.code.append("")
        return compile(string.join(self.code, "\n"), "<code>", "exec")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level -= 1


c = CodeGeneratorBackend()
c.begin()
c.write("for i in range(5):")
c.indent()
c.write("print 'code generation made easy!'")
c.dedent()
exec c.end()
