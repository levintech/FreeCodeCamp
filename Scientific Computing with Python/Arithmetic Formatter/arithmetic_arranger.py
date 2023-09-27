def arithmetic_arranger(problems, showResult=False):
  if showResult:
    output_lines = [""] * 4
  else:
    output_lines = [""] * 3

  if len(problems) > 5:
    return "Error: Too many problems."

  for index, problem in enumerate(problems):
    (operand1, operator, operand2) = problem.split()
    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."
    elif not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."
    elif len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    result = 0
    if operator == "+":
      result = int(operand1) + int(operand2)
    else:
      result = int(operand1) - int(operand2)

    length = max([len(operand1), len(operand2)])

    output_lines[0] += operand1.rjust(length + 2)
    output_lines[1] += operator + operand2.rjust(length + 1)
    output_lines[2] += '-' * (length + 2)
    if showResult:
      output_lines[3] += str(result).rjust(length + 2)

    if index < len(problems) - 1:
      output_lines = [line + "    " for line in output_lines]

  arranged_problems = "\n".join(output_lines)
  return arranged_problems
