# Broccoli

Broccoli aims to be a tool that serves as a bridge between game writers and game programmers

![ReadMe Diagram](img/README_Diagram.png)

The game writers will use the software, writing their item descriptions (or dialogues, or whatever needs text) and categorize each line as appropriate. Saving that project will create a file (.json) with a dictionary containing the text needed to implement in such a way that is easy for the programmer to later access in the game engine.

This will make it so that it's not necessarry to hardcode each line of text in the game engine's scripts, nor to spend team time  converting the text from the game writers to a format that can be used in a game engine.

Besides, the hability of the game writers to categorize each item of text will make it easier for the programmers to understand where each text should be applied.

<hr>

## How to install Broccoli

> Broccoli will eventually run on a server or site, but, for now, follow this instructions to actually use Broccoli

After you've clonned this repository, make sure you have [Node.js](https://nodejs.org/en/) installed, and some sort of code editor, like [Visual Studio Code](https://code.visualstudio.com/).

Then, run your terminal and navigate to the folder where you've clonned the repository, and open the "steamed-broccoli" folder
```
cd [Path_To_Repository]\steamed-broccoli
```
and then run
```
npm install -g @angular/cli
npm install
```
<br><br>
After that, whenever you want to run Broccoli, open a terminal, navigate to the `steamed-broccoli` folder, and run
```
npm serve -o
```

<hr>

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the  LGPL-3.0 License - see the [LICENSE](LICENSE) file for details