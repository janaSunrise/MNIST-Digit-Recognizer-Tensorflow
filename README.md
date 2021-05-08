# MNIST Digit Recognizer Tensorflow

> A Handwritten digit recognizer ML project in Tensorflow and Python.

## Running Demo

Here's a Demo on how it works

![alt text](https://github.com/janaSunrise/MNIST-Digit-Recognizer-Tensorflow/blob/main/assets/mnist_digit_prediction.gif)

## Installation and usage.

This project uses `pipenv` for dependency management. You need to ensure that you have `pipenv`
installed on your system.

Here's how to install the dependencies, and get started.

- Install it using **`pipenv sync -d`**
- Once done, spawn a shell to run the files: `pipenv shell`

And you're done, and you can run any of the files, and test them.

**Note**: There is a GUI Application built for testing too. You can run it by using `pipenv run start`.
The model might not be really good, But it performed decently on test set.

### Debugging

If you ever get a `ModuleNotFoundError`, Saying `tkinter` library is not found, No worries. Here are some tips to fix it:

- **Linux** | Execute this command to fix it: `sudo apt install python3-tk`
- **MacOS** | Execute this command to fix: `brew install python-tk`
- **Windows** | You need to reinstall python, And select the option to install tkinter and all other libraries when you install again.

### Project structure

This project has 3 main sections.

- `src/` Contains the python scripts for training the ML Models.
- `notebooks/` contains the jupyter notebooks with explanations and the outputs of our end
  goal.
- `models/` contains the exported model to make your work easy.
- `gui/` Contains the GUI app for testing the model.

## Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you
can just submit a PR to this repo and it will be deployed once it's accepted.

⚠️ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your
commit or the PR Created. Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/)
before making the commit message.

## Show your support

We love people's support in growing and improving. Be sure to leave a ⭐️ if you like the project and
also be sure to contribute, if you're interested!

<div align="center">
Made by Sunrit Jana with <3
</div>

