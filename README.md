## Demo

You can see the results from this repository under: https://metrics.green-coding.org/ 
Please select the project which has the URL of this repository in the "URL" field.

## Repository Info
This repository contains a sample software to be measured with
the Green Metric Tool.

The software to be measured is arbitrary, as long as it can be orchestrated
with the format specified in usage_scenario.json.

Currently we only supply a sample for a command line application.
However, it will extended to web- and desktop-applications in the near future.


## Format

At the beginning of the file you should specify name, author, version and
architecture.
These will help you later on distinguish which version of the software was certified
if you use the repository url multiple times in the certification process.

Supported architecture for the moment is only "linux"


### Setup
The setup block is the starting point of the usage scenario.

- "name": A valid docker Container name [a-zA-Z0-9_]
- "type": Currently only "container" is supported
- "identifier": A valid identifier accessible on docker hub
- "portmapping": Expose a port to other containers for later use (optional)
- "setup-commands": Commands to be run before actual load testing. Mostly installs will be done here. Note that
your docker container must support these commands and you cannot rely on a standard linux installation to provide access to /bin (optional)

### Flow
Flow handles the actual load testing

- "name": An arbitrary name, that helps you distinguish later on where the load happend in the chart
- "container": The same name you specified on "Setup" where you want to run the following commands
- "commands": An array of objects
- "commands" -> "type": Only console currently supported
- "commands" -> "command": The command to be executed. Piping or moving to background is not supported. Note: This command will block execution. If you need parallel execution supply "detach"
- "commands" -> "detach": Detach process True / False (optional)
- "commands" -> "note": A string that will appear as note attached to the datapoint of measurement (optional)
