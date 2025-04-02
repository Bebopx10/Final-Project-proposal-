import subprocess

Print{"Add Commit Push"}


# Print the output
print("Executing \"git space status\":")
Print("")

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)

print(resultGitStatus.stdout)
#print("STDERR:")
#print(result.stderr)

print("Executing \"git space status\":")
Print("")

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)

Print(resultGitStatus.stdout)
