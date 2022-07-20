# From https://www.youtube.com/watch?v=keSvLnLNep4&ab_channel=NeuralNine
# cd <to here>
# conda create --name exec_vs_eval python=3.7
# conda activate exec_vs_eval
# pip install -r requirements.txt
# Be wary of using exec and eval, especially if accepting input from users
# These take strings as input and then executes/evaluates it
# Eval also returns output

print(eval("1 + 1"))
print(exec("1 + 1"))

# Below looks like a 'ctf' flag:
# CTF is capture the flag
# Presumably competitions are organized around trying to build programs
# to achieve specific tasks, such as CTF
MYSECRET_PASSWORD = "YOU WILL NEVER KNOW"

varname = input("Please enter a variable name: ")
varval = input("Please enter a value for the variable: ")

exec(f"{varname} = {varval}")

print(f"The value of your variable is now: {eval(varname)}")

# If the user runs this program and enters MYSECRET_PASSWORD
# for variable name and for variable, then your secret
# variable would be printed to the console

# If the user sends malicious code when you try to accept varname
# then that code will be eavaluated.
# Example, if the user inputs open('mynewfile.txt', 'w').write('GOTCHA')

# If the user sends: open('secret.txt', 'r')

# your secret will print to the console

# eval/exec are to be avoided at all costs if creating an app that users
# willl send any input to
