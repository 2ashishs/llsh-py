# Large Language Model Powered AI Shell (LLSH)

A shell utility that allows you to generate shell command syntax for any scenario, specified by you, in natural language (currently english). Powered by a local LLM API (Ollama) and a language model (qwen2.5-coder).

### Usage

`llsh <natural language query for a shell command>`

Example:

`*llsh* list all files in current directory`

### Features

- [ ] Generate response for command line syntax query
 	- [x] Get environment variables from OS.
        - [ ] Clean natural language query.
 	- [x] Pass natural language query to Ollama + Language Model.
	- [x] Get response from Ollama + Language Model.
	- [x] Clean response.
	- [x] Return response to user to execute.
	- [ ] Allow user to specify API server from environment variable.
	- [ ] Allow user to specify model from environment variable or some other mechanism.
- [ ] Allow auto-completion of command
- [ ] Allow parsing through arguments of a command
	- [ ] Prefix a long complicated input command with our program and press return key.
	- [ ] Our program parses the command for arguments.
	- [ ] Step-wise allow the user to modify each argument.
	- [ ] Auto generate other possible outcomes for each argument, using AI.
- [ ] Add RAG & Internet Search.
- [ ] More to come...

### Dependencies

- Ollama + Suitable Model: For running language model locally.
- Open-WebUI [ToDO]: Cleaner interface to Ollama & the model.
