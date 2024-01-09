# Stalker Tools

A small set of tools that I wrote personally for myself when there was a need. At the moment it can only copy textures, but this will also be enough, as for me.

## How to use

We indicate our paths in the settings, in the body file we indicate the path to the log, the easiest way would be to copy the file to the folder with the program and simply indicate its name. We launch and wait for execution.

## Settings

All information about setting up the program is described below.

### Basic arguments

Arguments for all operating modes (must be specified before writing the operating mode):

* **no_errors** - Disable errors
* **silent** - Disable masseges

### Pathes and formats

You can also specify some arguments in the `settings.json` file. For convenience, they have been placed in a separate file.

* **input** - Path to search files
* **output** - Path to copy files
* **file_types** - Which formats are needed

### Copying texures

Arguments for **textures**:

* **file** `FILE` - Path to the text file *(required for work)*
* **overwrite** - Overwrite a texture if it is already in the folder?
* **parse** - Analyze the log so that the program itself finds the missing textures
  
## Example for *.bat

Here is an example of how this program is usually used and with what arguments. In this case, we are copying textures with parsing the log and overwriting existing textures.

```powershell
env\Scripts\python main.py textures -file main.log -parse -overwrite
```
