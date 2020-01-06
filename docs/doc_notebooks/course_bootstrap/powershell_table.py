# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Bash and powershell command reference
#
# | Cmdlet | Alias | Bash Equivalent | Description |
# | ------- | ------- | ------- | ------- |
# | `Get-ChildItem` | `gci` | `ls` | List the directories and files in the current location. | 
# | `Set-Location` | `sl` | `cd` | Change to the directory at the given path. Typing `..` rather than a path will move up one directory. |
# | `Push-Location` | `pushd` | `pushd` | Changes to the directory. |
# | `Pop-Location` | `popd` | `popd` | Changes back to the previous directory after using `pushd` |
# | `New-Item` | `ni` | (`touch`) | Creates a new item. Used with no parameter, the item is by default a file. Using `mkdir` is a shortcut for including the parameter `-ItemType dir`. |
# | `mkdir` | none | `mkdir` | Creates a new directory. (See `New-Item`.) |
# | `Explorer` | `start .` | `open .`) | Open something using File Explorer (the GUI) |
# | `Remove-Item` | `rm` | `rm` | Deletes something. Permanently! |
# | `Move-Item` | `mv` | `mv` | Moves something. Takes two arguments - first a filename (i.e. its present path), then a path for its new location (including the name it should have there). By not changing the path, it can be used to rename files. |
# | `Copy-Item` | `cp` | `cp` | Copies a file to a new location. Takes same arguments as move, but keeps the original file in its location. |
# | `Write-Output` | `write` | `echo` | Outputs whatever you type. Use redirection to output to a file. Redirection with `>>` will add to the file, rather than overwriting contents. |
# | `Get-Content` | `gc` | `cat` | Gets the contents of a file and prints it to the screen. Adding the parameter `-TotalCount` followed by a number x prints only the first x lines. Adding the parameter `-Tail` followed by a number x prints only the final x lines. |
# | `Select-String` | `sls` | (`grep`) | Searches for specific content. |
# | `Measure-Object` | `measure` | (`wc`) | Gets statistical information about an object. Use `Get-Content` and pipe the output to `Measure-Object` with the parameters `-line`, `-word`, and `-character` to get word count information. |
# | `>` | none | `>` |Redirection. Puts the output of the command to the left of `>` into a file to the right of `>`. |
# | `|` | none | `|` |Piping. Takes the output of the command to the left and uses it as the input for the command to the right. |
# | `Get-Help` | none | `man` | Gets the help file for a cmdlet. Adding the parameter `-online` opens the help page on TechNet. |
# | `exit` | none | `exit` | Exits PowerShell |
#
# Remember the keyboard shortcuts of `tab` for auto-completion and the up and down arrows to scroll through recent commands. These shortcuts can save a lot of typing!

# %%
