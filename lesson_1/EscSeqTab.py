from tabulate import tabulate
table = [["\\a Bell (alert)", "\a Alert"], ["\\b Backspace", "BB\backspace"],
         ["\\n New line", "New \n line"], ["\\t Horizontal tab", "Horizontal\ttab"],
         ["\\\ Backslash\ ", "\\Backslash\\"], ["\\\" Double quotation mark\"", '"Double"'],
         ["\\' Single quotation mark'", "'Single'"]]
print(tabulate(table, headers=("Escape sequences", "Result")))
