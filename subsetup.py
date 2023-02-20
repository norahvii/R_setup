import os
import subprocess

# get cwd and set the script path
cwd = os.getcwd()
script_path = cwd+"/Rsetup.R"

# execute R library installation script
subprocess.run(["Rscript", script_path])
print("All packages successfully installed.")
