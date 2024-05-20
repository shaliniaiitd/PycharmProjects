# GenAI Resume Builder


## Getting started
Ensure you are connected through VPN.

### Clone the Repository
To get started with the project, follow these steps to clone the repository to your local machine:
```
git clone --config http.sslVerify=false https://git.garage.lab.epam.com/genai-resume-builder/genai-resume-builder.git
cd genai-resume-builder
```

### Install Pipenv
Pipenv is used to manage dependencies and create virtual environments for the project. If you haven't already installed Pipenv, you can do so using pip:
```bash
pip install pipenv
```

### Create Virtual Environment
Once Pipenv is installed, you can use it to create a virtual environment for the project. Navigate to the project directory and run
```bash
pipenv install
```
This command will create a virtual environment for the project and install all required dependencies specified in the Pipfile.

### Activate Virtual Environment
To activate the virtual environment, use the following command
```bash
pipenv shell
```
This command will activate the virtual environment, and you should see the environment name (project-name) in your terminal prompt.

### Ensure .env file
Ensure there is .env file at the root level with following entry
AZURE_OPENAI_API_KEY = "<API_KEY>"

### Install required modules

pip install all packages mentioned in Pipfile.  
download antiword from the internet
extract zip file in C drive
add the address C:/antiword to path variable among user variables
create a new user variable called "ANTIWORDHOME" with same value, i.e C:/antiword

### Run the Project
Once the virtual environment is activated, you can run the project using the following command:
```bash
python app.py
```
This command will start the project, and you should see output indicating that the project is running.
```bash
Running on http://127.0.0.1:5000
```

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
